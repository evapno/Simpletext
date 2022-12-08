# Tâches SimpleText@CLEF-2022

[Accueil](./) | [Appel à contributions](./CFP) | [Dates importantes](./dates) | [Tâches](./tasks)  | [Outils](./tools) 
[Programme](./program) | [Publications](./publications) | [Organisateurs](./organisers) | [Contact](./contact) | [CLEF-2023](https://simpletext-project.com/2023/clef)


---

## Directives pour les tâches SimpleText

Nous vous invitons à soumettre aussi bien des parcours automatiques que manuels ! Les interventions manuelles doivent être signalées.

---

<button>[Accès](./tasks)</button> | <button>[Tâche partagée 1](./task1)</button> | <button>[Tâche partagée 2](./task2)</button> | <button>[Tâche partagée 3](./task3)</button>| <button>[Tâche non-partagée 4](./task4)</button>

<br>

## Tâche 3 : Réécris ça ! En fonction d'une requête, simplifier des passages de résumés scientifiques. 

Le but de cette tâche est de fournir une version simplifiée de passages de texte (phrases) par rapport à une requête. Les participants recevront des requêtes et des résumés d'articles scientifiques. Les résumés peuvent être divisés en phrases. Les passages simplifiés seront évalués manuellement avec l'utilisation éventuelle de métriques d'agrégation.

**Format d'entrée :** 
Les données de formation et de test sont fournies dans les formats JSON et CSV avec les champs suivants :
* *snt_id*: un identifiant unique de passage (phrase) 
* *source_snt*: un passage de texte
* *doc_id*: un identifiant unique de document source
* *query_id*: une requête d'identification
* *query_text*: simplification à faire par rapport à cette requête

*Exemple d'entrée:*

*{"snt_id":"G11.1_2892036907_2","source_snt":"With the ever increasing number of unmanned aerial vehicles getting involved in activities in the civilian and commercial domain, there is an increased need for autonomy in these systems too.","doc_id":2892036907,"query_id":"G11.1","query_text":"drones"}*

**Foramt de sortie:** 
Liste des termes à contextualiser dans un **format JSON** ou un fichier tabulé TSV (pour les runs manuels) avec les champs suivants :
* *run_id*: ID d'exécution qui commence par **team_id_task_3_**
* *manual*: si l'exécution est manuelle {0,1}
* *snt_id*: un identifiant unique de passage (phrase) du fichier d'entrée 
* *simplified_snt*: Texte du passage simplifié 

*Exemple de sortie*:
{"run_id":"BTU_task_3_run1","manual":1,"snt_id":"G11.1_2892036907_2","simplified_snt":"Drones are increasingly used in the civilian and commercial domain and need to be autonomous."}

*Vérificateur du format de sortie*

Vous pouvez utiliser ce script python3 pour vérifier le format de sortie. Le script nécessite Python 3 et la bibliothèque Pandas : [Télécharger python output checker](../check_format.py)

**Disclaimer:** En téléchargeant et en utilisant ces données, vous acceptez les conditions d'utilisation. Toute utilisation des données à des fins autres que la recherche universitaire constituerait une violation de l'utilisation prévue de ces données. 

Par conséquent, en téléchargeant et en utilisant ces données, vous donnez les assurances suivantes concernant les données SimpleText :
1. Vous n'utiliserez ni ne permettrez à d'autres d'utiliser les données des ensembles de données SimpleText de quelque manière que ce soit, sauf pour les cours et la recherche universitaire
2. À aucun moment vous ne divulguerez, ne donnerez ou ne transmettrez (de quelque manière, sous quelque forme ou à quelque fin que ce soit) les données (ou toute partie de celles-ci) à quelque endroit ou personne que ce soit, y compris, mais sans s'y limiter, en rendant les données disponibles sur Internet et en copiant les données sur tout système de stockage en nuage
3. Vous ne divulguerez pas et ne permettrez pas à d'autres de divulguer l'ensemble de données ou toute partie de celui-ci à quiconque. 

En cas de violation des conditions d'accès aux données à des fins scientifiques, cet accès peut être retiré à l'entité de recherche et/ou au chercheur. L'entité de recherche peut également être tenue de payer des dommages et intérêts à des tiers ou être invitée à prendre des mesures disciplinaires à l'encontre du chercheur fautif. 

### Évaluation
Les passages simplifiés seront évalués manuellement avec l'utilisation éventuelle de métriques d'agrégation.

### Soumission des résultats :
Les participants doivent placer leurs résultats d'exécution dans le dossier Documents créé pour leur utilisateur et les **soumettre par e-mail** à *contact@simpletext-project.com*.

L'objet de l'e-mail doit être dans le format **[CLEF TASK 3] TEAM\_ID**. 

Les séries doivent être soumises sous la forme d'un dossier ZIP contenant les fichiers JSON correspondants. Les passages manuels peuvent être soumis en format CSV. 

Un courriel de confirmation sera envoyé dans les deux jours suivant la date limite de soumission. 

## Comment citer un document
Si vous étendez ou utilisez ce travail, veuillez citer [l'article](https://doi.org/10.1007/978-3-031-13643-6_28) où il a été introduit :
```
Liana Ermakova, Eric SanJuan, Jaap Kamps, Stéphane Huet, Irina Ovchinnikova, Diana Nurbakova, 
Sílvia Araújo, Radia Hannachi, Elise Mathurin, et Patrice Bellot. 2022. 
Vue d'ensemble du Laboratoire Simpletext CLEF 2022 : "Automatic Simplification of Scientific Texts". 
"In Experimental IR Meets Multilinguality, Multimodality, and Interaction" : 13e Conférence internationale de la CLEF Association, CLEF 2022, Bologne, Italie, 5-8 septembre, 2022, Compte-rendus. 
Springer-Verlag, Berlin, Heidelberg, 470–494. https://doi.org/10.1007/978-3-031-13643-6_28
```
[Article](https://doi.org/10.1007/978-3-031-13643-6_28)

[Téléchargez .BIB](../../BibTeX/ermakova_overview_2022.bib)
