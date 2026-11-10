"""Write meta-refresh redirect pages for moved URLs.

GitHub Pages can't do server-side redirects, so for each entry in the REDIRECTS
setting ({old_path: new_url_path}) this writes a small HTML file at old_path that
sends visitors (and search engines, via rel=canonical) to the new location.
"""

from pathlib import Path

from pelican import signals


def write_redirects(pelican):
    settings = pelican.settings
    redirects = settings.get("REDIRECTS") or {}
    if not redirects:
        return

    from pelican.generators import Generator

    gen = Generator(
        context={},
        settings=settings,
        path=settings["PATH"],
        theme=settings["THEME"],
        output_path=pelican.output_path,
    )
    template = gen.get_template("redirect")
    output = Path(pelican.output_path)
    for old_path, new_path in redirects.items():
        target = output / old_path
        target.parent.mkdir(parents=True, exist_ok=True)
        html = template.render(
            SITEURL=settings.get("SITEURL", ""),
            SITENAME=settings.get("SITENAME", ""),
            DEFAULT_LANG=settings.get("DEFAULT_LANG", "en"),
            redirect_to=new_path,
        )
        target.write_text(html, encoding="utf-8")


def register():
    signals.finalized.connect(write_redirects)
