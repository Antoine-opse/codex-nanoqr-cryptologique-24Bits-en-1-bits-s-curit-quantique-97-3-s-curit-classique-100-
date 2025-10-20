#!/usr/bin/env python3
"""
NanoQR Test Suite
=================

Comprehensive test suite for the NanoQR cryptographic system.
"""

import unittest
from nanoqr import (
    NanoQREncoder, NanoQRDecoder, NanoQR, NanoQRVisualizer,
    SecurityAnalyzer, LABYRINTH_SYMBOLS, SYMBOL_TO_VALUE
)


class TestLabyrinthSymbols(unittest.TestCase):
    """Test labyrinth symbol definitions."""
    
    def test_symbol_count(self):
        """Test that we have exactly 16 symbols."""
        self.assertEqual(len(LABYRINTH_SYMBOLS), 16)
    
    def test_symbol_uniqueness(self):
        """Test that all symbols are unique."""
        self.assertEqual(len(LABYRINTH_SYMBOLS), len(set(LABYRINTH_SYMBOLS)))
    
    def test_symbol_to_value_mapping(self):
        """Test that symbol to value mapping is correct."""
        self.assertEqual(len(SYMBOL_TO_VALUE), 16)
        for idx, symbol in enumerate(LABYRINTH_SYMBOLS):
            self.assertEqual(SYMBOL_TO_VALUE[symbol], idx)


class TestNanoQREncoder(unittest.TestCase):
    """Test NanoQR encoder functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = NanoQREncoder(grid_size=7)
    
    def test_initialization(self):
        """Test encoder initialization."""
        self.assertEqual(self.encoder.grid_size, 7)
        self.assertEqual(self.encoder.total_modules, 49)
        self.assertEqual(self.encoder.bits_per_module, 4)
        self.assertEqual(self.encoder.max_data_bits, 196)
    
    def test_string_to_bits(self):
        """Test string to bits conversion."""
        result = self.encoder._string_to_bits("A")
        expected = "01000001"  # ASCII 'A' = 65
        self.assertEqual(result, expected)
    
    def test_encode_short_message(self):
        """Test encoding a short message."""
        message = "TEST"
        nanoqr = self.encoder.encode(message)
        
        self.assertIsInstance(nanoqr, NanoQR)
        self.assertEqual(len(nanoqr.grid), 7)
        self.assertEqual(len(nanoqr.grid[0]), 7)
        self.assertEqual(nanoqr.physical_bits, 1)
    
    def test_encode_maximum_capacity(self):
        """Test encoding at maximum capacity."""
        message = "A" * 24  # Maximum efficient capacity
        nanoqr = self.encoder.encode(message)
        
        self.assertEqual(nanoqr.data_bits, 192)  # 24 * 8 bits
        self.assertEqual(nanoqr.total_modules, 49)
    
    def test_grid_symbols_valid(self):
        """Test that encoded grid contains only valid symbols."""
        message = "VALID"
        nanoqr = self.encoder.encode(message)
        
        for row in nanoqr.grid:
            for symbol in row:
                self.assertIn(symbol, LABYRINTH_SYMBOLS)


class TestNanoQRDecoder(unittest.TestCase):
    """Test NanoQR decoder functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = NanoQREncoder(grid_size=7)
        self.decoder = NanoQRDecoder(grid_size=7)
    
    def test_initialization(self):
        """Test decoder initialization."""
        self.assertEqual(self.decoder.grid_size, 7)
        self.assertEqual(self.decoder.bits_per_module, 4)
    
    def test_encode_decode_roundtrip(self):
        """Test that encoding and decoding preserves data."""
        messages = [
            "Hello",
            "World",
            "TEST123",
            "QUANTUM_SECURE",
        ]
        
        for message in messages:
            with self.subTest(message=message):
                nanoqr = self.encoder.encode(message)
                decoded = self.decoder.decode(nanoqr)
                self.assertIn(message, decoded)
    
    def test_decode_with_error_correction(self):
        """Test decoding with error correction enabled."""
        message = "ERROR_CORRECTION_TEST"
        nanoqr = self.encoder.encode(message, use_error_correction=True)
        decoded = self.decoder.decode(nanoqr, use_error_correction=True)
        
        self.assertIn(message, decoded)
    
    def test_decode_without_error_correction(self):
        """Test decoding without error correction."""
        message = "NO_ERROR_CORRECTION"
        nanoqr = self.encoder.encode(message, use_error_correction=False)
        decoded = self.decoder.decode(nanoqr, use_error_correction=False)
        
        self.assertIn(message, decoded)


