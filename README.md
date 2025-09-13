# PH-ormula.github.io

## 1. Quick Start

```
# 1 · clone your fork
git clone https://github.com/<your-user>/ph-ormula.github.io
cd ph-ormula.github.io

# 2 · install gems into .bundle/ (no sudo required)
bundle config set --local path '.bundle'
bundle install

# 3 · launch local server (ctrl-c to stop)
bundle exec jekyll serve
```

The site recompiles automatically when you save files and is served at <http://localhost:4000>.

---

## 2. Adding a New Page

1. **Create a Markdown file** inside the project root.  
   Filename = slug (e.g. `my-topic.md`).

2. **Front matter template**

   ```
   ---
   layout: page          # keep as “page” so Minima uses the full-width layout
   title:  "My Topic"    # displayed in browser tab and h1
   permalink: /my-topic/ # clean URL → http://…/my-topic/
   ---
   ```

3. **Write content** below the front matter in regular Markdown.

4. **Decide whether it appears in the top-right navigation**  
   - Header links are listed manually in `_config.yml → header_pages:`.
   - To **show** the page, add its filename there.
   - To **hide** the page, do nothing; the page is still reachable via its permalink.

---

## 3. Images & Downloads

- Put assets in `images/` and link relatively: `![Alt text](/images/diagram.png){: width="60%"}`

- Large binaries (PDFs, ZIPs) go in `files/` to keep the repo lean, but for non-embedded files it is recommended to use a link to an external website for download

---

## 4. Working Branches & Pull Requests

1. Create a branch: `git checkout -b my-feature`
2. Commit logically: `git add file.md; git commit -m "Add My Topic page"`
3. Push and open a PR against `main`.
4. CI (GitHub Pages) builds the site automatically; verify the preview URL shown by GitHub.

---

## 5. Troubleshooting

| Symptom                           | Fix                                                               |
| --------------------------------- | ----------------------------------------------------------------- |
| `Bundler::PermissionError`        | You skipped `bundle config` – run the commands in Quick Start.    |
| Infinite Sass “import loop” error | Never name files `_sass/minima.scss`; instead edit `assets/main.scss`. |
| 404 on a link                     | Link to `/my-topic/` or `my-topic.html`, **not** `my-topic.md`.   |

---

## 6. Housekeeping Rules

* `_site/`, `.bundle/`, `Gemfile.lock`, caches, etc. are already in `.gitignore`; **do not commit them**.  
* `README.md` is excluded from the published site via `_config.yml → exclude:`.  
* Keep line length ≤ 100 chars so diffs stay readable.

Happy writing!
