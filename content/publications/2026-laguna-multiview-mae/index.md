---
title: "Structure is Supervision: Multiview Masked Autoencoders for Radiology"
authors:
- "S. Laguna"
- "A. Agostini"
- "A. Ryser"
- "me"
- "I. Cannistraci"
- "M. Vandenhirtz"
- "S. Mandt"
- "N. Deperrois"
- "F. Nooralahzadeh"
- "M. Krauthammer"
- "T. M. Sutter"
- "J. E. Vogt"
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
date: "2026-04-01T00:00:00Z"
publishDate: "2026-04-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Transactions on Machine Learning Research*"
abstract: |-
  Building robust medical machine learning systems requires pretraining strategies that exploit the intrinsic structure present in clinical data. We introduce Multiview Masked Autoencoder (MVMAE), a self-supervised framework that leverages the natural multi-view organization of radiology studies to learn view-invariant and disease-relevant representations. MVMAE combines masked image reconstruction with cross-view alignment, transforming clinical redundancy across projections into a powerful self-supervisory signal. We further extend this approach with MVMAE-V2T, which incorporates radiology reports as an auxiliary text-based learning signal to enhance semantic grounding while preserving fully vision-based inference. Evaluated on a downstream disease classification task on three large-scale public datasets, MIMIC-CXR, CheXpert, and PadChest, MVMAE consistently outperforms supervised and vision-language baselines. Furthermore, MVMAE-V2T provides additional gains, particularly in low-label regimes where structured textual supervision is most beneficial. Together, these results establish the importance of structural and textual supervision as complementary paths toward scalable, clinically grounded medical foundation models.
tags:
- "Multimodal Learning"
- "Representation Learning"
- "Medical Imaging"
featured: false
links:
- name: "OpenReview (TMLR)"
  url: "https://openreview.net/forum?id=wryiHLzieX"
hugoblox:
  ids:
    doi: "10.48550/arXiv.2511.22294"
    arxiv: "2511.22294"
---
