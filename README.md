# Tournois d'Echec

Description:

Ce programme est un système de gestion de tournois qui permet de créer des joueurs, des tournois et de suivre l'évolution des matchs et des scores. 
Il utilise une interface en ligne de commande et est structuré selon le modèle MVC (Modèle-Vue-Contrôleur).

# Fonctionnalités principales 
- **Création de joueurs** : Ajouter de nouveaux joueurs avec des informations telles que le nom, prénom, date de naissance, et un identifiant unique. 
- **Création de tournois** : Créer un tournoi avec un nom, un lieu, une description, une date de début et une date de fin.  
- **Gestion des matchs** : Enregistrer les scores des matchs entre joueurs et déterminer le gagnant. 
- **Affichage des résultats** : Afficher les résultats des matchs et des tournois. 
- **Rapports** : Générer des rapports sur les joueurs et les tournois (liste, résultats, etc.).

# Installation:
# Prérequis
*Système d'exploitation : Windows, macOS, Linux
*Python 3.8 ou supérieur 

## Etape 1: Se mettre à la racine du projet:
cd Projet4\CentreEchecs

## Etape 2: Clonez le dépôt :
git clone https://github.com/Laureopean/Projet4.git

## Etape 3: Pour créer environnement virtuel :
python -m venv Projet4
- fonctionne sous windows, Linux et MacOs.

# Pour activer l'environnement sous Linux et MacOS
source Projet4/bin/activate

# Pour activer l'environnement sous windows
projet4\Scripts\activate

## Etape 4: Installez les dépendances nécessaires :
pip install -r requirements.txt

## Etape 5: Flake8 :
- **Installer** :Flake8 : pip install flake8-html
- **Configurer** : setup.csg avec format = html
- **Executez** : flake8 - cela générera un rapport HTML.
- **Ouvrez** : flake8-rapport/index.html pour voir le résultat.

# Résultat sous :
**Linux**: xdg-open flake8-report/index.html
**Mac** :open flake8-report/index.html 
**Windows** : start flake8-report\index.html

## Etape 6: Lancez le programme :
python main.py

## Etape 7: Résultat Final :
![image](https://github.com/user-attachments/assets/461961ab-974d-4740-82b4-d6a1e70bed24)
