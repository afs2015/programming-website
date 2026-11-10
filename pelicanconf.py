AUTHOR = "Andrew Selzer"
SITENAME = "Andrew Selzer"
SITESUBTITLE = "> full-stack senior developer"
SITE_TAGLINE = "Full-Stack Senior Developer | Python & Django"
SITE_DESCRIPTION = (
    "Andrew Selzer is a full-stack senior developer in Somerville, MA who works in "
    "Python and Django and writes and speaks about open source and web development."
)
SITEURL = ""

# Default link-preview image (Open Graph / Twitter). A post can override it with
# an `Image: images/whatever.jpg` metadata line.
SOCIAL_IMAGE = "images/social-card.jpg"
SOCIAL_IMAGE_ALT = "Andrew Selzer, full-stack senior developer in Somerville, MA"

# Profiles verified with rel="me" (e.g. Mastodon's green checkmark) — rendered in <head>
REL_ME = ["https://mastodon.social/@AndrewSelzer"]

# Structured data (JSON-LD) describing the site owner — see templates/jsonld.html
PERSON = {
    "jobTitle": "Full-Stack Senior Developer",
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
        "https://mastodon.social/@AndrewSelzer",
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
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon.svg": {"path": "favicon.svg"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

# Single author, single category: skip the thin author/category/tag listing pages
DIRECT_TEMPLATES = ["index", "archives", "404"]
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""

# Clean URLs: /blog/<slug>/ for posts, /<slug>/ for pages, /blog/ for the post list
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARCHIVES_URL = "blog/"
ARCHIVES_SAVE_AS = "blog/index.html"
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

# Old URLs -> new ones, written as redirect pages by plugins/redirects.py.
# Add an entry here whenever a published URL changes.
REDIRECTS = {
    "archives.html": "blog/",
    "welcome.html": "blog/welcome/",
    "pages/talks.html": "talks/",
    "pages/about.html": "",
}

# Sitemap (pelican-sitemap plugin) — written to /sitemap.xml
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "redirects"]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 1.0, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "weekly", "pages": "monthly"},
    # Low-value listing pages, redirects, and the 404 page stay out of the sitemap
    "exclude": [
        r"^about/",
        r"^404\.html$",
        r"^authors?(/|\.html)",
        r"^categor(y|ies)(/|\.html)",
        r"^tags?(/|\.html)",
    ],
}

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {"archives": None}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
