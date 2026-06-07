---
title: "ECG-XPLAIM: eXPlainable Locally-adaptive Artificial Intelligence Model for Arrhythmia Detection from Large-Scale Electrocardiogram Data"
authors:
- "P. Pantelidis"
- "me"
- "J. E. Vogt"
- "A. Antonopoulos"
- "I. Gialamas"
- "G. E. Zakynthinos"
- "M. Spartalis"
- "P. Dilaveris"
- "J. Millet"
- "T. G. Papaioannou"
- "E. Oikonomou"
- "G. Siasos"
date: "2025-10-01T00:00:00Z"
publishDate: "2025-10-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Frontiers in Cardiovascular Medicine*, 12"
impact_factor: 2.8
abstract: |-
  **Background.** Timely and accurate detection of arrhythmias from electrocardiograms (ECGs) is crucial for improving patient outcomes. While artificial intelligence (AI)-based ECG classification has shown promising results, limited transparency and interpretability often impede clinical adoption.

  **Methods.** We present ECG-XPLAIM, a novel deep learning model dedicated to ECG classification that employs a one-dimensional inception-style convolutional architecture to capture local waveform features (e.g., waves and intervals) and global rhythm patterns. To enhance interpretability, we integrate Grad-CAM visualization, highlighting key waveform segments that drive the model's predictions. ECG-XPLAIM was trained on the MIMIC-IV dataset and externally validated on PTB-XL for multiple arrhythmias, including atrial fibrillation (AFib), sinus tachycardia (STach), conduction disturbances (RBBB, LBBB, LAFB), long QT (LQT), Wolff-Parkinson-White (WPW) pattern, and paced rhythm detection. We evaluated performance using sensitivity, specificity, and area under the receiver operating characteristic curve (AUROC), and benchmarked against a simplified convolutional neural network, a two-layer gated recurrent unit (GRU), and an external, pre-trained, ResNet-based model.

  **Results.** Internally (MIMIC-IV), ECG-XPLAIM achieved high diagnostic performance (sensitivity, specificity, AUROC > 0.9) across most tasks. External evaluation (PTB-XL) confirmed generalizability, with metric values exceeding 0.95 for AFib and STach. For conduction disturbances, macro-averaged sensitivity reached 0.90, specificity 0.95, and AUROC 0.98. Performance for LQT, WPW, and pacing rhythm detection was 0.691/0.864/0.878, 0.773/0.973/0.895, and 0.96/0.988/0.993 (sensitivity/specificity/AUROC), respectively. Compared to baseline models, ECG-XPLAIM offered superior performance across most tests, and improved sensitivity over the external ResNet-based model, albeit at the cost of specificity. Grad-CAM revealed physiologically relevant ECG segments influencing predictions and highlighted patterns of potential misclassification.

  **Conclusion.** ECG-XPLAIM combines high diagnostic performance with interpretability, addressing a key limitation in AI-driven ECG analysis. The open-source release of ECG-XPLAIM's architecture and pre-trained weights encourages broader adoption, external validation, and further refinement for diverse clinical applications.
tags:
- "Explainable AI"
- "ECG"
- "Arrhythmia"
featured: false
hugoblox:
  ids:
    doi: "10.3389/fcvm.2025.1659971"
links:
  - type: doi
    url: "https://doi.org/10.3389/fcvm.2025.1659971"
---
