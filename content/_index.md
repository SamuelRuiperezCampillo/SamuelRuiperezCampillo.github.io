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

  - block: markdown
    id: papers
    content:
      title: Featured Publications
      text: |
        <div class="not-prose mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">

          <a href="/publications/2025-ruiperez-noise-vae/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2025-ruiperez-noise-vae.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Generative Models · Signal Processing</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Reducing Diverse Sources of Noise in Ventricular Electrical Signals Using Variational Autoencoders</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300"><strong>S. Ruipérez-Campillo</strong> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">November 2025</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2025-tonko-endo-epicardial/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2025-tonko-endo-epicardial.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Cardiac Electrophysiology · Ventricular Arrhythmia</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Endo-Epicardial Electrical Disarray in Arrhythmogenic Cardiomyopathy with Ventricular Arrhythmias</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300">J. B. Tonko<sup>*</sup>, <strong>S. Ruipérez-Campillo</strong><sup>*</sup> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">September 2025</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2024-pancorbo-vector-field/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2024-pancorbo-vector-field.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Cardiac Electrophysiology · Signal Processing</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Vector Field Heterogeneity for Assessing Locally Disorganised Cardiac Wavefronts from High-Density Multielectrodes</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300">L. Pancorbo<sup>*</sup>, <strong>S. Ruipérez-Campillo</strong><sup>*</sup> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">January 2024</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2024-kolk-vt-dynamic/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2024-kolk-vt-dynamic.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Ventricular Arrhythmia · Deep Learning</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Dynamic Prediction of Malignant Ventricular Arrhythmias Using Neural Networks in ICD Patients</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300">M. Z. H. Kolk, <strong>S. Ruipérez-Campillo</strong> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">January 2024</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2023-ruiperez-clique-omnipolar/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2023-ruiperez-clique-omnipolar.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Cardiac Electrophysiology · Signal Processing</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Evaluation and Assessment of Clique Arrangements for the Estimation of Omnipolar Electrograms in High-Density Electrode Arrays</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300"><strong>S. Ruipérez-Campillo</strong> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">June 2023</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2023-castells-electrode-config/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2023-castells-electrode-config.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Cardiac Electrophysiology · Signal Processing</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Performance Assessment of Electrode Configurations for the Estimation of Omnipolar Electrograms from High-Density Arrays</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300">F. Castells<sup>*</sup>, <strong>S. Ruipérez-Campillo</strong><sup>*</sup> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">March 2023</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

          <a href="/publications/2022-ruiperez-macroreentrant/" class="group flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-shadow hover:shadow-md md:col-span-2 md:max-w-[calc(50%-0.75rem)] dark:border-gray-700 dark:bg-gray-900">
            <img src="/featured/2022-ruiperez-macroreentrant.jpg" alt="" loading="lazy" class="aspect-[16/9] w-full bg-gray-100 object-cover dark:bg-gray-800" />
            <div class="flex flex-1 flex-col p-5">
              <p class="mb-2 text-xs font-semibold uppercase tracking-wider text-primary-600 dark:text-primary-400">Vectorcardiogram · Atrial Tachycardia</p>
              <h3 class="mb-3 text-base font-semibold leading-snug">Non-invasive Characterisation of Macroreentrant Atrial Tachycardia Types from a Vectorcardiographic Approach with the Slow Conduction Region as a Cornerstone</h3>
              <p class="mb-1 text-sm text-gray-700 dark:text-gray-300"><strong>S. Ruipérez-Campillo</strong> et al.</p>
              <p class="mb-4 text-xs text-gray-500 dark:text-gray-400">March 2022</p>
              <span class="mt-auto text-sm font-medium text-primary-600 group-hover:underline dark:text-primary-400">Read more →</span>
            </div>
          </a>

        </div>
    design:
      columns: '1'

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
      order: desc
    design:
      view: compact
---
