Vous suivez consciencieusement les étapes suivantes :
1. Vous vous rapprochez d’un ou plusieurs collaborateurs pour la
réalisation du projet.
2. Vous récupérez des données gracieusement fournies par une agence
immobilière ici. Vous avez le choix entre deux datasets.
## We here
3. Vous consultez vos données et vous créez une feuille de route du
projet. Énumérez les tâches puis estimez leur durée. Estimez les
ressources humaines et matérielles (nombre de personnes
impliquées dans le projet, les machines utilisées pour le
_3
développement de l’outil).
4. Vous créez votre repository github ainsi qu’un tableau Trello afin de
répartir, équitablement, les tâches du projet.
5. Traitez et nettoyez vos données. Vous devrez traiter les données
manquantes (par imputation ou suppression), les dublicats, les
données aberrantes et tout autre donnée dont la modification
(normalisation, standardisation, ...) est pertinente. Chaque choix doit
être justifié et argumenté.
6. Réalisez une analyse exploratoire complète de vos données à l’aide de
l’outil Power BI.
7. Documentez vous sur les algorithmes de régression et rédigez un
descriptif du fonctionnement d’au moins 3 de ces algorithmes. Pensez
à utiliser des schémas d’illustration. Vous avez le choix de fournir votre
documentation sous forme du readme de votre repository ou d’un
fichier PDF.
8. Analysez et sélectionnez les caractéristiques (features) à modéliser.
Employez différentes méthodes afin d’apporter une solution finale
(Boruta, forward feature selection, ...).
9. Entraînez au moins 3 algorithmes de prédiction du prix des biens
immobiliers puis évaluez et comparez leur performance.
10. Les résultats ne vous conviennent pas ? Utilisez la méthode du grid
search afin d’identifier le modèle (et les paramètres) avec les
meilleures performances possibles.
_4
11. Déployez le modèle sélectionné sur une application Flask. Le visuel
doit être un minimum travaillé.
12. Docker est une technologie de conteneurisation qui permet
d'encapsuler une application et ses dépendances dans un conteneur
léger et portable. En créant un script Docker, vous assurez que votre
application et son environnement de développement sont
reproductibles et peuvent être exécutés de manière cohérente sur
n'importe quel environnement, qu'il s'agisse d'un ordinateur local, d'un
serveur de production ou d'un service cloud.
Créez un script Docker permettant d’installer les dépendances
nécessaires à votre application, copier les fichiers de votre
application dans le conteneur, et spécifier la commande à exécuter
lorsque le conteneur démarre (par exemple, lancer votre application
Flask).
