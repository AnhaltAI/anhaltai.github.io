---
title: 'Unsupervised Natural Language Processing for Knowledge Extraction from Domain-specific Textual Resources'
authors:
  - Christian Hänig
date: '2013-04-25T00:00:00Z'
#doi: 'https://doi.org/10.1007/978-3-319-12655-5_6'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-11-09T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['7']

# Publication name and optional abbreviated publication name.
publication: '(Dissertation)'
publication_short: '(Dissertation)'

abstract: 'This thesis aims to develop a Relation Extraction algorithm to extract knowledge out of automotive data. While most approaches to Relation Extraction are only evaluated on newspaper data dealing with general relations from the business world their applicability to other data sets is not well studied. Part I of this thesis deals with theoretical foundations of Information Extraction algorithms. Text mining cannot be seen as the simple application of data mining methods to textual data. Instead, sophisticated methods have to be employed to accurately extract knowledge from text which then can be mined using statistical methods from the field of data mining. Information Extraction itself can be divided into two subtasks: Entity Detection and Relation Extraction. The detection of entities is very domain-dependent due to terminology, abbreviations and general language use within the given domain. Thus, this task has to be solved for each domain employing thesauri or another type of lexicon. Supervised approaches to Named Entity Recognition will not achieve reasonable results unless they have been trained for the given type of data. The task of Relation Extraction can be basically approached by pattern-based and kernel-based algorithms. The latter achieve state-of-the-art results on newspaper data and point out the importance of linguistic features. In order to analyze relations contained in textual data, syntactic features like part-of-speech tags and syntactic parses are essential. Chapter 4 presents machine learning approaches and linguistic foundations being essential for syntactic annotation of textual data and Relation Extraction. Chapter 6 analyzes the performance of state-of-the-art algorithms of POS tagging, syntactic parsing and Relation Extraction on automotive data. The findings are: supervised methods trained on newspaper corpora do not achieve accurate results when being applied on automotive data. This is grounded in various reasons. Besides low-quality text, the nature of automotive relations states the main challenge. Automotive relation types of interest (e. g. component – symptom) are rather arbitrary compared to well-studied relation types like is-a or is-head-of. In order to achieve acceptable results, algorithms have to be trained directly on this kind of data. As the manual annotation of data for each language and data type is too costly and inflexible, unsupervised methods are the ones to rely on. Part II deals with the development of dedicated algorithms for all three essential tasks. Unsupervised POS tagging (Chapter 7) is a well-studied task and algorithms achieving accurate tagging exist. All of them do not disambiguate high frequency words, only out-of-lexicon words are disambiguated. Most high frequency words bear syntactic information and thus, it is very important to differentiate between their different functions. Especially domain languages contain ambiguous and high frequent words bearing semantic information (e. g. pump). In order to improve POS tagging, an algorithm for disambiguation is developed and used to enhance an existing state-of-the-art tagger. This approach is based on context clustering which is used to detect a word type’s different syntactic functions. Evaluation shows that tagging accuracy is raised significantly. An approach to unsupervised syntactic parsing (Chapter 8) is developed in order to suffice the requirements of Relation Extraction. These requirements include high precision results on nominal and prepositional phrases as they contain the entities being relevant for Relation Extraction. Furthermore, accurate shallow parsing is more desirable than deep binary parsing as it facilitates Relation Extraction more than deep parsing. Endocentric and exocentric constructions can be distinguished and improve proper phrase labeling. unsuParse is based on preferred positions of word types within phrases to detect phrase candidates. Iterating the detection of simple phrases successively induces deeper structures. The proposed algorithm fulfills all demanded criteria and achieves competitive results on standard evaluation setups. Syntactic Relation Extraction (Chapter 9) is an approach exploiting syntactic statistics and text characteristics to extract relations between previously annotated entities. The approach is based on entity distributions given in a corpus and thus, provides a possibility to extend text mining processes to new data in an unsupervised manner. Evaluation on two different languages and two different text types of the automotive domain shows that it achieves accurate results on repair order data. Results are less accurate on internet data, but the task of sentiment analysis and extraction of the opinion target can be mastered. Thus, the incorporation of internet data is possible and important as it provides useful insight into the customer\''s thoughts. To conclude, this thesis presents a complete unsupervised workflow for Relation Extraction – except for the highly domain-dependent Entity Detection task – improving performance of each of the involved subtasks compared to state-of-the-art approaches. Furthermore, this work applies Natural Language Processing methods and Relation Extraction approaches to real world data unveiling challenges that do not occur in high quality newspaper corpora.'

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - paper-tag
featured: true

links:
  - name: URL
    url: https://nbn-resolving.org/urn:nbn:de:bsz:15-qucosa-112706
#url_pdf: http://www.lrec-conf.org/proceedings/lrec2014/pdf/258_Paper.pdf

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#  - internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides:
---

