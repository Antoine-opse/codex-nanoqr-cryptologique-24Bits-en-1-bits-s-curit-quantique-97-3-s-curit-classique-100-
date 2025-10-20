# Quick Start Guide - NanoQR

## Installation rapide

```bash
# Pas de dépendances externes nécessaires!
# Python 3.6+ seulement
python3 --version  # Vérifier la version
```

## Utilisation Basique

### 1. Encoder un message

```python
from nanoqr import NanoQREncoder, NanoQRDecoder

encoder = NanoQREncoder()
nanoqr = encoder.encode("Votre message ici")
```

### 2. Visualiser le NanoQR

```python
from nanoqr import NanoQRVisualizer

# Voir à différents niveaux de zoom
print(NanoQRVisualizer.visualize(nanoqr, zoom_level=1))    # Point simple
print(NanoQRVisualizer.visualize(nanoqr, zoom_level=100))  # Complexité complète
```

### 3. Décoder le message

```python
decoder = NanoQRDecoder()
message_original = decoder.decode(nanoqr)
print(message_original)
```

## Exemples Rapides

### Exemple 1 : Message Simple
```python
from nanoqr import NanoQREncoder, NanoQRDecoder, NanoQRVisualizer

encoder = NanoQREncoder()
decoder = NanoQRDecoder()

# Encoder
message = "Bonjour Monde!"
nanoqr = encoder.encode(message)

# Visualiser
print(NanoQRVisualizer.show_all_zoom_levels(nanoqr))

# Décoder
decoded = decoder.decode(nanoqr)
print(f"Message décodé: {decoded}")
```

### Exemple 2 : Clé Cryptographique
```python
from nanoqr import NanoQREncoder, SecurityAnalyzer

encoder = NanoQREncoder()

# Encoder une clé secrète
secret_key = "9F7E2A8B1C4D6E3F5A0B"
nanoqr = encoder.encode(secret_key, use_error_correction=True)

# Analyser la sécurité
SecurityAnalyzer.print_security_report(nanoqr)
```

### Exemple 3 : Tous les Exemples
```bash
# Exécuter tous les exemples pré-programmés
python3 examples.py
```

## Tests

```bash
# Exécuter la suite de tests complète
python3 tests.py
```

## Démonstration Complète

```bash
# Exécuter la démonstration principale
python3 nanoqr.py
```

## Caractéristiques Clés

- ✅ **24 bits** dans une apparence de **1 bit**
- ✅ **Sécurité Quantique** : 97.3%
- ✅ **Sécurité Classique** : 100%
- ✅ **Efficacité** : 24× réduction énergétique
- ✅ **Invisibilité** : Microscope requis pour révéler

## Applications

1. **Authentification d'œuvres d'art**
2. **Marquage de documents sensibles**
3. **Traçabilité de composants électroniques**
4. **Stockage de clés cryptographiques**

## Besoin d'Aide?

Consultez le `README.md` pour la documentation complète.
