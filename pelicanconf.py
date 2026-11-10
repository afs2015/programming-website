AUTHOR = "Andrew Selzer"
SITENAME = "Andrew Selzer"
SITESUBTITLE = "> full-stack senior developer"
SITE_TAGLINE = "Python & Django Developer in Somerville, MA"
SITE_DESCRIPTION = (
    "Andrew Selzer is a full-stack Python and Django developer in Somerville, MA "
    "who writes and speaks about open source, Django, and web development."
)
SITEURL = ""

# Structured data (JSON-LD) describing the site owner — see templates/jsonld.html
PERSON = {
    "jobTitle": "Full-Stack Software Engineer",
    "image": "images/andrew-selzer-headshot.jpg",
    "locality": "Somerville",
    "region": "MA",
    "country": "US",
    "alumniOf": "The Pennsylvania State University",
    "knowsAbout": [
        "Python",
        "Django",
        "Flask",
        "JavaScript",
        "HTMX",
        "Alpine.js",
        "PostgreSQL",
        "Apache Airflow",
        "AWS",
        "Open source",
        "Web development",
    ],
    "sameAs": [
        "https://github.com/afs2015",
        "https://www.linkedin.com/in/andrew-selzer/",
        "https://andrewselzer.com",
    ],
    "talks": [
        {
            "name": "Enter the Ecosystem: Contributing to Django Open Source Projects",
            "event": "DjangoCon US 2026",
            "startDate": "2026-08-24",
            "endDate": "2026-08-28",
            "city": "Chicago",
            "region": "IL",
            "video": "https://www.youtube.com/watch?v=ciJndAym7BA",
        },
    ],
}

THEME = "themes/papyrus-cyberpunk"
DISPLAY_PAGES_ON_MENU = True

PATH = "content"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static files copied as-is; robots.txt is served from the site root
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# Sitemap (pelican-sitemap plugin) — written to /sitemap.xml
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 1.0, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "weekly", "pages": "monthly"},
    # Low-value listing pages and the about -> home redirect stay out of the sitemap
    "exclude": [
        r"^pages/about\.html$",
        r"^authors?(/|\.html)",
        r"^categor(y|ies)(/|\.html)",
        r"^tags?(/|\.html)",
    ],
}

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {"archives": None}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
