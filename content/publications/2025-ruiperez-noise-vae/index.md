---
title: "Reducing Diverse Sources of Noise in Ventricular Electrical Signals Using Variational Autoencoders"
authors:
- "me"
- "A. Ryser"
- "T. M. Sutter"
- "B. Deb"
- "R. Feng"
- "P. Ganesan"
- "K. A. Brennan"
- "A. J. Rogers"
- "M. Z. H. Kolk"
- "F. V. Y. Tjong"
- "S. M. Narayan"
- "J. E. Vogt"
date: "2025-11-01T00:00:00Z"
publishDate: "2025-11-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Expert Systems with Applications*"
impact_factor: 7.5
abstract: |-
  Reducing electrophysiological (EP) signal noise is essential for diagnosis, mapping, and ablation procedures in patients with arrhythmias or conditions such as cardiomyopathies. However, traditional approaches have been suboptimal due to the varied sources of noise. We hypothesized that variational autoencoders (VAEs) can learn key components of 'clean' electrophysiological signals by creating robust internal representations, thereby enabling automatic denoising of diverse noise in clinical recordings. We set out to apply a β-VAE model to a dataset of 5706 intra-ventricular monophasic action potential (MAP) signals, selected because their morphology is verifiable and measurable against a reference, from 42 patients with ischemic cardiomyopathy at risk for sudden death. We designed a noise library, and implemented baselines based on state-of-the-art clinical filtering techniques. The proposed β-VAE model was assessed for various noise types, including challenging non-stationary real EP noise. Comprehensive evaluation using general metrics and clinical action potential duration labels by domain experts revealed that our β-VAE outperformed current state-of-the-art filters in denoising efficacy, with key physiological information encoded in the reconstruction. We performed a sensitivity analysis that confirmed the robustness of the β-VAE model to increasing noise levels. These results demonstrate the ability of our model to denoise various sources, including those of time-varying nature. The application to well-studied MAPs verifies that clinically meaningful features were reconstructed in the EP context. This work enhances traditional signal processing approaches to ensure 'clean' electrical signals, and may have promising applications for diagnosis, tracking therapy and prognostication in patients with EP disorders in real-world clinical environments.
tags:
- "Generative Models"
- "Signal Processing"
- "Cardiac Electrophysiology"
featured: true
hugoblox:
  ids:
    doi: "10.1016/j.eswa.2025.130185"
---
