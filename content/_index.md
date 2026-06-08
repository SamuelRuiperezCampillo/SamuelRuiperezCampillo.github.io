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
        about: 'Professional Summary — 🚧 Website in Progress!'
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: sm
      avatar:
        size: medium
        shape: circle
      date_format: '2006'

  - block: markdown
    content:
      title: '🔬 Research'
      subtitle: ''
      text: |-
        My research applies machine learning and signal processing to
        cardiology and biomedical signals. I work on generative and
        representation-learning models for cardiac time series, mapping
        arrhythmogenic substrates.
    design:
      columns: '1'

  # Featured Publications — temporarily disabled. Uncomment to restore.
  # - block: collection
  #   id: papers
  #   content:
  #     title: Featured Publications
  #     count: 0
  #     filters:
  #       folders:
  #         - publications
  #       featured_only: true
  #   design:
  #     view: article-grid
  #     columns: 2

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
      title: Highlighted Talks
      count: 6
      filters:
        folders:
          - events
      order: desc
    design:
      view: compact

  - block: markdown
    id: awards
    content:
      title: 'Selected Awards'
      text: |
        - **Paul Dudley White International Scholar Award** — American Heart Association *(2025)*
        - **Editor in Chief's Featured Article of the Month** — *Circulation: Arrhythmia and Electrophysiology* *(2026, 2025)*
        - **Best Oral Presentation on Multimodal AI & Foundational Models** — European Society of Cardiology, DCAI Summit *(2025)*
        - **Best Oral Presentation — Physionet Challenge 2025** — IEEE Computing in Cardiology *(2025)*
        - **Clinical Translation Award** — IEEE Computing in Cardiology *(2024)*
        - **Honorary Alumnus (one of five)** — Universidad Carlos III de Madrid *(2024)*
        - **"la Caixa" Excellence Fellowship** — full master's funding at UC Berkeley *(2020)*
        - **Rafael del Pino Excellence Fellowship** — full master's funding at ETH Zurich *(2020)*

        [See the full list →](/awards/)
    design:
      columns: '1'
---
