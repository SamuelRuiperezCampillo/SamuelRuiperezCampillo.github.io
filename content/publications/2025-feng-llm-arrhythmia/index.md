---
title: "Engineering of Generative Artificial Intelligence and Natural Language Processing Models to Accurately Identify Arrhythmia Recurrence"
authors:
- "R. Feng"
- "K. A. Brennan"
- "Z. Azizi"
- "J. Goyal"
- "B. Deb"
- "H. J. Chang"
- "P. Ganesan"
- "P. Clopton"
- "M. Pedron"
- "me"
- "Y. B. Desai"
- "H. De Larochellière"
- "T. Baykaner"
- "M. V. Perez"
- "M. Rodrigo"
- "A. J. Rogers"
- "S. M. Narayan"
author_notes:
- "Equal contribution"
- "Equal contribution"
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
date: "2025-01-01T00:00:00Z"
publishDate: "2025-01-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Circulation: Arrhythmia and Electrophysiology*, 18(1):e013023"
impact_factor: 9.8
abstract: |-
  **Background.** Large language models (LLMs) such as Chat Generative Pre-trained Transformer (ChatGPT) excel at interpreting unstructured data from public sources, yet are limited when responding to queries on private repositories, such as electronic health records (EHRs). We hypothesized that prompt engineering could enhance the accuracy of LLMs for interpreting EHR data without requiring domain knowledge, thus expanding their utility for patients and personalized diagnostics.

  **Methods.** We designed and systematically tested prompt engineering techniques to improve the ability of LLMs to interpret EHRs for nuanced diagnostic questions, referenced to a panel of medical experts. In 490 full-text EHR notes from 125 patients with prior life-threatening heart rhythm disorders, we asked GPT-4-turbo to identify recurrent arrhythmias distinct from prior events and tested 220 563 queries. To provide context, results were compared with rule-based natural language processing and Bidirectional Encoder Representations from Transformer-based language models. Experiments were repeated for 2 additional LLMs.

  **Results.** In an independent hold-out set of 389 notes, GPT-4-turbo had a balanced accuracy of 64.3% ± 4.7% out-of-the-box at baseline. This increased when asking GPT-4-turbo to provide a rationale for its answers, a structured data output, and in-context exemplars, to a balanced accuracy of 91.4% ± 3.8% (P < 0.05). This surpassed the traditional logic-based natural language processing and BERT-based models (P < 0.05). Results were consistent for GPT-3.5-turbo and Jurassic-2 LLMs.

  **Conclusions.** The use of prompt engineering strategies enables LLMs to identify clinical end points from EHRs with an accuracy that surpassed natural language processing and approximated experts, yet without the need for expert knowledge. These approaches could be applied to LLM queries for other domains, to facilitate automated analysis of nuanced data sets with high accuracy by nonexperts.
tags:
- "LLM"
- "Arrhythmia"
- "NLP"
featured: false
hugoblox:
  ids:
    doi: "10.1161/CIRCEP.124.013023"
links:
  - type: doi
    url: "https://doi.org/10.1161/CIRCEP.124.013023"
---
