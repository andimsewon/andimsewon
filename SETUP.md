# Setup Guide — Graph-first GitHub Profile README

This package includes two parts:

1. **GitHub Profile README** — static visual preview for your profile
2. **Interactive career graph** — hosted through **GitHub Pages** with drag, click, hover, and search

---

## Folder structure

Upload this structure into your special profile repository:

```text
andimsewon/
├── README.md
├── SETUP.md
├── assets/
│   ├── graph-preview.svg
│   ├── profile-circle.png
│   └── profile.jpg
└── docs/
    └── index.html
```

---

## Part 1 — Upload files to the repository

In `https://github.com/andimsewon/andimsewon`:

1. Click **Add file** → **Upload files**
2. Upload:
   - `README.md`
   - `SETUP.md`
   - everything inside `assets/`
   - the whole `docs/` folder contents
3. Commit directly to `main`

---

## Part 2 — Turn on GitHub Pages

To make the interactive graph work, enable GitHub Pages:

1. Open the repository
2. Click **Settings**
3. Go to **Pages** in the left sidebar
4. Under **Build and deployment**:
   - **Source** = `Deploy from a branch`
   - **Branch** = `main`
   - **Folder** = `/docs`
5. Save

After a short delay, the interactive page will be live at:

```text
https://andimsewon.github.io/andimsewon/
```

---

## Important limitation

GitHub Profile README does **not** support JavaScript-based interactivity directly inside the README.
That means:

- the README can show a **static graph preview**
- the **interactive draggable/clickable graph** must live on **GitHub Pages**

This is the correct architecture and the most reliable approach.

---

## What the interactive graph currently supports

- dragging nodes
- physics-based movement
- hover tooltips
- click-to-open detail panel
- search-to-focus node
- category filter chips

---

## If you want an even stronger next version later

A next iteration can add:

- node icons
- mini project thumbnails inside the detail card
- animated cluster expansion
- direct links from nodes to repos / papers / portfolio pages
- a second layer for `skills ↔ projects ↔ outputs`
- a darker, more experimental visual mode
