---
title: "Multimodal Patient-Specific Identification of Atrial Flutter Circuits from ECG Time Series Using Explainable Machine Learning"
authors:
- "me"
- "D. Hernando"
- "E. Ramírez"
- "S. Castrejón"
- "C. Zapata"
- "C. Rodríguez Carneiro"
- "J. E. Vogt"
- "J. L. Merino"
- "F. Castells"
- "J. Millet"
date: "2026-05-19T00:00:00Z"
publishDate: "2026-05-19T00:00:00Z"
publication_types: ["article-journal"]
publication: "*IEEE Journal of Translational Engineering in Health and Medicine*"
impact_factor: 5.9
abstract: |-
  **Objective.** Accurate pre-procedural identification of atrial flutter (AFL) mechanisms can streamline mapping and indirectly inform ablation strategy, yet surface-electrocardiogram (ECG) criteria remain unreliable and circuit definition is typically confirmed invasively.

  **Methods and Procedures.** We analyzed 97 consecutive patients undergoing electrophysiological (EP) study with simultaneous 12-lead ECG and EP-verified AFL subtype; adenosine-induced atrioventricular AV block enabled extraction of clean atrial segments. We reconstructed atrial vectorcardiograms (VCGs) and engineered interpretable descriptors of loop morphology and kinematics, including archetype cosine correlation, geometric complexity, and velocity-based slow-occupancy indices, then fused these with clinical variables in an explainable tree-ensemble model evaluated with nested cross-validation.

  **Results.** VCG loops exhibited subtype-specific archetypes (within-class correlation: 0.832±0.129 CCCW, 0.874±0.154 CCW, 0.647±0.127 PMCCW, 0.667±0.159 PMCW; C: common; PM: perimitral; CW: clockwise; CCW: counter-CW). On the test set, the multimodal Random-Forest improved discrimination over VCG-only and clinical-only baselines, achieving AUROC of 0.870 (CCCW), 0.900 (CCW), 0.840 (PMCCW), and 0.790 (PMCW), with high sensitivity for common AFL (0.833 and 0.929) and very high specificity for PMCW (0.988).

  **Conclusion.** This interpretable framework provides a practical route to non-invasive, mechanism-oriented AFL stratification to support targeted mapping and more efficient ablation planning. Future work will focus on multicenter prospective validation and robust atrial-signal extraction without adenosine to broaden routine applicability.
tags:
- "Atrial Flutter"
- "Explainable AI"
- "ECG"
- "Signal Processing"
featured: false
hugoblox:
  ids:
    doi: "10.1109/JTEHM.2026.3694616"
---
