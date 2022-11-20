# Projet déploiement : Impact des retards avec GetAround

![image](https://user-images.githubusercontent.com/96300465/202905294-fa20ea95-12a3-486e-9d63-2559adbff01e.png)

## 1. Objectif

GetAround est une plateforme française de location de voitures entre particuliers. Lorsqu'ils utilisent Getaround, les conducteurs réservent des voitures pour une durée déterminée, d'une heure, à quelques jours. Ils sont censés ramener la voiture à l'heure, mais il arrive de temps en temps que les conducteurs soient en retard lors de la restitution du véhicule.

Les retours tardifs peuvent générer des problèmes pour le loueur, surtout si la voiture était supposée être relouée durant ce délai.

L'objectif est donc de regarder l'impact de ces retards sur les locations de véhicule. En parallèle, un outil d'optimisation du prix multicritères a été developpé pour pouvoir donner un tarif evolutif selon les caractéristiques du véhicule loué.

## 2. Data overview

Deux datasets sont disponibles, le premier, appelé dataset_delay qui contient les données que chaque réservation : 
![image](https://user-images.githubusercontent.com/96300465/202905572-7afe1b27-9708-466f-bee2-c60a3ae6891d.png)

L'autre dataset_pricing qui contient les informations concernant les véhicules et leurs options :
![image](https://user-images.githubusercontent.com/96300465/202905597-4abf9588-49ad-43f4-a3d2-7a018a4b8e64.png)

## 3. Aperçu des résultats 

Les données concernant les retards sont représentées par un dashboard développé sur streamlit, disponible en <a href='https://deploiement-jedha-getaround.herokuapp.com/'>cliquant ici, onglet Dashboard :</a>

![image](https://user-images.githubusercontent.com/96300465/202905684-bad0025d-ce23-4161-8bbd-020faaa5de14.png)

L'outil de prédiction des prix des véhicules est disponible dans la version streamlit en <a href='https://deploiement-jedha-getaround.herokuapp.com/'>cliquant ici, onglet Prédiction :</a> ou en utilisant <a href='https://fastapideployjedha2.herokuapp.com/'>l'endpoint via l'outil request, développé avec FastAPI</a> :

![image](https://user-images.githubusercontent.com/96300465/202905712-e0a56ab3-46c7-4677-87f6-ff0eb6545774.png)


## 4. Crédits
