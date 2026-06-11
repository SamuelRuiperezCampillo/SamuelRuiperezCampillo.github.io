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

  - block: selected-talks
    id: talks
    content:
      title: Selected Talks

  - block: markdown
    id: awards
    content:
      title: 'Selected Awards'
      text: |
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl py-2">
          <ol class="space-y-3 list-none p-0">
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2026</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Editor in Chief's Featured Article of the Month</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://doi.org/10.1161/CIRCEP.125.014061" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Circulation: Arrhythmia and Electrophysiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Paul Dudley White International Scholar Award</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">American Heart Association</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation, Multimodal AI &amp; Foundational Models</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">European Society of Cardiology — Digital Health &amp; AI Summit</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation — Physionet Challenge 2025</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://physionetchallenges.org/2025/" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">IEEE Computing in Cardiology</a><span class="ml-1 text-slate-400">· $300</span></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2024</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Clinical Translation Award</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">IEEE Computing in Cardiology<span class="ml-1 text-slate-400">· $1,000</span></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2024</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Honorary Alumnus (one of five)</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Universidad Carlos III de Madrid</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2020</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">"la Caixa" Excellence Fellowship</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://fundacionlacaixa.org/en/scholarships-postgraduate-studies-north-america" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">"la Caixa" Foundation</a> — full master's funding at UC Berkeley<span class="ml-1 text-slate-400">· $100,000</span></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2020</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Rafael del Pino Excellence Fellowship</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://www.frdelpino.es/" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Rafael del Pino Foundation</a> — full master's funding at ETH Zurich<span class="ml-1 text-slate-400">· €48,000</span></div>
              </div>
            </li>
          </ol>
          <p class="mt-5 text-sm"><a href="/awards/" class="text-primary-600 dark:text-primary-400 hover:underline">See the full list →</a></p>
        </div>
    design:
      columns: '1'
---
