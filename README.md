# projet_2
## Description du projet :
Le projet consiste a développer un script qui permet de suivre les prix des livres sur le site http://books.toscrape.com/.

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
Ces données sont stockées dans des fichiers CSV qui sont classés par catégorie.

En deuxième temps, les images des livres sont téléchargées dans les dossier de la catégorie correspondante.

### 1-Création et activation de l’environnement virtuel:
- Ouvrir un terminal de commande (ex:powershell).
- A l’aide de la commande pwd trouver votre emplacement sur l’ordinateur.
- A l’aide de la commande cd placez vous dans le répertoire qui contient le projet.
- Taper la commande python -m venv nom (nom= choisissez un nom a donner à votre environnement). 
- Taper la commande .python\nom\Scripts\Activate.ps1 pour activer votre environnement virtuel.

### 2-Exécution du code de l’application :
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
git clone https://github.com/Mya1212/P2-NG.git

- Placez vous dans le dossier OC_P2_BooksToScrape, puis créez un nouvel environnement virtuel:

python -m venv env

- Ensuite, activez-le.
Windows:
env\scripts\activate.bat

Linux:

source env/bin/activate

- Il ne reste plus qu'à installer les packages requis:

pip install -r requirements.txt

- Vous pouvez enfin lancer le script:

python main.py

    

