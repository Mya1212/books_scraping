# Projet_2
## Description du projet :
Le projet consiste à développer un script qui permet de suivre les prix des livres sur le site http://books.toscrape.com/.

En premier temps,le script extrait les données suivantes :
- URL du livre
 - Universal Product Code (upc)
 - Titre du livre
 - Prix, taxe incluse
 - Prix, taxe exclue
 - Quantité disponible
 - Description du produit
 - Catégorie
 - Rating
 - URL de l'image
 - Chemin local de l'image téléchargée

Ces données sont stockées dans des fichiers CSV, un fichier par catégorie.

En deuxième temps, les images des livres sont téléchargées dans les dossier de la catégorie correspondante.

### Execution du code :
- Commencez tout d'abord par installer Python

- Lancez la console, placez vous dans le dossier de votre choix grace à la commande cd

- Clonez ce repository:

    git clone https://github.com/Mya1212/books_scraping.git

- Placez vous dans le dossier books_scraping, puis créez un nouvel environnement virtuel:

    python -m venv env

- Activez votre environnement virtuel:

    Windows:
env\scripts\activate.bat

    Linux:
source env/bin/activate

- Il ne reste plus qu'à installer les packages requis:

    pip install -r requirements.txt

- Vous pouvez enfin lancer le script:

    python main.py

    

