---
title: "Novel Domain Knowledge-Encoding Algorithm Enables Label-Efficient Deep Learning for Cardiac CT Segmentation to Guide Atrial Fibrillation Treatment in a Pilot Dataset"
authors:
- "P. Ganesan"
- "R. Feng"
- "B. Deb"
- "F. V. Y. Tjong"
- "A. J. Rogers"
- "me"
- "S. Somani"
- "P. Clopton"
- "T. Baykaner"
- "M. Rodrigo"
- "J. Zou"
- "F. Haddad"
- "M. Zaharia"
- "S. M. Narayan"
date: "2024-07-01T00:00:00Z"
publishDate: "2024-07-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Diagnostics*"
abstract: |-
  **Background.** Segmenting computed tomography (CT) is crucial in various clinical applications, such as tailoring personalized cardiac ablation for managing cardiac arrhythmias. Automating segmentation through machine learning (ML) is hindered by the necessity for large, labeled training data, which can be challenging to obtain. This article proposes a novel approach for automated, robust labeling using domain knowledge to achieve high-performance segmentation by ML from a small training set. The approach, the domain knowledge-encoding (DOKEN) algorithm, reduces the reliance on large training datasets by encoding cardiac geometry while automatically labeling the training set. The method was validated in a hold-out dataset of CT results from an atrial fibrillation (AF) ablation study.

  **Methods.** The DOKEN algorithm parses left atrial (LA) structures, extracts "anatomical knowledge" by leveraging digital LA models (available publicly), and then applies this knowledge to achieve high ML segmentation performance with a small number of training samples. The DOKEN-labeled training set was used to train a nnU-Net deep neural network (DNN) model for segmenting cardiac CT in N = 20 patients. Subsequently, the method was tested in a hold-out set with N = 100 patients (five times larger than training set) who underwent AF ablation.

  **Results.** The DOKEN algorithm integrated with the nn-Unet model achieved high segmentation performance with few training samples, with a training to test ratio of 1:5. The Dice score of the DOKEN-enhanced model was 96.7% (IQR: 95.3% to 97.7%), with a median error in surface distance of boundaries of 1.51 mm (IQR: 0.72 to 3.12) and a mean centroid–boundary distance of 1.16 mm (95% CI: −4.57 to 6.89), similar to expert results (r = 0.99; p < 0.001). In digital hearts, the novel DOKEN approach segmented the LA structures with a mean difference for the centroid–boundary distances of −0.27 mm (95% CI: −3.87 to 3.33; r = 0.99; p < 0.0001).

  **Conclusions.** The proposed novel domain knowledge-encoding algorithm was able to perform the segmentation of six substructures of the LA, reducing the need for large training data sets. The combination of domain knowledge encoding and a machine learning approach could reduce the dependence of ML on large training datasets and could potentially be applied to AF ablation procedures and extended in the future to other imaging, 3D printing, and data science applications.
tags:
- "Cardiac Imaging"
- "Deep Learning"
- "Segmentation"
featured: false
hugoblox:
  ids:
    doi: "10.3390/diagnostics14141538"
links:
  - type: doi
    url: "https://doi.org/10.3390/diagnostics14141538"
---
