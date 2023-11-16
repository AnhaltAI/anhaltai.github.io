---
title: 'NLP-based Decision Support System for Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank'
authors:
  - Christian Hänig
  - Schlösser, Markus
  - Serhii Hamotskyi
  - Zambaku, Gent
  - Blankenburg, Janek
date: '2013-07-01T00:00:00Z'
doi: '10.48550/arXiv.2302.04562'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-11-09T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: 'In *AAAI23 B8: AI for Financial Institutions*'
publication_short: In *AAAI23*

abstract: As part of its digitization initiative, the German Central Bank (Deutsche Bundesbank) wants to examine the extent to which natural Language Processing (NLP) can be used to make independent decisions upon the eligibility criteria of securities prospectuses. Every month, the Directorate General Markets at the German Central Bank receives hundreds of scanned prospectuses in PDF format, which must be manually processed to decide upon their eligibility. We found that this tedious and time-consuming process can be (semi-)automated by employing modern NLP model architectures, which learn the linguistic feature representation in text to identify the present eligible and ineligible criteria. The proposed Decision Support System provides decisions of document-level eligibility criteria accompanied by human-understandable explanations of the decisions. The aim of this project is to model the described use case and to evaluate the extent to which current research results from the field of NLP can be applied to this problem. After creating a heterogeneous domain-specific dataset containing annotations of eligible and non-eligible mentions of relevant criteria, we were able to successfully build, train and deploy a semi-automatic decider model. This model is based on transformer-based language models and decision trees, which integrate the established rule-based parts of the decision processes. Results suggest that it is possible to efficiently model the problem and automate decision making to more than 90% for many of the considered eligibility criteria.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - paper-tag
featured: true

links:
  - name: Arxiv
    url: https://arxiv.org/abs/2302.04562
url_pdf: https://arxiv.org/pdf/2302.04562.pdf

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

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

Supplementary notes can be added here, including [code and math](https://wowchemy.com/docs/content/writing-markdown-latex/).