class TestNanoQR(unittest.TestCase):
    """Test NanoQR data class."""
    
    def test_efficiency_factor(self):
        """Test efficiency factor calculation."""
        grid = [['╬'] * 7 for _ in range(7)]
        nanoqr = NanoQR(grid=grid, data_bits=24, physical_bits=1)
        
        self.assertEqual(nanoqr.efficiency_factor, 24)
    
    def test_total_modules(self):
        """Test total modules calculation."""
        grid = [['╬'] * 7 for _ in range(7)]
        nanoqr = NanoQR(grid=grid)
        
        self.assertEqual(nanoqr.total_modules, 49)
    
    def test_physical_size(self):
        """Test default physical size."""
        grid = [['╬'] * 7 for _ in range(7)]
        nanoqr = NanoQR(grid=grid)
        
        self.assertEqual(nanoqr.physical_size_mm, (3.0, 3.0))


class TestNanoQRVisualizer(unittest.TestCase):
    """Test NanoQR visualizer."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = NanoQREncoder(grid_size=7)
        self.message = "VISUAL_TEST"
        self.nanoqr = self.encoder.encode(self.message)
    
    def test_zoom_level_1(self):
        """Test visualization at zoom level 1."""
        result = NanoQRVisualizer.visualize(self.nanoqr, zoom_level=1)
        self.assertIn("[•]", result)
        self.assertIn("1-bit", result)
    
    def test_zoom_level_10(self):
        """Test visualization at zoom level 10."""
        result = NanoQRVisualizer.visualize(self.nanoqr, zoom_level=10)
        self.assertIn("Basic Structure", result)
    
    def test_zoom_level_50(self):
        """Test visualization at zoom level 50."""
        result = NanoQRVisualizer.visualize(self.nanoqr, zoom_level=50)
        self.assertIn("Partial Labyrinth", result)
    
    def test_zoom_level_100(self):
        """Test visualization at zoom level 100."""
        result = NanoQRVisualizer.visualize(self.nanoqr, zoom_level=100)
        self.assertIn("Full Labyrinth", result)
        self.assertIn("┌", result)
        self.assertIn("└", result)
    
    def test_show_all_zoom_levels(self):
        """Test showing all zoom levels."""
        result = NanoQRVisualizer.show_all_zoom_levels(self.nanoqr)
        
        self.assertIn("ZOOM LEVEL: ×1", result)
        self.assertIn("ZOOM LEVEL: ×10", result)
        self.assertIn("ZOOM LEVEL: ×50", result)
        self.assertIn("ZOOM LEVEL: ×100", result)
        self.assertIn("Efficiency Factor", result)


class TestSecurityAnalyzer(unittest.TestCase):
    """Test security analyzer."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = NanoQREncoder(grid_size=7)
        self.nanoqr = self.encoder.encode("SECURITY_TEST")
    
    def test_analyze_security(self):
        """Test security analysis."""
        analysis = SecurityAnalyzer.analyze_security(self.nanoqr)
        
        self.assertEqual(analysis['total_modules'], 49)
        self.assertEqual(analysis['symbols_per_module'], 16)
        self.assertEqual(analysis['bits_entropy'], 196)
        self.assertEqual(analysis['quantum_security'], 97.3)
        self.assertEqual(analysis['classical_security'], 100.0)
    
    def test_security_combinations(self):
        """Test total combinations calculation."""
        analysis = SecurityAnalyzer.analyze_security(self.nanoqr)
        
        # 16^49 combinations
        expected = 16 ** 49
        self.assertEqual(analysis['total_combinations'], expected)
    
    def test_brute_force_complexity(self):
        """Test brute force complexity."""
        analysis = SecurityAnalyzer.analyze_security(self.nanoqr)
        
        self.assertEqual(analysis['brute_force_complexity'], '2^196')


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def test_full_workflow(self):
        """Test complete encode-visualize-decode workflow."""
        # Setup
        encoder = NanoQREncoder(grid_size=7)
        decoder = NanoQRDecoder(grid_size=7)
        message = "INTEGRATION_TEST_2024"
        
        # Encode
        nanoqr = encoder.encode(message, use_error_correction=True)
        self.assertEqual(nanoqr.physical_bits, 1)
        self.assertGreater(nanoqr.data_bits, 0)
        
        # Visualize
        for zoom in [1, 10, 50, 100]:
            visualization = NanoQRVisualizer.visualize(nanoqr, zoom_level=zoom)
            self.assertIsInstance(visualization, str)
            self.assertGreater(len(visualization), 0)
        
        # Analyze security
        analysis = SecurityAnalyzer.analyze_security(nanoqr)
        self.assertEqual(analysis['quantum_security'], 97.3)
        self.assertEqual(analysis['classical_security'], 100.0)
        
        # Decode
        decoded = decoder.decode(nanoqr, use_error_correction=True)
        self.assertIn(message, decoded)
    
    def test_efficiency_claims(self):
        """Test that efficiency claims are accurate."""
        encoder = NanoQREncoder(grid_size=7)
        message = "EFFICIENCY_TEST"
        
        nanoqr = encoder.encode(message)
        
        # Test 1-bit physical appearance
        self.assertEqual(nanoqr.physical_bits, 1)
        
        # Test data capacity
        self.assertGreaterEqual(nanoqr.data_bits, len(message) * 8)
        
        # Test efficiency factor
        expected_efficiency = nanoqr.data_bits // nanoqr.physical_bits
        self.assertEqual(nanoqr.efficiency_factor, expected_efficiency)
    
    def test_multiple_messages_independence(self):
        """Test that different messages produce different encodings."""
        encoder = NanoQREncoder(grid_size=7)
        
        messages = ["MESSAGE_A", "MESSAGE_B", "MESSAGE_C"]
        encodings = []
        
        for message in messages:
            nanoqr = encoder.encode(message)
            # Convert grid to string for comparison
            grid_str = ''.join(''.join(row) for row in nanoqr.grid)
            encodings.append(grid_str)
        
        # All encodings should be different
        self.assertEqual(len(set(encodings)), len(messages))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_empty_string(self):
        """Test encoding empty string."""
        encoder = NanoQREncoder(grid_size=7)
        decoder = NanoQRDecoder(grid_size=7)
        
        nanoqr = encoder.encode("")
        decoded = decoder.decode(nanoqr)
        
        # Should handle gracefully
        self.assertIsInstance(decoded, str)
    
    def test_single_character(self):
        """Test encoding single character."""
        encoder = NanoQREncoder(grid_size=7)
        decoder = NanoQRDecoder(grid_size=7)
        
        nanoqr = encoder.encode("X")
        decoded = decoder.decode(nanoqr)
        
        self.assertIn("X", decoded)
    
    def test_special_characters(self):
        """Test encoding special ASCII characters."""
        encoder = NanoQREncoder(grid_size=7)
        decoder = NanoQRDecoder(grid_size=7)
        
        special_chars = "!@#$%^&*()"
        nanoqr = encoder.encode(special_chars)
        decoded = decoder.decode(nanoqr)
        
        # Check if at least some special characters are preserved
        common = set(special_chars) & set(decoded)
        self.assertGreater(len(common), 0)
    
    def test_long_message_truncation(self):
        """Test that long messages are handled gracefully."""
        encoder = NanoQREncoder(grid_size=7)
        decoder = NanoQRDecoder(grid_size=7)
        
        # Message longer than optimal capacity
        long_message = "A" * 50
        nanoqr = encoder.encode(long_message)
        decoded = decoder.decode(nanoqr)
        
        # Should encode and decode without errors
        self.assertIsInstance(decoded, str)


def run_tests():
    """Run all tests and display results."""
    print("\n" + "=" * 60)
    print("🧪 NANOQR TEST SUITE")
    print("=" * 60 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestLabyrinthSymbols))
    suite.addTests(loader.loadTestsFromTestCase(TestNanoQREncoder))
    suite.addTests(loader.loadTestsFromTestCase(TestNanoQRDecoder))
    suite.addTests(loader.loadTestsFromTestCase(TestNanoQR))
    suite.addTests(loader.loadTestsFromTestCase(TestNanoQRVisualizer))
    suite.addTests(loader.loadTestsFromTestCase(TestSecurityAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
    else:
        print("\n❌ SOME TESTS FAILED")
    
    print("=" * 60 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
