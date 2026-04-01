# Contributing to Tabular-Benchmark-MLOps

Merci de l'intérêt porté à ce projet ! 🎉

---

## 🤝 Code de Conduite

Soyez **respectueux et constructifs** dans toutes les interactions.

---

## 🎯 Comment Contribuer

1.  **Issues** : Vérifiez les issues existantes.
2.  **Branches** : `feature/nom-fonctionnalité` depuis `main`.
3.  **Commits** : Messages clairs (Conventional Commits).
4.  **Tests** : `pytest` doit passer.
5.  **Linting** : `pre-commit` avant push.

---

## 🛠 Setup de Développement

```powershell
# 1. Créer l'environnement virtuel
python -m venv .venv

# 2. Activer l'environnement virtuel
.\.venv\Scripts\Activate.ps1

# 3. Installer le projet avec dépendances de développement
pip install -e .[dev]

# 4. Installer les hooks pre-commit
pre-commit install
```

---

## 🔄 Pull Requests

Les PR doivent :

-   ✅ Passer la CI
-   ✅ Inclure des tests si nouvelle fonctionnalité
-   ✅ Mettre à jour le README si besoin

---

## 🔧 Dépannage & FAQ

### ❓ PowerShell affiche `>` rouge et n'exécute pas

**Symptôme :** Vous voyez un chevron `>` rouge au lieu de `PS >` normal.

**Cause :** Un délimiteur de chaîne multi-lignes mal fermé (`@' ... '@`).

**Solution :**

```powershell
# ✅ CORRECT - Les délimiteurs doivent être SEULS sur leur ligne
$script = @'
ligne 1
ligne 2
'@

# ❌ INCORRECT - PowerShell attend indéfiniment
$script = '@'
ligne 1
'@
```

**Règles d'or :**

| Élément | Correct ✅ | Incorrect ❌ |
| :--- | :--- | :--- |
| **Ouverture** | `@'` (seul sur ligne) | `'@'` (avec quote autour) |
| **Fermeture** | `'@` (seul sur ligne) | `'@'` (avec quote autour) |
| **Espaces avant** | Aucun | `  '@` |

**Sortie d'urgence :** Appuyez sur `Ctrl+C` jusqu'au retour de `PS >`

---

### 🅿️ Analogie : Le "Frein de Parking" PowerShell

Ce comportement est une **sécurité** plutôt qu'un bug :

| Métaphore | Voiture 🚗 | PowerShell 💻 |
| :--- | :--- | :--- |
| **Frein de parking** | Empêche la voiture de rouler | `@'` non fermé empêche l'exécution |
| **Témoin d'alerte** | Voyant rouge au tableau de bord | Chevron `>` rouge dans le terminal |
| **Débloquer** | Relâcher le frein | Fermer avec `'@` seul sur ligne |
| **Démarrer** | Tourner la clé | Appuyer sur Entrée après fermeture |

**Leçon :** Cette "erreur" est une **protection** contre l'exécution accidentelle de scripts incomplets ou dangereux ! 🛡️

---

## 📞 Besoin d'Aide ?

-   📖 **[README.md](README.md)** - Documentation complète
-   🐛 **[Issues](https://github.com/valorisa/Tabular-Benchmark-MLOps/issues)** - Signaler un bug
-   💡 **[Feature Request](https://github.com/valorisa/Tabular-Benchmark-MLOps/issues)** - Suggérer une idée

---

*Merci à tous les contributeurs qui aident à rendre ce projet meilleur !* 🎉

*Projet conçu par valorisa pour démonstration MLOps pédagogique.*