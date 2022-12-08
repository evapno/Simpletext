# Tâches SimpleText@CLEF-2022


[Accueil](./) | [Appel à contributions](./CFP) | [Dates importantes](./dates) | [Tâches](./tasks)  | [Outils](./tools) 
[Programme](./program) | [Publications](./publications) | [Organisateurs](./organisers) | [Contact](./contact) | [CLEF-2023](https://simpletext-project.com/2023/clef)


---

## Directives pour les tâches SimpleText

Nous vous invitons à soumettre aussi bien des interventions automatiques que manuelles ! Les interventions manuelles doivent être signalées.

---

<button>[Accès](./tasks)</button> | <button>[Tâche partagée 1](./task1)</button> | <button>[Tâche partagée 2](./task2)</button> | <button>[Tâche partagée 3](./task3)</button>| <button>[Tâche non-partagée 4](./task4)</button>

<br>

## Tâche 1:  Ce qui est dedans (ou dehors) ? Sélectionner les passages à inclure dans un résumé simplifié, à partir d'une requête.

La tâche vise à trouver des références en informatique qui pourraient être insérées comme citations dans des articles de presse originaux d'audience générale à des fins d'illustration, de vérification des faits ou d'actualisation. Pour chacune des références sélectionnées, des phrases plus pertinentes doivent être extraites. Ces passages peuvent être complexes et nécessitent une simplification supplémentaire qui sera effectuée dans les tâches 2 et 3. La tâche 1 se concentre sur l'extraction de contenu.

**Corpus: DBLP + résumés**

Nous utilisons la base de données Citation Network : DBLP+Citation, [ACM Citation network](https://www.aminer.org/citation). Un index ElasticSearch est fourni aux participants, accessible via une API GUI. Un dump json de l'index est également disponible pour les participants.

**Sujets : articles de presse**

Les sujets sont une sélection de 40 articles de presse. 20 provenant d'un grand journal international grand public et 20 de [Tech Xplore](https://techxplore.com/), enrichis de requêtes extraites manuellement du contenu de l'article. Il a été vérifié qu'au moins 5 résumés pertinents peuvent être trouvés pour chaque requête.

**Format de sortie :**
 
Les résultats doivent être fournis dans un format tabulé de type TREC (avec une extension ".csv"). Les colonnes suivantes sont obligatoires (les inclure en première ligne) :

1. run_id : ID de l'exécution commençant par teamid, suivi de "_task1_" et de run_name.
2. manual : Si l'exécution est manuelle {0,1}
3. topic_id : ID du sujet
4. query_id : ID de la requête utilisée pour récupérer le document (si une des requêtes fournies pour le sujet a été utilisée ; 0 sinon)
5. doc_id : ID du document récupéré (à extraire de la sortie json)
6. passage : Texte du passage sélectionné
 
Pour chaque sujet, le nombre maximum de références DBLP distinctes (champ _id json) est de 100 et la longueur totale des passages ne doit pas dépasser 1000 tokens.

*Exemple de sortie*:

| run_id | manual | topic_id | query_id | doc_id | passage |
|:-------|:-------|:---------|:-------|:--------|:-----|
| ST1_task1_1 | 0 | G01 | G01.1 | 1564531496 | A CDA is a mobile user device, similar to a Personal Digital Assistant (PDA). It supports the citizen when dealing with public authorities and proves his rights - if desired, even without revealing his identity. |
| ST1_task1_1 | 0 | G01 | G01.1 | 3000234933 | People are becoming increasingly comfortable using Digital Assistants (DAs) to interact with services or connected objects |
| ST1_task1_1 | 0 | G01 | G01.2 | 1448624402 | As extensive experimental research has shown individuals suffer from diverse biases in decision-making. |

*Vérificateur du format de sortie*

Vous pouvez utiliser ce script python3 pour vérifier le format de sortie. Ce script nécessite Python 3 et la bibliothèque Pandas :
[Télécharger le vérificateur de sortie python](../check_format.py)

**Disclaimer:** En téléchargeant et en utilisant ces données, vous acceptez les conditions d'utilisation. Toute utilisation des données à des fins autres que la recherche universitaire constituerait une violation de l'utilisation prévue de ces données. 

Par conséquent, en téléchargeant et en utilisant ces données, vous donnez les assurances suivantes concernant les données SimpleText :
1. Vous n'utiliserez pas et ne permettrez pas à d'autres d'utiliser les données dans les ensembles de données SimpleText de quelque manière que ce soit, sauf pour les cours et la recherche universitaire.
2. Vous ne divulguerez, ne donnerez ou ne transmettrez à aucun moment (de quelque manière ou forme que ce soit ou à quelque fin que ce soit) les données (ou toute partie de celles-ci) à tout endroit ou personne, y compris, mais sans s'y limiter, la mise à disposition des données sur Internet et la copie des données sur tout système de stockage basé sur le cloud.
3. Vous ne libérerez pas et ne permettrez pas à d'autres de libérer l'ensemble des données ou toute partie de celles-ci à toute personne. 

En cas de violation des conditions d'accès aux données à des fins scientifiques, cet accès peut être retiré à l'entité de recherche et/ou au chercheur. L'entité de recherche peut également être tenue de payer des dommages et intérêts à des tiers ou être invitée à prendre des mesures disciplinaires à l'encontre du chercheur fautif. 


### Évaluation  
Le regroupement de phrases et les métriques automatiques seront utilisés pour évaluer ces résultats. La pertinence du document source sera évaluée ainsi que les éventuels problèmes d'anaphore non résolus.

### Résultat des dépôts :
Les participants doivent placer leurs résultats d'exécution dans le dossier Documents créé pour leur utilisateur et les **soumettre par e-mail** à *contact@simpletext-project.com*.

L'objet de l'e-mail doit être au format **[CLEF TASK 1] TEAM_ID**. 

Les parcours doivent être soumis sous forme de fichier au format TSV. 

Un courriel de confirmation sera envoyé dans les 2 jours suivant la date limite de soumission. 

## Comment citer le document
Si vous étendez ou utilisez ce travail, veuillez citer [l'article](https://doi.org/10.1007/978-3-031-13643-6_28) où il a été présenté :
```
Liana Ermakova, Eric SanJuan, Jaap Kamps, Stéphane Huet, Irina Ovchinnikova, Diana Nurbakova, 
Sílvia Araújo, Radia Hannachi, Elise Mathurin, et Patrice Bellot. 2022. 
Overview of the CLEF 2022 SimpleText Lab: Automatic Simplification of Scientific Texts. 
In Experimental IR Meets Multilinguality, Multimodality, and Interaction: 13e Conférence Internationale 
 de CLEF Association, CLEF 2022, Bologne, Italie, 5-8 Septembre, 2022, Compte-rendus. 
Springer-Verlag, Berlin, Heidelberg, 470–494. https://doi.org/10.1007/978-3-031-13643-6_28
```
[Article](https://doi.org/10.1007/978-3-031-13643-6_28)

[Téléchargez .BIB](../../BibTeX/ermakova_overview_2022.bib)
