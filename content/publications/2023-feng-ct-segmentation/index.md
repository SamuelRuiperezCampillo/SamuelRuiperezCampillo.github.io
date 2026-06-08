---
title: "Segmenting Computed Tomograms for Cardiac Ablation Using Machine Learning Leveraged by Domain Knowledge Encoding"
authors:
- "R. Feng"
- "B. Deb"
- "P. Ganesan"
- "F. Tjong"
- "A. Rogers"
- "me"
- "S. Somani"
- "M. Rodrigo"
- "P. Clopton"
- "J. Zou"
- "M. Zaharia"
- "S. Narayan"
date: "2023-10-01T00:00:00Z"
publishDate: "2023-10-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Frontiers in Cardiovascular Medicine*"
impact_factor: 2.8
abstract: |-
  **Background.** Segmentation of computed tomography (CT) is important for many clinical procedures including personalized cardiac ablation for the management of cardiac arrhythmias. While segmentation can be automated by machine learning (ML), it is limited by the need for large, labeled training data that may be difficult to obtain. We set out to combine ML of cardiac CT with domain knowledge, which reduces the need for large training datasets by encoding cardiac geometry, which we then tested in independent datasets and in a prospective study of atrial fibrillation (AF) ablation.

  **Methods.** We mathematically represented atrial anatomy with simple geometric shapes and derived a model to parse cardiac structures in a small set of N = 6 digital hearts. The model, termed "virtual dissection," was used to train ML to segment cardiac CT in N = 20 patients, then tested in independent datasets and in a prospective study.

  **Results.** In independent test cohorts (N = 160) from 2 Institutions with different CT scanners, atrial structures were accurately segmented with Dice scores of 96.7% in internal (IQR: 95.3%–97.7%) and 93.5% in external (IQR: 91.9%–94.7%) test data, with good agreement with experts (r = 0.99; p < 0.0001). In a prospective study of 42 patients at ablation, this approach reduced segmentation time by 85% (2.3 ± 0.8 vs. 15.0 ± 6.9 min, p < 0.0001), yet provided similar Dice scores to experts (93.9% (IQR: 93.0%–94.6%) vs. 94.4% (IQR: 92.8%–95.7%), p = NS).

  **Conclusions.** Encoding cardiac geometry using mathematical models greatly accelerated training of ML to segment CT, reducing the need for large training sets while retaining accuracy in independent test data.
tags:
- "Cardiac Imaging"
- "Segmentation"
featured: false
hugoblox:
  ids:
    doi: "10.3389/fcvm.2023.1189293"
---
