# Remote Relay - Render

Projet de relais WebSocket entre deux ordinateurs via Render.

## 1. Deployer sur Render

Envoyer ces fichiers dans un depot GitHub puis creer un Web Service Render.

Le fichier `render.yaml` configure automatiquement :
- Python
- installation des dependances
- lancement de FastAPI/Uvicorn

Apres le deploiement, le service sera disponible sous une adresse du type :

https://remote-relay-xxxx.onrender.com

## 2. Configurer les clients

Dans `client.py` et `operator.py`, remplacer :

TON-SERVICE.onrender.com

par le domaine reel de Render.

Exemple :

SERVER = "wss://remote-relay-xxxx.onrender.com"

## 3. Installer sur les PC

Lancer :

install.bat

## 4. Creer une session

Sur le PC operateur :

start_operator.bat

Un code a 6 chiffres sera affiche.

## 5. Rejoindre la session

Sur le PC client :

start_client.bat

Entrer le code affiche par l'operateur.

## Limites

Cette version est uniquement un relais de messages authentifie par code de session.
Elle ne capture pas l'ecran et ne controle pas le clavier ou la souris.
