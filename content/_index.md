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
