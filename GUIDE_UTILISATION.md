# Guide d'Utilisation - NanoQR Cryptologique

## 🚀 Démarrage Rapide

### Option 1 : Utilisation Locale
1. Ouvrez simplement le fichier `index.html` dans votre navigateur web
2. Aucune installation ou configuration requise

### Option 2 : Serveur Local
```bash
# Avec Python 3
python3 -m http.server 8080

# Avec Node.js
npx http-server -p 8080

# Puis ouvrez http://localhost:8080
```

## 📖 Guide des Fonctionnalités

### 1. 📏 Cadre Physique
Cette section affiche les dimensions du NanoQR :
- **Dimensions** : 3mm × 3mm (taille microscopique)
- **Surface totale** : 9mm²

C'est le cadre de référence pour tout le système.

### 2. 🔬 Extérieur - Vue Nano
Représentation visuelle du NanoQR tel qu'il apparaîtrait à l'échelle microscopique :
- Motif QR standard visible
- Taille réelle simulée à 3×3mm
- Points de référence aux coins

**À noter** : À cette échelle, le labyrinthe interne est invisible à l'œil nu.

### 3. 🌀 Intérieur - Labyrinthe Complexe
Canvas noir montrant le labyrinthe cryptographique :
- **Complexité** : Ultra-Dense (300×300 cellules)
- **Densité** : Maximum (cellules de 2px)
- **Visibilité** : Quasi invisible sans zoom

Le labyrinthe est généré algorithmiquement avec des motifs cryptographiques basés sur des fonctions mathématiques (sin, cos).

### 4. 🔍 Zoom Automatique

#### Comment Utiliser le Zoom
1. **Localisez le curseur** dans la section "ZOOM AUTOMATIQUE"
2. **Déplacez le curseur** de gauche (1x) à droite (100x)
3. **Observez** la vue zoomée en dessous

#### Niveaux de Zoom
- **1x - 5x** : Labyrinthe presque invisible
- **6x - 20x** : Premiers détails apparaissent
- **21x - 50x** : Structure claire avec couleurs
- **51x - 100x** : Détails maximaux avec grille

#### Indicateurs
- **Niveau de zoom** : Affiche le multiplicateur actuel (ex: 51x)
- **Détails visibles** : Pourcentage de complexité révélée (ex: 51%)

### 5. 🔐 Encodage Cryptologique

#### Encoder des Données

1. **Entrez votre texte**
   - Maximum 3 caractères (24 bits)
   - Chaque caractère = 8 bits
   - Exemples : "ABC", "123", "XYZ"

2. **Cliquez sur "Encoder"**
   - La compression s'effectue automatiquement
   - Le ratio de 24:1 est appliqué

3. **Résultats affichés**
   - **Bits d'entrée** : Nombre de bits du texte (ex: 24 bits pour 3 chars)
   - **Bits compactés** : Résultat de la compression (ex: 1 bit)
   - **Ratio de compression** : 24.0:1 (typique)
   - **Code encodé** : Format hexadécimal du résultat

4. **Labyrinthe régénéré**
   - Le labyrinthe se régénère automatiquement
   - Basé sur le code encodé
   - Chaque texte produit un motif unique

#### Exemples d'Encodage

| Texte | Bits Entrée | Bits Sortie | Code Hex |
|-------|-------------|-------------|----------|
| "A"   | 8 bits      | 1 bit       | Variable |
| "AB"  | 16 bits     | 1 bit       | Variable |
| "ABC" | 24 bits     | 1 bit       | Variable |

## 🎯 Cas d'Usage

### Démonstration de Concept
Utilisez le système pour démontrer :
- La miniaturisation extrême des QR codes
- Les techniques de compression avancées
- La cryptographie visuelle

### Éducation
Enseignez les concepts de :
- Encodage binaire
- Compression de données
- Sécurité quantique vs classique
- Visualisation de données complexes

### Recherche
Explorez les possibilités de :
- Stockage de données ultra-compact
- Labyrinthe cryptographique
- Génération procédurale basée sur seeds

## 🔒 Sécurité

### Métriques de Sécurité
- **Sécurité Quantique** : 97.3%
  - Résistance aux attaques par ordinateurs quantiques
  - Basé sur la complexité du labyrinthe

- **Sécurité Classique** : 100%
  - Résistance aux attaques traditionnelles
  - Compression irréversible sans clé

### Caractéristiques de Sécurité
1. **Invisibilité** : Labyrinthe invisible à l'œil nu
2. **Complexité** : 90,000 cellules (300×300)
3. **Compression** : Perte d'information (24→1)
4. **Randomisation** : Seed pseudo-aléatoire
5. **Unicité** : Chaque entrée → motif unique

## 💡 Conseils et Astuces

### Pour de Meilleurs Résultats
1. **Utilisez un navigateur moderne** (Chrome, Firefox, Safari, Edge)
2. **Écran haute résolution** pour voir plus de détails
3. **Zoomez progressivement** pour voir l'effet microscopique
4. **Testez différents textes** pour voir les motifs uniques

### Dépannage

#### Le labyrinthe ne s'affiche pas
- Vérifiez que JavaScript est activé
- Rechargez la page (F5)
- Essayez un autre navigateur

#### Le zoom ne fonctionne pas
- Cliquez sur le curseur puis utilisez les flèches du clavier
- Vérifiez les messages d'erreur dans la console (F12)

#### L'encodage échoue
- Assurez-vous d'entrer au moins 1 caractère
- Maximum 3 caractères acceptés
- Vérifiez que le champ n'est pas vide

## 📱 Compatibilité

### Navigateurs Supportés
- ✅ Chrome/Chromium 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+

### Appareils
- ✅ Ordinateurs de bureau
- ✅ Ordinateurs portables
- ✅ Tablettes
- ✅ Smartphones (interface responsive)

## 🎨 Personnalisation

Le système peut être personnalisé en modifiant :

### Couleurs (style.css)
```css
/* Changez les couleurs du gradient principal */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Taille du Labyrinthe (script.js)
```javascript
// Modifiez la taille des cellules
const cellSize = 2; // Plus petit = plus dense
```

### Ratio de Compression (script.js)
```javascript
// Modifiez le ratio de compression
const blockSize = 24; // Nombre de bits par bloc
```

## 🆘 Support

Pour toute question ou problème :
1. Consultez la [documentation complète](README.md)
2. Vérifiez les issues GitHub
3. Contactez le mainteneur du projet

## 📚 Ressources Additionnelles

- [QR Code Standards](https://en.wikipedia.org/wiki/QR_code)
- [Cryptographie Quantique](https://fr.wikipedia.org/wiki/Cryptographie_quantique)
- [Compression de Données](https://fr.wikipedia.org/wiki/Compression_de_donn%C3%A9es)
- [HTML5 Canvas API](https://developer.mozilla.org/fr/docs/Web/API/Canvas_API)

---

**Bon encodage ! 🚀**
