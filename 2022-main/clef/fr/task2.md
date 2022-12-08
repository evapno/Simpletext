# Tâches SimpleText@CLEF-2022

[Accueil](./) | [Appel à contributions](./CFP) | [Dates importantes](./dates) | [Tâches](./tasks)  | [Outils](./tools) 
[Programme](./program) | [Publications](./publications) | [Organisateurs](./organisers) | [Contact](./contact) | [CLEF-2023](https://simpletext-project.com/2023/clef)


---

## Directives pour les tâches SimpleText

Nous vous invitons à soumettre aussi bien des parcours automatiques que manuels ! Les interventions manuelles doivent être signalées.

---

Accès | Tâche partagée 1 | Tâche partagée 2 | Tâche partagée 3| Tâche non partagée 4

<br>

## Tâche 2 : Qu'est-ce qui n'est pas clair ? Étant donné un passage et une requête, classez les termes/concepts qui doivent être expliqués pour comprendre ce passage (définitions, contexte, applications,...).

Le but de cette tâche est de décider quels mots (jusqu'à 5) nécessitent une explication et une contextualisation pour aider un lecteur à comprendre un texte scientifique complexe - par exemple, en ce qui concerne une requête, les termes qui doivent être contextualisés (avec une définition, un exemple et/ou un cas d'utilisation). Pour chaque passage, les participants doivent fournir une liste classée des termes difficiles avec les notes correspondantes sur l'échelle 1-3 (3 pour les termes les plus difficiles, tandis que le sens des termes notés 1 peut être déduit ou deviné) et sur l'échelle 1-5 (5 pour les termes les plus difficiles). Les passages (phrases) sont considérés comme indépendants, c'est-à-dire que la répétition de termes difficiles est autorisée. Le regroupement des termes et des métriques automatiques (précision de la classification binaire des termes, NDCG pour le classement des termes, statistiques de kappa...) seront utilisés pour évaluer ces résultats.

**Format d'entrée :**
Les données de formation et de test sont fournies dans les formats JSON et CSV avec les champs suivants :
* `snt_id`: un identifiant unique de passage (phrase)
* `source_snt`: texte du passage
* `doc_id`: un identifiant unique du document source
* `query_id`: un identifiant de requête
* `query_text`: mots difficiles à extraire des phrases par rapport à cette requête

*Exemple d'entrées :*

```
{"snt_id":"G06.2_2548923997_3",
"source_snt":"These communication systems render self-driving vehicles vulnerable to many types of malicious attacks, such as Sybil attacks, Denial of Service (DoS), black hole, grey hole and wormhole attacks.",
"doc_id":2548923997,
"query_id":"G06.2",
"query_text":"self driving"}
```

**Format de sortie :** 

Liste des termes à contextualiser dans un **format JSON** ou un fichier tabulé **TSV** (pour les runs manuels) avec les champs suivants :
* `run_id`: un ID d'exécution commençant par **team_id_task_id_**
* `manual`: Si l'exécution est manuelle {0,1}
* `snt_id`: un identifiant unique de passage (phrase) du fichier d'entrée 
* `term`: mot ou autre phrase à expliquer
* `term_rank_snt`: rang de difficulté du terme dans la phrase donnée
* `score_5`: score de difficulté du mot sur une échelle de 1 à 5 (5 les mots les plus difficiles)
* `score_3`: score de difficulté du mot sur uen échelle de 1 à 3 (3 les mots les plus difficiles)

*Exemple de sortie*:

```{json}
{"run_id":"NP_task_2_run1",
"manual":1,
"snt_id":"G06.2_2548923997_3",
"term":"black hole attack",
"term_rank_snt":1,
"score_5":5,
"score_3":3},

{"run_id":"NP_task_2_run1",
"manual":1,
"snt_id":"G06.2_2548923997_3",
"term":"grey hole attack",
"term_rank_snt":2,
"score_5":5,
"score_3":3},

{"run_id":"NP_task_2_run1",
"manual":1,
"snt_id":"G06.2_2548923997_3",
"term":"Sybil attack",
"term_rank_snt":3,
"score_5":5,
"score_3":3},

{"run_id":"NP_task_2_run1",
"manual":1,
"snt_id":"G06.2_2548923997_3",
"term":"wormhole attack",
"term_rank_snt":4,
"score_5":5,"score_3":3},

{"run_id":"NP_task_2_run1",
"manual":1,
"snt_id":"G06.2_2548923997_3",
"term":"Denial of service attack",
"term_rank_snt":5,
"score_5":4,
"score_3":3}
```

*Vérificateur du format de sortie*

Vous pouvez utiliser ce script python3 pour vérifier le format de sortie. Le script nécessite Python 3 et la bibliothèque Pandas : [Télécharger python output checker](../check_format.py)

**Avis de non-responsabilité :** En téléchargeant et en utilisant ces données, vous acceptez les conditions d'utilisation. Toute utilisation des données à des fins autres que la recherche universitaire constituerait une violation de l'utilisation prévue de ces données. 

Par conséquent, en téléchargeant et en utilisant ces données, vous donnez les assurances suivantes concernant les données SimpleText :
1. Vous n'utiliserez ni ne permettrez à d'autres d'utiliser les données des ensembles de données SimpleText de quelque manière que ce soit, sauf pour les cours et la recherche universitaire
2. À aucun moment vous ne divulguerez, ne donnerez ou ne transmettrez (de quelque manière, sous quelque forme ou à quelque fin que ce soit) les données (ou toute partie de celles-ci) à quelque endroit ou personne que ce soit, y compris, mais sans s'y limiter, en rendant les données disponibles sur Internet et en copiant les données sur tout système de stockage en nuage
3. Vous ne divulguerez pas et ne permettrez pas à d'autres de divulguer l'ensemble de données ou toute partie de celui-ci à quiconque. 

En cas de violation des conditions d'accès aux données à des fins scientifiques, cet accès peut être retiré à l'entité de recherche et/ou au chercheur. L'entité de recherche peut également être tenue de payer des dommages et intérêts à des tiers ou être invitée à prendre des mesures disciplinaires à l'encontre du chercheur fautif. 
 
### Évaluation
Le regroupement des termes et des métriques automatiques (précision de la classification binaire des termes, NDCG pour le classement des termes, statistiques de kappa...) seront utilisés pour évaluer ces résultats.

### Soumission des résultats :
Les participants doivent placer leurs résultats d'exécution dans le dossier Documents créé pour leur utilisateur et les **soumettre par e-mail** à *contact@simpletext-project.com*.

L'objet de l'e-mail doit être au format **[CLEF TASK 2] TEAM\_ID**. 

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
