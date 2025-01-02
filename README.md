# Logiciel de Tournoi d'Échecs

Ce projet est une application de gestion de tournois d'échecs développée en Python. Elle permet de créer des tournois, d'ajouter des joueurs, d'organiser des matchs, d'enregistrer les résultats, et d'afficher des rapports détaillés.

---

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/santultimate/Logiciel-de-tournoi-d-checs.git
   cd nom-du-repo
   ```

2. **Créer et activer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur MacOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les données :**
   - Assurez-vous que le répertoire `data/` contient les fichiers nécessaires :
     - `players.json` : liste des joueurs enregistrés.
     - `tournaments.json` : liste des tournois sauvegardés.

---

## Fonctionnalités

- **Création de tournois :**
  - Saisissez le nom, le lieu, les dates et une description du tournoi.
  
- **Ajout de joueurs :**
  - Enregistrez des joueurs avec leur nom, prénom, date de naissance, et identifiant national d'échecs.

- **Organisation des matchs :**
  - Générez automatiquement des paires de joueurs pour chaque tour.

- **Enregistrement des résultats :**
  - Saisissez les scores pour chaque match. Les points sont automatiquement attribués en fonction des résultats.

- **Affichage des rapports :**
  - Liste des joueurs par ordre alphabétique.
  - Liste des tournois et leurs détails.
  - Historique des tours et matchs d'un tournoi.
  - Classement final des joueurs.

---

## Utilisation

Pour exécuter le logiciel :
```bash
python main.py
```

### Navigation dans le menu principal :
1. Créer un nouveau tournoi.
2. Charger un tournoi existant.
3. Ajouter un joueur.
4. Commencer un nouveau tour.
5. Enregistrer les résultats d'un match.
6. Terminer le tour actuel.
7. Afficher les rapports.
8. Terminer le tournoi et afficher le classement.
9. Quitter.

---

## Analyse de code avec `flake8`

Pour générer un rapport de conformité au style PEP 8, utilisez l'outil `flake8`.

1. **Installer `flake8` :**
   ```bash
   pip install flake8
   ```

2. **Exécuter l'analyse :**
   ```bash
   flake8 --max-line-length=119 --format=html --htmldir=flake8-report
   ```

   - Cette commande générera un rapport HTML dans le répertoire `flake8-report`.

3. **Consulter le rapport :**
   - Ouvrez le fichier `flake8-report/index.html` dans un navigateur pour visualiser les résultats.

---

## Structure du projet

```
Logiciel-de-tournoi-d-echecs/
|-- controllers/
|   |-- menu_controller.py
|   |-- player_controller.py
|   |-- tournament_controller.py
|
|-- models/
|   |-- player.py
|   |-- match.py
|   |-- round.py
|   |-- tournament.py
|
|-- views/
|   |-- report_view.py
|   |-- tournament_view.py
|
|-- data/
|   |-- players.json
|   |-- tournaments.json
|
|-- main.py
|-- requirements.txt
|-- README.md
```

---

## Contributeurs
- **YACOUBA SANTARA/SANTULTIMATE**
- Contributions et suggestions sont les bienvenues via des pull requests.