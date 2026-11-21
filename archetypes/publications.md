---
# Folder naming: <year>-<firstauthor-lastname>-<keyword>, e.g. 2027-ruiperez-diffusion.
title: "{{ replace .File.ContentBaseName "-" " " | title }}"  # Full paper title, exactly as published.
authors:                     # In published order. Use "me" for Samuel (bolds via data/authors/me.yaml); others as "F. M. Lastname".
  - "me"
  - "A. B. Coauthor"
# author_notes:              # OPTIONAL, parallel to authors; "Equal contribution" renders an asterisk, "" for the rest.
#   - "Equal contribution"
#   - ""
date: "{{ .Date }}"          # Publication date; drives the year shown in citations. Set to e.g. "2027-03-01T00:00:00Z".
publishDate: "{{ .Date }}"   # Keep equal to date (when the page goes live).
publication_types: ["article-journal"]  # CSL type; every journal paper on this site uses article-journal.
publication: "*Journal Name*"  # Venue in markdown italics (asterisks required), e.g. "*Nature Communications*".
# impact_factor: 0.0         # OPTIONAL: journal impact factor (number, no quotes).
abstract: |-
  Paste the VERBATIM published abstract here. Never paraphrase or invent text.
# summary: ""                # OPTIONAL one-liner, e.g. "Editor in Chief's Featured Article of the Month."
tags:                        # 2-4 topic tags, Title Case, reuse existing tags where possible.
  - "Cardiac Electrophysiology"
featured: false              # true -> appears in homepage "Selected Publications" (auto via featured_only).
# links:                     # OPTIONAL extra buttons next to the DOI "Link" button.
#   - name: "arXiv"
#     url: "https://arxiv.org/abs/XXXX.XXXXX"
hugoblox:
  ids:
    doi: ""                  # DOI only (no https://doi.org/ prefix); renders the primary "Link" button.
---
