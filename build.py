"""Builds the Smart Building Finishes website.

Edit the business details in SITE below, or the page content in pages/,
then run:  python build.py
The finished .html files are written next to this script.
"""

from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

# Business details used on every page. Change them here, then rebuild.
SITE = {
    "name": "Smart Building Finishes",
    "tagline": "Building automation, CCTV and access control",
    "phone": "(876) 506-8383",
    "phone_dial": "+18765068383",
    "email": "smartbuildingfinishes@gmail.com",
    # Leave the address empty to hide it on the site.
    "address": "",
    "area": "island-wide across Jamaica",
    "hours": "Monday to Saturday, 9:00am to 6:00pm",
    # Paste a form service URL (e.g. Formspree) to receive enquiries without
    # opening the visitor's email app. Leave empty to use email instead.
    "form_endpoint": "",
}

PLACEHOLDERS = {
    "phone": "+1 (000) 000-0000",
    "email": "info@example.com",
    "address": "Your street address, City",
    "area": "your service area",
}

PAGES = [
    {
        "file": "index.html",
        "source": "home.html",
        "nav": "Home",
        "title": "Smart Building Finishes | Building automation, CCTV and access control",
        "description": "Smart Building Finishes designs, installs and maintains building automation, CCTV and access control systems for commercial and residential properties.",
    },
    {
        "file": "services.html",
        "source": "services.html",
        "nav": "Services",
        "title": "Services | Smart Building Finishes",
        "description": "Building automation, CCTV surveillance and access control: design, installation, integration and maintenance.",
    },
    {
        "file": "projects.html",
        "source": "projects.html",
        "nav": "Projects",
        "title": "Projects | Smart Building Finishes",
        "description": "CCTV and smart lock installations by Smart Building Finishes, including Rogers Commercial Centre, The Bhamboa, Sky View Apartments and Holborn Road.",
    },
    {
        "file": "about.html",
        "source": "about.html",
        "nav": "About",
        "title": "About | Smart Building Finishes",
        "description": "How Smart Building Finishes approaches building automation and security projects.",
    },
    {
        "file": "contact.html",
        "source": "contact.html",
        "nav": "Contact",
        "title": "Contact | Smart Building Finishes",
        "description": "Request a quote or site survey for building automation, CCTV or access control.",
    },
]

MARK = (
    '<svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true">'
    '<rect x="3" y="3" width="26" height="26" rx="6" fill="currentColor" opacity=".16"/>'
    '<path d="M9 23V12l7-4 7 4v11" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>'
    '<circle cx="16" cy="17" r="2.6" fill="currentColor"/>'
    "</svg>"
)


def brand():
    for ext in ("svg", "png", "jpg", "webp"):
        if (ROOT / "assets" / "img" / f"logo.{ext}").exists():
            return f'<img class="brand-logo" src="assets/img/logo.{ext}" alt="{escape(SITE["name"])}">'
    return f'{MARK}<span class="brand-name">Smart Building <b>Finishes</b></span>'


def tokens():
    values = {key: escape(value) for key, value in SITE.items()}
    values["phone_href"] = "tel:" + SITE["phone_dial"]
    address = values["address"]
    values["address_item"] = f"<li>{address}</li>" if address else ""
    values["address_row"] = f"<dt>Address</dt><dd>{address}</dd>" if address else ""
    values["area_label"] = "Serving the entire island"
    values["year"] = str(date.today().year)
    return values


def render(page):
    nav = "\n".join(
        '        <li><a href="{file}"{current}>{nav}</a></li>'.format(
            file=p["file"],
            nav=p["nav"],
            current=' aria-current="page"' if p is page else "",
        )
        for p in PAGES
    )
    body = (ROOT / "pages" / page["source"]).read_text(encoding="utf-8")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page["title"])}</title>
  <meta name="description" content="{escape(page["description"])}">
  <meta property="og:title" content="{escape(page["title"])}">
  <meta property="og:description" content="{escape(page["description"])}">
  <meta property="og:image" content="assets/img/project-commercial-complex.jpg">
  <meta name="theme-color" content="#0d1b26">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">{brand()}</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
      <nav id="site-nav" class="site-nav" aria-label="Main">
        <ul>
{nav}
        </ul>
        <a class="btn btn-accent nav-cta" href="contact.html">Request a quote</a>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <a class="brand" href="index.html">{brand()}</a>
        <p class="footer-note">{{{{tagline}}}} for commercial and residential buildings.</p>
      </div>
      <div>
        <h2>Services</h2>
        <ul>
          <li><a href="services.html#automation">Building automation</a></li>
          <li><a href="services.html#cctv">CCTV surveillance</a></li>
          <li><a href="services.html#access">Access control</a></li>
        </ul>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Get in touch</h2>
        <ul>
          <li><a href="{{{{phone_href}}}}">{{{{phone}}}}</a></li>
          <li><a href="mailto:{{{{email}}}}">{{{{email}}}}</a></li>
          <li>{{{{area_label}}}}</li>
          {{{{address_item}}}}
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; {{{{year}}}} {{{{name}}}}. All rights reserved.</p>
    </div>
  </footer>
  <script src="js/main.js" defer></script>
</body>
</html>
"""
    for key, value in tokens().items():
        html = html.replace("{{" + key + "}}", value)
    return html


def main():
    for page in PAGES:
        (ROOT / page["file"]).write_text(render(page), encoding="utf-8")
        print("built", page["file"])
    pending = [key for key, value in PLACEHOLDERS.items() if SITE[key] == value]
    if pending:
        print("Still using placeholder values for:", ", ".join(pending))


if __name__ == "__main__":
    main()
