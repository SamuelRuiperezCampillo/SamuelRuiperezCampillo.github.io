---
title: "Dynamic Prediction of Malignant Ventricular Arrhythmias Using Neural Networks in ICD Patients"
authors:
- "M. Z. H. Kolk"
- "me"
- "L. Alvarez-Florez"
- "B. Deb"
- "E. J. Bekkers"
- "C. P. Allaart"
- "A.-L. C. J. Van Der Lingen"
- "P. Clopton"
- "I. Išgum"
- "A. A. M. Wilde"
- "R. E. Knops"
- "S. M. Narayan"
- "F. V. Y. Tjong"
date: "2024-01-01T00:00:00Z"
publishDate: "2024-01-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Lancet eBioMedicine*"
impact_factor: 10.8
abstract: |-
  **Background.** Risk stratification for ventricular arrhythmias currently relies on static measurements that fail to adequately capture dynamic interactions between arrhythmic substrate and triggers over time. We trained and internally validated a dynamic machine learning (ML) model and neural network that extracted features from longitudinally collected electrocardiograms (ECG), and used these to predict the risk of malignant ventricular arrhythmias.

  **Methods.** A multicentre study in patients implanted with an implantable cardioverter-defibrillator (ICD) between 2007 and 2021 in two academic hospitals was performed. Variational autoencoders (VAEs), which combine neural networks with variational inference principles, and can learn patterns and structure in data without explicit labelling, were trained to encode the mean ECG waveforms from the limb leads into 16 variables. Supervised dynamic ML models using these latent ECG representations and clinical baseline information were trained to predict malignant ventricular arrhythmias treated by the ICD. Model performance was evaluated on a hold-out set, using time-dependent receiver operating characteristic (ROC) and calibration curves.

  **Findings.** 2942 patients (61.7 ± 13.9 years, 25.5% female) were included, with a total of 32,129 ECG recordings during a mean follow-up of 43.9 ± 35.9 months. The mean time-varying area under the ROC curve for the dynamic model was 0.738 ± 0.07, compared to 0.639 ± 0.03 for a static (i.e. baseline-only model). Feature analyses indicated dynamic changes in latent ECG representations, particularly those affecting the T-wave morphology, were of highest importance for model predictions.

  **Interpretation.** Dynamic ML models and neural networks effectively leverage routinely collected longitudinal ECG recordings for personalised and updated predictions of malignant ventricular arrhythmias, outperforming static models.
tags:
- "Ventricular Arrhythmia"
- "Deep Learning"
- "ICD"
featured: true
hugoblox:
  ids:
    doi: "10.1016/j.ebiom.2023.104937"
---
