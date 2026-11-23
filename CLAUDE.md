# CLAUDE.md

Personal academic website of Samuel Ruipérez-Campillo (PhD candidate, Institute of
Machine Learning, ETH Zurich; visiting research fellow, MIT/Harvard Medical School).
Hugo Blox v2 "academic-cv" template, heavily customized. Deployed to GitHub Pages
on push to `main`. For update recipes (new paper/talk/award/news/CV), follow
**UPDATING.md** — do not improvise formats.

## Content model

- `content/publications/<year-lastname-keyword>/index.md` — journal papers only
  (`publication_types: ["article-journal"]`). Key fields: `authors` (`"me"` = owner,
  bolded via `data/authors/me.yaml`; optional parallel `author_notes` with
  "Equal contribution"), `publication` (journal in `*italics*`), `abstract`
  (verbatim), `hugoblox.ids.doi` (bare DOI → "Link" button), optional
  `impact_factor`, `links:`, `summary`, `tags`, `featured`.
- `content/events/<year-venue-topic>/index.md` — talks. Key fields: `event_name`
  (canonical venue spellings — see UPDATING.md), `location`, `talk_type`
  (`conference` | `invited`; invited get their own section on `/events/`),
  `awards:` (strings → badges), `summary`/`abstract`, `featured`.
- `content/awards.md` — canonical awards record (hand-written HTML list,
  year gutter + hairline separators).
- `content/_index.md` — homepage sections: hero (reads `data/authors/me.yaml`),
  News block, Research blurb, Selected Publications (collection block),
  Selected Talks (`blox/selected-talks`), Selected Awards block.
- `data/authors/me.yaml` — bio, role, links, `education:` and `experience:`
  (these feed `/experience/` via `blox/resume-experience`).
- `static/uploads/resume.pdf` — the CV behind the hero "Download CV" button.
- `archetypes/publications/` and `archetypes/events/` — commented skeletons;
  `hugo new publications/<slug>/index.md` (or without `/index.md`) uses them.

## Curated vs automatic

- AUTOMATIC (set `featured: true` on the entry): homepage Selected Publications
  (collection block with `featured_only: true`) and Selected Talks.
- MANUALLY CURATED (edit HTML in `content/_index.md`): News (Month-Year gutter,
  ~6 items, newest first) and Selected Awards (a curated copy of `awards.md`,
  not a feed).

## Design system — "Refined Scholar, Inter edition"

Inter site-wide (typography.pack "modern", self-hosted variable font; headings
semibold with tracking tightened in proportion to size — see custom.css); light
mode is the default (`theme.mode: light`, toggle kept — the owner explicitly
rejected dark-on-first-load); content rail 48rem, widening to 56rem at ≥1440px
via the `--container-3xl` override; horizontal hero with the name forced to one
line at ≥1024px; one blue accent + slate neutrals; two signature flourishes on
the homepage Research section: an animated "denoising ECG" trace (blox/ecg-divider,
path data from scripts/gen_ecg.py, draw-once on scroll, reduced-motion fallback)
between the Research heading and three hairline research-theme cards with inline
line-art SVG icons (in content/_index.md + custom.css); flat
surfaces, hairline rules, year gutters on all lists; `whitespace-nowrap` on year
cells; no emoji in headings. Custom layouts live in `layouts/` (publications
list/single, events list/page, citation view, author bolding) and `blox/`
(hero, experience, selected-talks). `assets/css/custom.css` has a **FRAGILE**
section (selectors into Hugo Blox module internals) tied to the module versions
pinned in `go.mod` and `hugo_version: 0.161.1` in `hugoblox.yaml` — re-verify
that section visually after any module/Hugo upgrade.

## House rules

- Never invent facts. Abstracts verbatim from the published paper only; exact
  titles, dates, venues. If unverifiable, ask or leave out.
- Monetary amounts only on the two major fellowships ("la Caixa" $100,000;
  Rafael del Pino €48,000).
- Spellings: PhysCade Inc., SWiiFT Inc., Universidad Carlos III de Madrid.
- Git: commit locally; push only when the owner explicitly says so.
- Always verify the build before finishing: `hugo --minify --destination /tmp/<unique>`.
- Never add `publications.bib` at the repo root (triggers an import workflow PR).

## Syncing the site from an updated CV

1. Replace `static/uploads/resume.pdf` with the new CV.
2. Diff the new CV against the site: publications (`content/publications/`),
   talks (`content/events/`), awards (`content/awards.md`), education/experience
   (`data/authors/me.yaml`), bio.
3. Propose the adds, then create them per the UPDATING.md recipes
   (archetype-based `hugo new` for papers/talks).
4. Update the News block for announcement-worthy items (newest on top, prune old).
5. Keep curated lists curated: when adding to Selected Awards or News means
   something else should drop out, or a `featured` flag should be removed,
   ask before demoting anything.
6. Build green, commit locally, push only on explicit instruction.
