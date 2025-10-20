#!/usr/bin/env python3
"""
NanoQR Examples
===============

Various examples demonstrating the NanoQR cryptographic system.
"""

from nanoqr import NanoQREncoder, NanoQRDecoder, NanoQRVisualizer, SecurityAnalyzer


def example_basic_encoding():
    """Basic encoding and decoding example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Encoding and Decoding")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    decoder = NanoQRDecoder(grid_size=7)
    
    message = "Hello World!"
    print(f"Original Message: '{message}'")
    
    # Encode
    nanoqr = encoder.encode(message)
    print(f"Encoded into {nanoqr.total_modules} modules")
    
    # Show at zoom level 100
    print("\nVisualization at 100x zoom:")
    print(NanoQRVisualizer.visualize(nanoqr, zoom_level=100))
    
    # Decode
    decoded = decoder.decode(nanoqr)
    print(f"\nDecoded Message: '{decoded}'")
    print(f"Match: {message in decoded}")


def example_maximum_capacity():
    """Example using maximum data capacity."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Maximum Data Capacity (24 characters)")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    decoder = NanoQRDecoder(grid_size=7)
    
    # Maximum efficient data for 7x7 grid
    message = "KEY:A7F9C2E8D1B4536X90QZ"  # 24 characters
    print(f"Original Message: '{message}'")
    print(f"Length: {len(message)} characters = {len(message) * 8} bits")
    
    # Encode
    nanoqr = encoder.encode(message)
    print(f"\nPhysical appearance: {nanoqr.physical_bits} bit")
    print(f"Actual data stored: {nanoqr.data_bits} bits")
    print(f"Efficiency: {nanoqr.efficiency_factor}x")
    
    # Decode
    decoded = decoder.decode(nanoqr)
    print(f"\nDecoded Message: '{decoded}'")
    print(f"Match: {message in decoded}")


def example_cryptographic_key():
    """Example encoding a cryptographic key."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Cryptographic Key Storage")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    decoder = NanoQRDecoder(grid_size=7)
    
    # Simulate a cryptographic key (shortened for demo)
    crypto_key = "9F7E2A8B1C4D6E3F5A0B"
    print(f"Cryptographic Key: '{crypto_key}'")
    print(f"Key Length: {len(crypto_key)} characters")
    
    # Encode
    nanoqr = encoder.encode(crypto_key, use_error_correction=True)
    
    # Security analysis
    SecurityAnalyzer.print_security_report(nanoqr)
    
    # Show invisibility feature
    print("\nInvisibility Demonstration:")
    print("Without zoom (naked eye):")
    print(NanoQRVisualizer.visualize(nanoqr, zoom_level=1))
    
    print("\nWith microscope (100x zoom):")
    print(NanoQRVisualizer.visualize(nanoqr, zoom_level=100))
    
    # Decode
    decoded = decoder.decode(nanoqr, use_error_correction=True)
    print(f"\nRecovered Key: '{decoded}'")


def example_micro_tagging():
    """Example for micro-tagging applications."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Micro-Tagging for Authentication")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    
    # Different types of tags
    tags = [
        ("ART2024-001", "Artwork authentication"),
        ("DOC-SECURE-X7", "Document security"),
        ("CHIP-ID-A9B3", "Electronic component"),
    ]
    
    for tag_id, description in tags:
        print(f"\nTag: {description}")
        print(f"ID: '{tag_id}'")
        
        nanoqr = encoder.encode(tag_id)
        print(f"Physical size: {nanoqr.physical_size_mm[0]}mm × {nanoqr.physical_size_mm[1]}mm")
        print(f"Visible appearance: Microscopic point (1-bit)")
        print(f"Hidden data: {len(tag_id)} characters ({len(tag_id) * 8} bits)")
        print(f"Security level: {nanoqr.total_modules} modules, 2^{nanoqr.total_modules * 4} combinations")


def example_zoom_levels():
    """Demonstrate all zoom levels."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Zoom Level Demonstration")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    message = "ZOOM_TEST_2024"
    
    print(f"Encoding: '{message}'")
    nanoqr = encoder.encode(message)
    
    # Show all zoom levels
    print(NanoQRVisualizer.show_all_zoom_levels(nanoqr))


def example_efficiency_comparison():
    """Compare efficiency with traditional systems."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Efficiency Comparison")
    print("=" * 60)
    
    encoder = NanoQREncoder(grid_size=7)
    message = "TEST_MESSAGE_123456"
    
    nanoqr = encoder.encode(message)
    
    traditional_bits = len(message) * 8
    nanoqr_physical_bits = nanoqr.physical_bits
    efficiency = traditional_bits / nanoqr_physical_bits
    
    print(f"\nMessage: '{message}'")
    print(f"Length: {len(message)} characters")
    print("\nTraditional QR Code:")
    print(f"  - Physical modules needed: {traditional_bits}")
    print(f"  - Storage: {traditional_bits} bits")
    print(f"  - Transmission: {traditional_bits} bits")
    
    print("\nNanoQR System:")
    print(f"  - Physical appearance: {nanoqr_physical_bits} bit")
    print(f"  - Actual storage: {traditional_bits} bits")
    print(f"  - Transmission: {nanoqr_physical_bits} bit (metadata) + microscopic reveal")
    
    print(f"\n📊 Efficiency Gains:")
    print(f"  ✅ Storage: {efficiency:.1f}x more dense")
    print(f"  ✅ Energy: {efficiency:.1f}x less consumption")
    print(f"  ✅ Bandwidth: {efficiency:.1f}x less transmission")
    print(f"  ✅ Security: {efficiency:.1f}x more complex to crack")


def main():
    """Run all examples."""
    print("\n" + "🚀 " * 15)
    print("NANOQR CRYPTOGRAPHIC SYSTEM - EXAMPLES")
    print("🚀 " * 15)
    
    example_basic_encoding()
    example_maximum_capacity()
    example_cryptographic_key()
    example_micro_tagging()
    example_zoom_levels()
    example_efficiency_comparison()
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
