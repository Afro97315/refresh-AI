# refresh-AI
API pour décoloniser l 'IA
# RE-Educ'-IA Core

> **API de décolonisation de l’IA**  
> Par **Indye Gyal'Z Corporation** – Y-GYALAB  
> *"Une IA pensée PAR nous, POUR nous."*

## 🔧 Fonctionnalités

- Détecter les biais raciaux, eurocentrés, sexistes
- Reformuler un texte de manière inclusive
- Ajouter du contexte historique colonial
- Générer des prompts décolonisés

## 🚀 Déployer sur Render

1. Créez un nouveau **Web Service** sur Render
2. Connectez votre repo GitHub
3. Language : **Python**
4. Build Command : `pip install -r requirements.txt`
5. Start Command : `gunicorn app:app`
6. Port : **10000** (par défaut)
7. Cliquez sur **Create Web Service**

✅ L’API sera disponible à : https://refresh-ai.onrender.com 

## 📡 Endpoints

- `POST /detect` → Détecte les biais
- `POST /reformulate` → Reformule sans biais
- `POST /contextualize` → Ajoute du contexte
- `POST /prompt` → Génère un prompt décolonisé

## 🛡️ Licence
Ce projet est protégé par les droits d’auteur d’Indye Gyal'Z Corporation.  
Toute utilisation commerciale ou redistribution doit être autorisée.
