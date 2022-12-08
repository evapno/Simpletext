# Tâches SimpleText@CLEF-2022


[Accueil](./) | [Appel à contributions](./CFP) | [Dates importantes](./dates) | [Tâches](./tasks)  | [Outils](./tools) 
[Programme](./program) | [Publications](./publications) | [Organisateurs](./organisers) | [Contact](./contact) | [CLEF-2023](https://simpletext-project.com/2023/clef)


---

## Directives pour les tâches SimpleText

Nous vous invitons à soumettre aussi bien des interventions automatiques que manuelles ! Les interventions manuelles doivent être signalées.

---

<button>[Accéder](./tasks)</button> | <button>[Tâche partagée 1](./task1)</button> | <button>[Tâche partagée 2](./task2)</button> | <button>[Tâche partagée 3](./task3)</button>| <button>[Tâche non-partagée 4](./task4)</button>

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

*Output format checker*

You can use this python3 script to check the output format. The script requires Python 3 and the Pandas library:
[Download python output checker](../check_format.py)

**Disclaimer:** By downloading and using these data, you agree to the terms of use. Any use of the data for any purpose other than academic research, would be in violation of the intended use of these data. 

Therefore, by downloading and using these data you give the following assurances with respect to the SimpleText data:
1. You will not use nor permit others to use the data in the SimpleText datasets in any way except for classes and academic research.
2. You will not at any time disclose, give, or transmit (in any manner or form or for any purpose) the data (or any portion thereof) to any location or person, including but not limiting to making the data available on the Internet, and copying the data onto any cloud-based storage system.
3. You will not release nor permit others to release the dataset or any part of it to any person. 

In case of violation of the conditions for access to the data for scientific purposes, this access may be withdrawn from the research entity and/or from the researcher. The research entity may also be liable to pay compensation for damages for third parties or asked to take disciplinary action against the offending researcher. 


### Evaluation  
Sentence pooling and automatic metrics will be used to evaluate these results. The relevance of the source document will be evaluated as well as potential unresolved anaphora issues.

### Result submission:
Participants should put their run results into the folder Documents created for their user and **submit them by email** to *contact@simpletext-project.com*.

The email subject has to be in the format **\[CLEF TASK 1] TEAM_ID**. 

Runs should be submitted as a file in a TSV format. 

A confirmation email will be sent within 2 days after the submission deadline. 

## How to Cite
If you extend or use this work, please cite the [paper](https://doi.org/10.1007/978-3-031-13643-6_28) where it was introduced:
```
Liana Ermakova, Eric SanJuan, Jaap Kamps, Stéphane Huet, Irina Ovchinnikova, Diana Nurbakova, 
Sílvia Araújo, Radia Hannachi, Elise Mathurin, and Patrice Bellot. 2022. 
Overview of the CLEF 2022 SimpleText Lab: Automatic Simplification of Scientific Texts. 
In Experimental IR Meets Multilinguality, Multimodality, and Interaction: 13th International 
Conference of the CLEF Association, CLEF 2022, Bologna, Italy, September 5–8, 2022, Proceedings. 
Springer-Verlag, Berlin, Heidelberg, 470–494. https://doi.org/10.1007/978-3-031-13643-6_28
```
[Paper](https://doi.org/10.1007/978-3-031-13643-6_28)

[Dowload .BIB](../../BibTeX/ermakova_overview_2022.bib)
