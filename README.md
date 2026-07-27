# Résumeur de texte local

Ce projet permet de résumer un texte grâce à une intelligence artificielle. Il fonctionne avec une API locale, ce qui signifie que vous pouvez l’utiliser sur votre ordinateur sans avoir besoin d’un service externe.

## À quoi sert ce projet ?

Vous envoyez un texte au serveur, puis le serveur renvoie une version plus courte et plus simple du texte.

Cette idée est utile pour :
- résumer des articles
- comprendre rapidement des longs documents
- gagner du temps lors de la lecture

## Modèle utilisé

Le projet utilise le modèle suivant :
- facebook/bart-large-cnn

Ce modèle a été choisi parce qu’il est simple à utiliser, efficace pour résumer du texte et adapté à un premier projet local.

## Prérequis

Avant de commencer, il faut installer :
- Python 3.9 ou plus
- pip
- un accès à Internet pour télécharger le modèle

## Étape 1 : créer un environnement virtuel

Dans le dossier du projet, exécutez :

```bash
python -m venv .venv
```

Sur Windows, activez l’environnement avec :

```powershell
.venv\Scripts\Activate.ps1
```

## Étape 2 : installer les dépendances

```bash
pip install -r requirements.txt
```

## Étape 3 : créer votre fichier d’environnement

Copiez le fichier d’exemple :

```bash
copy .env.example .env
```

Puis ouvrez le fichier .env et remplacez la valeur par votre propre jeton Hugging Face :

```text
TOKEN_HUGGINFFACE=VotreJetonIci
```

Si vous n’avez pas de jeton, vous pouvez en créer un sur Hugging Face.

## Étape 4 : lancer le serveur local

Depuis la racine du projet, exécutez :

```bash
uvicorn main:app --reload
```

Le serveur sera disponible à l’adresse :

```text
http://127.0.0.1:8000
```

## Étape 5 : tester l’API

Vous pouvez tester l’API avec une requête HTTP POST vers :

```text
http://127.0.0.1:8000/summarize
```

Exemple de corps JSON :

```json
{
  "text": "Les grands groupes technologiques investissent massivement dans l'intelligence artificielle pour améliorer la productivité, automatiser certaines tâches et proposer de nouveaux services."
}
```

## Structure du projet

- main.py : démarrage de l’API FastAPI
- service.py : logique de résumé
- model.py : chargement du modèle
- schema.py : définition des données envoyées et reçues
- requirements.txt : dépendances Python

## Conseils pour les débutants

- Si le téléchargement du modèle prend du temps, attendez simplement.
- Si vous voyez une erreur liée à un jeton, vérifiez votre fichier .env.
- Si l’API ne répond pas, vérifiez que le serveur est bien lancé et que le port 8000 est libre.

## Résumé rapide

Pour lancer le projet rapidement :

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```
