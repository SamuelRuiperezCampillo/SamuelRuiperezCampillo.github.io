---
title: ''
summary: ''
date: 2026-05-13
type: landing

sections:
  - block: resume-biography-3
    id: hero
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: 'About — 🚧 Website in Progress'
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: false
      name:
        size: sm
      avatar:
        size: small
        shape: circle
      date_format: '2006'

  - block: markdown
    id: news
    content:
      title: ''
      text: |
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl"><h2 class="bbloxh2 hb-section-title text-3xl font-bold tracking-tight">News</h2></div>
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl py-2">
          <ol class="space-y-3 list-none p-0">
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">May 2026</span>
              <div class="flex-1 leading-snug">Invited talk at <a href="/events/2026-harvard-medical-school-generative-ai/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Harvard Medical School</a> on generative AI and the physiology of cardiac time series.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Mar 2026</span>
              <div class="flex-1 leading-snug"><a href="/publications/2026-rodrigo-catheter-mapping/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Our paper on catheter configuration in AF mapping</a> is the Editor-in-Chief's Featured Article of the Month in <em>Circulation: Arrhythmia and Electrophysiology</em>.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Nov 2025</span>
              <div class="flex-1 leading-snug">Awarded the <a href="/awards/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Paul Dudley White International Scholar Award</a> by the American Heart Association.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Nov 2025</span>
              <div class="flex-1 leading-snug">Best Oral Presentation in Multimodal AI &amp; Foundational Models at the <a href="/events/2025-esc-dcai-contrastive-ecg-mri/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">ESC Digital Health &amp; AI Summit</a>.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Sep 2025</span>
              <div class="flex-1 leading-snug"><a href="/events/2025-cinc-swissbeatsnet/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">SwissBeatsNet</a> wins the Best Oral Presentation Award, Physionet Challenge 2025, at IEEE Computing in Cardiology.</div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Sep 2024</span>
              <div class="flex-1 leading-snug"><a href="/awards/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">Clinical Translation Award</a> at IEEE Computing in Cardiology.</div>
            </li>
          </ol>
        </div>
    design:
      columns: '1'

  - block: markdown
    id: research-heading
    content:
      title: ''
      text: |
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl"><h2 class="bbloxh2 hb-section-title text-3xl font-bold tracking-tight">Research</h2></div>
    design:
      columns: '1'

  - block: ecg-divider
    id: ecg

  - block: markdown
    id: research
    content:
      title: ''
      subtitle: ''
      text: |-
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl py-2">
          <p class="mt-2 leading-relaxed">As a PhD candidate at the Institute of Machine Learning at
          ETH Zurich, I apply machine learning and signal processing to cardiology.</p>
          <div class="hb-research-grid">
            <div class="hb-research-card">
              <svg class="hb-research-icon" width="30" height="30" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M2 18h5.5l2.4-5 3.4 11 3.6-16 2.6 10h2.3l1.6-3.2 1.6 3.2H30"/>
              </svg>
              <h3>Generative &amp; representation learning</h3>
              <p>Generative and representation-learning models for cardiac signals such as the ECG and intracardiac electrograms.</p>
            </div>
            <div class="hb-research-card">
              <svg class="hb-research-icon" width="30" height="30" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M16 27.2C9 21.9 5 17.5 5 12.8 5 9.4 7.5 6.8 10.7 6.8c2.1 0 4.1 1.2 5.3 3.2 1.2-2 3.2-3.2 5.3-3.2C24.5 6.8 27 9.4 27 12.8c0 4.7-4 9.1-11 14.4Z"/>
                <path d="M16 11.5A3 3 0 0 1 13 14.5"/>
                <path d="M18.5 11.5A5.5 5.5 0 0 1 13 17"/>
                <circle cx="13" cy="11.5" r="0.6"/>
              </svg>
              <h3>Electrophysiology mapping</h3>
              <p>Mapping arrhythmogenic substrates and characterizing cardiac activation from multi-electrode recordings.</p>
            </div>
            <div class="hb-research-card">
              <svg class="hb-research-icon" width="30" height="30" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M2 17h3l2.2-4.6 3 8.6 2.2-5.4h6.2"/>
                <path d="M16.6 14.9 18.7 17l-2.1 2.1"/>
                <circle cx="25.9" cy="17" r="4.4"/>
                <path d="M25.9 15v4M23.9 17h4"/>
              </svg>
              <h3>Clinical translation</h3>
              <p>Translating these methods into clinical practice, currently as a visiting research fellow at MIT and Harvard Medical School.</p>
            </div>
          </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    id: papers-heading
    content:
      title: ''
      text: |
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl"><h2 class="bbloxh2 hb-section-title text-3xl font-bold tracking-tight">Selected Publications</h2></div>
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
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl"><h2 class="bbloxh2 hb-section-title text-3xl font-bold tracking-tight">Selected Awards</h2></div>
        <div class="container px-4 sm:px-6 mx-auto max-w-3xl py-2">
          <ol class="space-y-3 list-none p-0">
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2026</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Editor-in-Chief's Featured Article of the Month</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://doi.org/10.1161/CIRCEP.125.014061" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Circulation: Arrhythmia and Electrophysiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Paul Dudley White International Scholar Award</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">American Heart Association</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation in Multimodal AI &amp; Foundational Models</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">European Society of Cardiology — Digital Health &amp; AI Summit</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Best Oral Presentation — Physionet Challenge 2025</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://physionetchallenges.org/2025/" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">IEEE Computing in Cardiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2025</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Editor-in-Chief's Featured Article of the Month</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://doi.org/10.1161/CIRCEP.124.012860" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Circulation: Arrhythmia and Electrophysiology</a></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2024</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Clinical Translation Award</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">IEEE Computing in Cardiology</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2024</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Honorary Alumnus (one of five)</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Universidad Carlos III de Madrid</div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2020</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">"la Caixa" Excellence Fellowship</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://fundacionlacaixa.org/en/scholarships-postgraduate-studies-north-america" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">"la Caixa" Foundation</a> — full master's funding at UC Berkeley<span class="ml-1 text-slate-500 dark:text-slate-400">· $100,000</span></div>
              </div>
            </li>
            <li class="flex gap-3 items-baseline">
              <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums whitespace-nowrap w-12 shrink-0">2020</span>
              <div class="flex-1">
                <span class="text-slate-900 dark:text-slate-100 font-medium leading-snug">Rafael del Pino Excellence Fellowship</span>
                <div class="text-sm text-slate-500 dark:text-slate-400 mt-0.5"><a href="https://www.frdelpino.es/" target="_blank" rel="noopener" class="hover:text-primary-600 dark:hover:text-primary-400">Rafael del Pino Foundation</a> — full master's funding at ETH Zurich<span class="ml-1 text-slate-500 dark:text-slate-400">· €48,000</span></div>
              </div>
            </li>
          </ol>
          <p class="mt-5 text-sm"><a href="/awards/" class="text-primary-600 dark:text-primary-400 hover:underline">See all awards →</a></p>
        </div>
    design:
      columns: '1'
---
