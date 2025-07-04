# Script PowerShell pour créer le repo GitHub, publier le code et activer GitHub Pages
# Placez ce fichier dans le dossier du projet (contenant clan_atchr_tree.html, *.json, README.md)

# === CONFIGURATION ===
$repo = "arbre-genealogique"
$user = "Yohannkp"
$token = Read-Host "Collez ici votre token GitHub personnel (repo scope requis)"

# === 1. Création du repo sur GitHub via l’API ===
$headers = @{ Authorization = "token $token"; "User-Agent" = "$user" }
$body = @{ name = $repo; description = "Arbre généalogique D3.js responsive"; private = $false } | ConvertTo-Json
$uri = "https://api.github.com/user/repos"
$response = Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -Body $body
if ($response.full_name) {
    Write-Host "Dépôt créé : $($response.html_url)"
} else {
    Write-Host "Erreur lors de la création du dépôt. Vérifiez le token ou si le dépôt existe déjà."
    exit 1
}

# === 2. Initialisation du dépôt local ===
if (-not (Test-Path ".git")) {
    git init
    git branch -M main
}

# === 3. Ajout des fichiers et commit ===
git add clan_atchr_tree.html *.json README.md
git commit -m "Déploiement initial de l’arbre généalogique"

# === 4. Ajout du remote et push ===
git remote remove origin 2>$null
git remote add origin "https://Yohannkp:$token@github.com/$user/$repo.git"
git push -u origin main

# === 5. Ouvre la page de configuration GitHub Pages ===
Start-Process "https://github.com/$user/$repo/settings/pages"
Write-Host "Dans la page qui s’ouvre, choisissez : branche main, dossier / (root), puis validez."
Write-Host "Votre site sera bientôt disponible sur : https://$user.github.io/$repo/"
