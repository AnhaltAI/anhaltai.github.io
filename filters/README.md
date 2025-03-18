# Filters
## Conditional metadata
Solves the fact that diff languages should have different front-matter attributes as well (currently only titles).

To use (**BUT DON'T DO THIS, it's already included in `_metadata.yml` globally**):

```qmd
---
# will fall back to the standard title if translation not found
title: "Publications and Awards"
titles:
  # language codes have to match profile name exactly   
  de: "Veröffentlichungen"
  ua: "Публікації"
# Either add in a `_metadata.yaml` in the entire directory or per-file
# RELATIVE PATH! Inside posts_blog it's `../_filters/conditional-metadata.lua` etc.
filters: [./_filters/conditional-metadata.lua]
# etc. 
--- 

::: {.content-visible when-profile="en"}
English text
:::
# ... etc.
```
Assuming `en,de,ua` are the different profiles, it will pick the title from the one matching current profile name/language. 
Assumes only one profile is set, and it matches the language code exactly.

## Problems / TODO
- Doesn't work for listings! E.g. title of blog posts will be same as the main title
- Support other fields: [HTML Options – Quarto](https://quarto.org/docs/reference/formats/html.html#title-author)
  - used by us:
    - description in Lehre / courses.
  - not used by us
    - subtitle
    - abstract
- Ideally a separate structure to make it cleaner and more robust:

```qmd
---
title: "Publications and Awards"
description: "Our ..."
langs:
  title:
    en: "Publications and Awards"
    de: "Veröffentlichungen"
    ua: "Публікації"
  description:
    en: "Summary of our ..."
    de: "Fazit"
    ua: ...
filters: [./_filters/conditional-metadata.lua]
---
```
