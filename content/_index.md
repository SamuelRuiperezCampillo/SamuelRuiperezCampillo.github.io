---
title: ''
summary: ''
date: 2026-05-13
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: markdown
    content:
      title: '🔬 Research'
      subtitle: ''
      text: |-
        My research applies machine learning and signal processing to
        cardiology and biomedical signals. I work on generative and
        representation-learning models for intracardiac and surface
        electrocardiographic signals, with the goal of denoising clinical
        recordings, mapping arrhythmogenic substrates, and supporting
        treatment decisions in atrial and ventricular arrhythmias. I also
        work on multimodal models combining ECG, cardiac imaging, and
        clinical text.

        Recent and ongoing projects include diffusion- and VAE-based
        denoising of intracardiac time series, equivariant representation
        learning for cardiac MRI, contrastive multimodal models that enrich
        ECG with cardiac MRI, large language and foundation models for
        arrhythmia phenotyping, and AI-guided catheter mapping for atrial
        fibrillation ablation.

        I'm always happy to discuss collaborations on ML for medical time
        series, cardiac electrophysiology, and multimodal foundation models
        for healthcare.
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation

  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - events
    design:
      view: card
---
