# Python Frameworks

A curated directory of popular Python frameworks, libraries, and tools — organized by category and published at **[pythonframeworks.com](https://pythonframeworks.com/)**.

[![Preview](static/image/screenshot.png)](https://pythonframeworks.com/)

---

## Project structure

```
index.html            # All site content (~4,500 lines)
frameworks.py         # Local dev server (Bottle.py, 16 lines)
llms.txt              # LLM/AI agent discovery file
static/
  css/                # Bootstrap 5
  js/                 # Masonry, ImagesLoaded
  image/
    logos/            # Framework logos (~190 files)
bottle.py             # Vendored single-file WSGI framework (do not edit)
```

---

## Contributing

Contributions are welcome — new frameworks, updated logos, better descriptions, and bug fixes are all appreciated.

### 1. Set up the development environment

Requires Python 3. No extra dependencies beyond the vendored `bottle.py`.

```bash
git clone https://github.com/jgujerry/pythonframeworks.git
cd pythonframeworks
python3 frameworks.py
```

Visit [http://localhost:8080/](http://localhost:8080/). The server hot-reloads on file changes.

### 2. Add a framework

All content lives in `index.html`. Find the right category section (each is a `<div class="category" id="...">`) and add a Bootstrap card inside its `.row.grids` div. Use an existing card as a reference for structure and style.

### 3. Add a category

Add a new section before the closing `</main>` tag, following this pattern:

```html
<hr class="my-4">

<div class="category" id="Category Name">
    <h3 class="mt-5 display-6">Category Name</h3>
    <p>A short paragraph describing this category and why it matters.</p>

    <div class="row grids mt-4" data-masonry='{"percentPosition": true }'>
        <!-- cards go here -->
    </div>
</div>
```

The navigation tag cloud is generated automatically from `id` attributes — no manual nav updates needed.

### 4. Update `llms.txt`

If you add a new framework or category, also update `llms.txt` at the project root so AI agents and LLM-powered search tools stay accurate.

### 5. Open a pull request

- Test your changes locally at [http://localhost:8080/](http://localhost:8080/).
- Keep card descriptions concise and neutral — describe what the framework does, not marketing copy.
- One framework or related set of changes per PR keeps reviews fast.
- Target the `main` branch.

---

## Contact

Questions or suggestions? Open an issue on GitHub or reach out to [@jgujerry](https://twitter.com/jgujerry) on X (Twitter).

## License

Released under the [MIT License](LICENSE).
