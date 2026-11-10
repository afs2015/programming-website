# Andrew Selzer

My personal website, built with [Pelican](https://getpelican.com/) and live at
https://andrewselzer.dev.

## Running it locally

You'll need [uv](https://docs.astral.sh/uv/). Then:

```sh
uv sync
make devserver
```

Open http://localhost:8000. The site rebuilds as you edit, though changes to
`pelicanconf.py` need a restart.

## Writing a post

Add a Markdown file to `content/` with a header like this:

```markdown
Title: My Post
Date: 2026-11-10
Tags: python, django
Slug: my-post
Summary: A sentence or two for search results and the homepage.
```

Pushing to `main` publishes the site.
