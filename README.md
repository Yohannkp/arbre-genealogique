# Arbre Généalogique Modulaire (D3.js)

Ce projet est une application web 100% front-end pour visualiser, éditer et exporter un arbre généalogique de grande taille, optimisée pour desktop, mobile et tablette.

## 🚀 Fonctionnalités principales
- **Affichage interactif** de l’arbre généalogique avec D3.js (pan/zoom, survol, détails, recherche…)
- **Responsive** : ergonomie mobile/tablette (Android/iOS et web)
- **Ajout/édition/suppression** de personnes, unions, parentés
- **Import/Export** : JSON, ZIP, Excel, PDF
- **Statistiques dynamiques**
- **Boutons d’action adaptés** (mobile/desktop)
- **Centrage automatique** de l’arbre

## 📁 Fichiers à placer dans le dépôt
- `clan_atchr_tree.html` (application principale)
- `persons.json` (liste des personnes)
- `unions.json` (liste des unions)
- `parentages.json` (liens parent/enfant)

## 🌐 Déploiement sur GitHub Pages
1. Créez un dépôt public sur votre compte GitHub (ex : `arbre-genealogique`).
2. Placez-y les fichiers ci-dessus.
3. Activez GitHub Pages : Settings > Pages > Source : `main` et `/ (root)`.
4. Accédez à : `https://<votre-utilisateur>.github.io/<nom-du-repo>/`

Un script PowerShell (`deploy_and_create_repo.ps1`) est fourni pour automatiser la création du dépôt, le push et l’ouverture de la page GitHub Pages.

## 🛠️ Technologies
- D3.js v7
- HTML5/CSS3 (responsive, media queries)
- JSZip, xlsx, html2pdf.js (import/export)

## 📱 Mobile/tablette
- Les boutons d’action sont accessibles en bas de l’écran.
- Les overlays (fiches, formulaires, stats) sont adaptés et ne sont jamais masqués.

## 📝 Personnalisation
- Modifiez les fichiers JSON pour adapter les données.
- Le code est commenté et modulaire pour faciliter l’évolution.

## 🤝 Contributions
Pull requests bienvenues !

## Licence
MIT
