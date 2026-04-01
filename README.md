# Tabular Benchmark MLOps

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/valorisa/tabular-benchmark-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/valorisa/tabular-benchmark-mlops/actions/workflows/ci.yml)

## 🎯 Objectif du Projet

Ce dépôt est une référence pédagogique et technique pour le benchmarking de modèles sur des données tabulaires. Il compare trois approches majeures :

1.  **Scikit-Learn** (Random Forest)
2.  **XGBoost** (Gradient Boosting)
3.  **PyTorch** (Multi-Layer Perceptron)

Le projet est conçu pour être **exécutable immédiatement** (données synthétiques), **structuré comme un projet production** (MLOps), et **compatible Windows/PowerShell**.

## 🚀 Démarrage Rapide (Windows 11 / PowerShell)

### 1. Prérequis

Assurez-vous d'avoir les outils suivants installés :

-   **Python 3.11+** : [Télécharger](https://www.python.org/downloads/)
-   **Git** : [Télécharger](https://git-scm.com/download/win)
-   **Compte Weights & Biases** : [Inscription gratuite](https://wandb.ai/)

### 2. Installation

Ouvrez **PowerShell 7** et naviguez vers le projet :

`powershell
cd C:\Users\bbrod\Projets\tabular-benchmark-mlops
`

Créez un environnement virtuel et activez-le :

`powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
`

Installez les dépendances :

`powershell
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
`

### 3. Configuration Weights & Biases

Connectez-vous à W&B :

`powershell
wandb login
`

*Pour tester sans compte, ajoutez le flag --offline.*

### 4. Lancement du Benchmark

#### Classification (XGBoost)

`powershell
python src/main.py --task classification --model xgboost --epochs 100
`

#### Régression (PyTorch)

`powershell
python src/main.py --task regression --model pytorch --epochs 50
`

#### Benchmark Complet

`powershell
python src/main.py --task classification --model all --epochs 100
`

## 📂 Structure du Projet

`	ext
.
├── configs/            # Fichiers de configuration YAML
├── src/                # Code source principal
│   ├── main.py         # Point d'entrée CLI
│   ├── data.py         # Génération et preprocessing
│   ├── models.py       # Définition des modèles
│   ├── train.py        # Boucle d'entraînement
│   └── evaluate.py     # Métriques et évaluation
├── tests/              # Tests unitaires
├── .github/            # Workflows CI et templates
└── README.md
`

## 🛠 Commandes Utiles (PowerShell)

| Action | Commande PowerShell |
| :--- | :--- |
| **Installer** | pip install -e . |
| **Tester** | pytest tests/ -v |
| **Linter** | pre-commit run --all-files |
| **Entraîner** | python src/main.py --task classification --model all |
| **Nettoyer** | Remove-Item -Recurse -Force __pycache__, .venv |

## 📊 Métriques Suivi

-   **Classification** : Accuracy, F1-Score, Loss
-   **Régression** : RMSE, R², Loss
-   **Système** : Temps d'entraînement (via W&B)

## 🤝 Contribuer

1.  Forker le projet
2.  Créer une branche (git checkout -b feature/nom)
3.  Committer (git commit -m 'Add feature')
4.  Pusher (git push origin feature/nom)
5.  Ouvrir une Pull Request

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les détails.

## 📄 Licence

Distribué sous la licence MIT. Voir [LICENSE](LICENSE).

## 🙏 Remerciements

-   **Scikit-Learn** : Datasets synthétiques
-   **Weights & Biases** : Tracking d'expériences
-   **PyTorch & XGBoost** : Moteurs d'entraînement

---
*Projet conçu par valorisa pour démonstration MLOps pédagogique.*