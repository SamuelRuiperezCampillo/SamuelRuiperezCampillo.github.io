---
title: "RadVLM: A Multitask Conversational Vision-Language Model for Radiology"
authors:
- "N. Deperrois"
- "H. Matsuo"
- "me"
- "M. Vandenhirtz"
- "S. Laguna"
- "A. Ryser"
- "K. Fujimoto"
- "M. Nishio"
- "T. M. Sutter"
- "J. E. Vogt"
- "J. Kluckert"
- "T. Frauenfelder"
- "C. Blüthgen"
- "F. Nooralahzadeh"
- "M. Krauthammer"
date: "2026-08-25T00:00:00Z"
publishDate: "2026-08-25T00:00:00Z"
publication_types: ["article-journal"]
publication: "*Scientific Reports*"
impact_factor: 3.9
abstract: |-
  The widespread use of chest X-rays (CXRs), coupled with a shortage of radiologists, has driven growing interest in automated CXR analysis and AI-assisted reporting. While existing vision-language models (VLMs) show promise in specific tasks such as report generation or abnormality detection, they often lack support for interactive diagnostic capabilities. In this work we present RadVLM, a compact, multitask conversational VLM for CXR interpretation. We construct and standardize a large-scale CXR instruction dataset comprising over 1 million image-instruction pairs from multiple public datasets. The dataset integrates single-turn tasks—including report generation, abnormality classification, and visual grounding—with synthetic multi-turn conversations generated from structured CXR attributes. After fine-tuning RadVLM on this instruction dataset, we evaluate it across different tasks together with re-implemented baseline VLMs. Among the evaluated baselines, RadVLM achieves the strongest performance in conversational capabilities and visual grounding, while remaining competitive in other radiology tasks. Ablations comparing task-specific fine-tuning with full multitask fine-tuning are consistent with a benefit of joint training, particularly for lower-resource grounding and conversational settings. Together, these findings support RadVLM as a research prototype for structured CXR interpretation and conversational capabilities to support more effective and accessible diagnostic workflows.
tags:
- "Vision-Language Models"
- "Radiology"
- "Multimodal Learning"
featured: false
hugoblox:
  ids:
    doi: "10.1038/s41598-026-66181-1"
    arxiv: "2502.03333"
---
