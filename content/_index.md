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
        about: 'About'
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: false
      name:
        size: sm
      avatar:
        size: medium
        shape: circle
      date_format: '2006'

  - block: markdown
    id: news
    content:
      title: ''
      text: |
        <div class="flex flex-col items-center"><h2 class="bbloxh2 text-3xl font-bold tracking-tight mb-4">News</h2></div>
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl py-2">
          <ol class="space-y-3 list-none p-0">
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">May 2026</span>
              <div class="flex-1 leading-snug">Invited talk at <a href="/events/2026-harvard-medical-school-generative-ai/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Harvard Medical School</a> on generative AI and the physiology of cardiac time series.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">Mar 2026</span>
              <div class="flex-1 leading-snug"><a href="/publications/2026-rodrigo-catheter-mapping/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Our paper on catheter configuration in AF mapping</a> is the Editor in Chief's Featured Article of the Month in <em>Circulation: Arrhythmia and Electrophysiology</em>.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">Nov 2025</span>
              <div class="flex-1 leading-snug">Awarded the <a href="/awards/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Paul Dudley White International Scholar Award</a> by the American Heart Association.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">Sep 2025</span>
              <div class="flex-1 leading-snug"><a href="/events/2025-cinc-swissbeatsnet/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">SwissBeatsNet</a> wins the Best Oral Presentation Award, Physionet Challenge 2025, at IEEE Computing in Cardiology.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">2025</span>
              <div class="flex-1 leading-snug">Best Oral Presentation in Multimodal AI &amp; Foundational Models at the <a href="/events/2025-esc-dcai-contrastive-ecg-mri/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">ESC Digital Health &amp; AI Summit</a>.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-20 shrink-0">Sep 2024</span>
              <div class="flex-1 leading-snug"><a href="/awards/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Clinical Translation Award</a> at IEEE Computing in Cardiology.</div>
            </li>
          </ol>
        </div>
    design:
      columns: '1'

  - block: markdown
    id: research
    content:
      title: ''
      subtitle: ''
      text: |-
        <div class="flex flex-col items-center"><h2 class="bbloxh2 text-3xl font-bold tracking-tight mb-4">Research</h2></div>

        My research applies machine learning and signal processing to
        cardiology, developing generative and representation-learning models
        for cardiac signals such as the ECG and intracardiac electrograms. A
        central focus is cardiac electrophysiology — mapping arrhythmogenic
        substrates and characterizing cardiac activation from multi-electrode
        recordings. As a PhD candidate at the Institute of Machine Learning at
        ETH Zurich, currently a visiting research fellow at MIT and Harvard
        Medical School, I work on translating these methods into clinical
        practice.
    design:
      columns: '1'

  - block: markdown
    id: papers-heading
    content:
      title: ''
      text: |
        <div class="flex flex-col items-center"><h2 class="bbloxh2 text-3xl font-bold tracking-tight mb-4">Selected Publications</h2></div>
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: ''
      text: ''
      count: 0
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation

  - block: markdown
    id: papers-link
    content:
      title: ''
      text: |
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl">
          <p class="mt-2 text-sm"><a href="/publications/" class="text-primary-600 dark:text-primary-400 hover:underline">See all publications →</a></p>
        </div>
    design:
      columns: '1'

  - block: selected-talks
    id: talks
    content:
      title: Selected Talks

  - block: markdown
    id: awards
    content:
      title: ''
      text: |
        <div class="flex flex-col items-center"><h2 class="bbloxh2 text-3xl font-bold tracking-tight mb-4">Selected Awards</h2></div>
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
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation in Multimodal AI &amp; Foundational Models</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">European Society of Cardiology — Digital Health &amp; AI Summit</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation — Physionet Challenge 2025</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://physionetchallenges.org/2025/" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">IEEE Computing in Cardiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Editor in Chief's Featured Article of the Month</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://doi.org/10.1161/CIRCEP.124.012860" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Circulation: Arrhythmia and Electrophysiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-400 dark:text-slate-500 text-sm font-medium tabular-nums w-12 shrink-0">2024</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Clinical Translation Award</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">IEEE Computing in Cardiology</div>
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
          <p class="mt-5 text-sm"><a href="/awards/" class="text-primary-600 dark:text-primary-400 hover:underline">See all awards →</a></p>
        </div>
    design:
      columns: '1'
---
