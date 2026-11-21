# Updating the site

One recipe per flow. Preview anytime with `hugo server` (http://localhost:1313).

## a) New paper

```bash
hugo new publications/2027-lastname-keyword/index.md   # year-firstauthor-keyword
```

The generated file is fully commented — fill it in. Fields that matter:

- `title` — exact published title.
- `authors` — published order; `"me"` for Samuel (auto-bolded), others as `"F. M. Lastname"`.
  Co-first authorship: add a parallel `author_notes` list with `"Equal contribution"` / `""`.
- `date` / `publishDate` — publication date (sets the citation year and sort order).
- `publication` — journal in markdown italics: `"*Circulation: Arrhythmia and Electrophysiology*"`.
- `abstract` — verbatim from the published paper. Never paraphrase.
- `hugoblox.ids.doi` — bare DOI (no URL prefix); renders the "Link" button.
- `featured: true` — surfaces it in the homepage "Selected Publications" list
  (automatic: the collection block in `content/_index.md` uses `featured_only: true`).
- Optional: `impact_factor`, `summary` (e.g. award note), `links:` (extra buttons), `tags`.

If it is announcement-worthy, also add a News line (recipe d).

Note: do not add a `publications.bib` at the repo root — pushing one triggers
`.github/workflows/import-publications.yml`, which opens an auto-generated PR.

## b) New talk

```bash
hugo new events/2027-venue-topic/index.md
```

Fields that matter:

- `title`, `date` (month precision is fine), `location` (`"City, Country"`).
- `event_name` — reuse the canonical spellings already in `content/events/`, e.g.
  "European Heart Rhythm Association (EHRA)", "European Society of Cardiology Congress (ESC)",
  "IEEE Computing in Cardiology", "IEEE Engineering in Medicine & Biology Conference (EMBC)",
  "American Heart Association Scientific Sessions (AHA)", "ESC Digital Health and AI Summit (ESC-DCAI)".
- `talk_type` — `conference` (default) or `invited`; invited talks get their own
  section at the top of `/events/`.
- `awards:` — list of award names; each renders as a badge on the talk page and list.
- `featured: true` — surfaces it in the homepage "Selected Talks" list (automatic,
  reverse-chronological, rendered by `blox/selected-talks/block.html`).
- `summary` — one factual sentence; `abstract` (verbatim) replaces it when present.

If the talk won an award, also do recipe (c).

## c) New award

1. Add it to `content/awards.md` — the canonical record. Copy an existing `<li>`
   block (year gutter + title + venue line) and keep reverse-chronological order.
2. Optionally add it to the homepage "Selected Awards" list — the `awards` markdown
   block in `content/_index.md`. This list is MANUALLY CURATED (a copy, not a feed);
   adding to `awards.md` does not surface it on the homepage.
3. If tied to a talk, add it to that event's `awards:` list too (badge).
4. Consider a News line (recipe d).

House rule: monetary amounts appear only on the two major fellowships
("la Caixa" $100,000; Rafael del Pino €48,000) — none elsewhere.

## d) News item

Edit the `news` markdown block in `content/_index.md` (MANUALLY CURATED).
Insert a new `<li>` at the top of the `<ol>`, following the Month-Year gutter
convention (abbreviated month + year in the fixed-width span):

```html
<li class="flex gap-3 items-baseline">
  <span class="text-slate-500 dark:text-slate-400 text-sm font-medium tabular-nums w-20 shrink-0">Jun 2027</span>
  <div class="flex-1 leading-snug">One factual sentence, with an internal link such as
    <a href="/publications/2027-lastname-keyword/" class="hover:text-primary-600 dark:hover:text-primary-400 font-medium">the paper</a>.</div>
</li>
```

Keep the list short (~6 items): add at the top, prune the oldest.

## e) Updated CV PDF

1. Replace `static/uploads/resume.pdf` (the hero "Download CV" button points here).
2. Diff the new CV against the site and sync `data/authors/me.yaml` if anything
   changed: `education:` and `experience:` feed `/experience/`; `bio:` feeds the
   homepage About. Then run recipes (a)-(d) for any new papers/talks/awards/news.

## f) Preview and publish

```bash
hugo server                                   # live preview
hugo --minify --destination /tmp/site-check   # sanity build (must be green)
git add -A && git commit -m "..."             # commit locally
git push                                      # ONLY when ready to go live
```

Pushing to `main` runs `.github/workflows/deploy.yml`: it reads
`hugoblox.yaml` (`deploy.host: github-pages`, `hugo_version: 0.161.1`), calls
`build.yml` (installs pnpm deps + Tailwind CLI, builds with that pinned Hugo,
uploads the artifact), then publishes via `actions/deploy-pages`. No manual
steps; the site is live a few minutes after push. PRs against `main` run the
build as a check without deploying.

## Naming standards

- PhysCade Inc. (capital C), SWiiFT Inc., Universidad Carlos III de Madrid.
- Venue names: use the canonical `event_name` spellings listed in recipe (b).
- Journal names in `publication:` exactly as the journal styles itself, in `*italics*`.

## House rules

- No emoji in headings (or anywhere on the site).
- No invented facts: abstracts verbatim, titles exact, dates/venues verified.
- Homepage lists: Selected Publications and Selected Talks are AUTOMATIC
  (`featured: true`); News and Selected Awards are MANUALLY CURATED in
  `content/_index.md`; `content/awards.md` is the canonical awards record.
