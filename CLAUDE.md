# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A static site ([pythonframeworks.com](https://pythonframeworks.com/)) listing popular Python frameworks organized by category. The entire site is a single `index.html` file — there is no backend in production. Bottle.py is used only for local development.

## Running Locally

```bash
python3 frameworks.py
```

Visit `http://localhost:8080/`. Hot reloading is enabled by default (`reloader=True`).

## Architecture

- **`frameworks.py`** — Entire backend (16 lines). Two routes: `/` renders `index.html` as a Bottle template, `/static/<path>` serves static files.
- **`index.html`** — All content lives here (~4,300 lines). Each framework is a Bootstrap card. Categories are `<div class="category" id="CategoryName">` sections containing a Masonry grid of cards.
- **`bottle.py`** — Vendored single-file WSGI micro-framework for local development only. Do not edit.
- **`static/`** — CSS/JS libraries (Bootstrap 5, Masonry, ImagesLoaded) and framework logos under `static/image/logos/`.

## Adding a Framework

Add a Bootstrap card inside the appropriate category's `.row.grids` div in `index.html`:

```html
<div class="col-sm-6 col-lg-3 mb-4">
    <div class="card">
        <!-- name, link, logo, description -->
    </div>
</div>
```

## Adding a Category

```html
<hr class="my-4">

<div class="category" id="CategoryName">
    <h3 class="mt-5 display-6">Category Name</h3>
    <p>Description of this category</p>

    <div class="row grids mt-4" data-masonry='{"percentPosition": true }'>
        <!-- cards go here -->
    </div>
</div>
```

The navigation tag cloud is dynamically generated from category `id` attributes and card counts — no manual nav updates needed.
