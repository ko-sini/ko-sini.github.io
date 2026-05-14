# ko-sini.github.io

A simple Jekyll-based GitHub Pages blog site built with Ruby and Sass.

## Overview

This repository is a GitHub Pages site using Jekyll. The site source is stored in the repository root and the generated static site is written into `_site/`.

## Requirements

- Ruby (2.7+ recommended)
  - Install: https://guides.rubyonrails.org/install_ruby_on_rails.html#install-ruby-on-windows
- Install dependencies with bundler
  - Install bundler: `gem install bundler`
  - Install bundle from Gemfile: `bundle install`

## Local development

From the repository root:

```bash
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000` in your browser.

### WSL troubleshooting of `jekyll serve`

If you get the error `Jekyll: Operation not permitted @ apply2files` on WSL you may need to change ownership of the project files. Run:

```bash
sudo chmod -R 777 /mnt/e/Work/project/
sudo chown -R <youruser> /mnt/e/Work/project/
```

After this you may need to restart VSCode and WSL for the ownership changes to become effective.

## Build output

The generated site is written to `_site/`. Do not edit files inside `_site/` directly; they are regenerated each time Jekyll builds.

## Project structure

Root files:

- `index.html` — home page content
- `about.md` — about page content
- `blog.html` — blog listing page that loops through posts
- `staff.html` — staff page content
- `README.md` — this repository documentation
- `_config.yml` — Jekyll site configuration

Content collections and data:

- `_posts/` — blog post source files in Jekyll markdown format
- `_authors/` — author collection files used by the site
- `_data/navigation.yml` — navigation menu definition used by includes

Layout and includes:

- `_layouts/default.html` — base HTML page wrapper used by all pages
- `_layouts/post.html` — layout for individual blog posts
- `_layouts/author.html` — layout for author pages
- `_includes/navigation.html` — reusable site navigation markup
- `_includes/cosine.html` — optional include used for SVG or decoration

Styles and assets:

- `assets/css/styles.scss` — main Sass entrypoint imported by Jekyll
- `_sass/main.scss` — general site styles
- `_sass/blog.scss` — blog-specific styles, including post title styling
- `assets/images/` — image assets
- `assets/svg/` — SVG assets

Generated site:

- `_site/` — generated HTML/CSS output after Jekyll builds the site

## How fonts are handled

Google Fonts are imported in `assets/css/styles.scss` using `@import url(...)`.
Then font usage is defined in the Sass files such as `_sass/main.scss` and `_sass/blog.scss`.

## Editing posts

1. Add a new Markdown file to `_posts/` with a filename like `YYYY-MM-DD-title.md`.
2. Include front matter such as:

```yaml
---
layout: post
title: "My Post Title"
date: 2026-05-13
author: ted
---
```

3. Write content below the front matter. Jekyll will generate the article page.

## Common tasks

- Add a new page: create an `.md` or `.html` file at the root and include front matter if needed.
- Change navigation: update `_data/navigation.yml` and the `_includes/navigation.html` include.
- Change layout: edit `_layouts/default.html`, `_layouts/post.html`, or `_layouts/author.html`.
- Update styles: edit `_sass/main.scss`, `_sass/blog.scss`, or `assets/css/styles.scss`.

## Notes

- The site uses Jekyll collections and defaults defined in `_config.yml`.
- Keep generated content out of source control by not editing `_site/` manually.
- For GitHub Pages, push the repo to `username.github.io` and GitHub will build it automatically.
 
