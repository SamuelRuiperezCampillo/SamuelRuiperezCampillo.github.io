---
# Folder naming: <year>-<venue>-<topic>, e.g. 2027-ehra-foundation-models.
title: "{{ replace .File.ContentBaseName "-" " " | title }}"  # Talk/abstract title as presented.
date: "{{ .Date }}"          # Talk date (month precision is fine), e.g. "2027-06-01T00:00:00Z"; drives the year gutter.
event_name: ""               # Canonical venue name; reuse existing spellings, e.g. "European Heart Rhythm Association (EHRA)", "IEEE Computing in Cardiology".
location: ""                 # "City, Country", e.g. "Vienna, Austria".
summary: ""                  # One factual sentence describing the talk; shown on the talk page if no abstract.
# abstract: |-               # OPTIONAL: verbatim abstract; replaces summary on the talk page when present.
#   ...
authors:                     # Presenter(s); "me" bolds Samuel via data/authors/me.yaml.
  - me
talk_type: conference        # "conference" or "invited"; invited talks list under "Invited Talks" on /events/.
# awards:                    # OPTIONAL: award names render as badges on the talk page and /events/ list.
#   - "Best Oral Presentation Award"
featured: false              # true -> appears in homepage "Selected Talks" (auto, reverse-chronological).
---
