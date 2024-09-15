project = "Portfolio"
copyright = "2024, Vikram Rangarajan"
author = "Vikram Rangarajan"


extensions = [
    "sphinx_design",
    "sphinx_simplepdf",
]

templates_path = ["_templates"]
exclude_patterns = []

email = "vikram.rangaraja@gmail.com"
phone = "609-608-6762"
linkedin = "https://linkedin.com/in/vikram-rangarajan/"
github = "https://github.com/VikramRangarajan"

html_theme = "pydata_sphinx_theme"
html_sidebars = {"**": []}
html_theme_options = {
    "navigation_with_keys": False,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "github_url": github,
    "logo": {
        "text": "Introduction",
    },
    "icon_links": [
        {
            "name": "LinkedIn",
            "url": linkedin,
            "icon": "fa-brands fa-linkedin",
            "type": "fontawesome",
        },
        {
            "name": "Email",
            "url": f"mailto:{email}",
            "icon": "fa-solid fa-envelope",
            "type": "fontawesome",
        },
        {
            "name": "Phone",
            "url": f"tel:{phone}",
            "icon": "fa-solid fa-phone",
            "type": "fontawesome",
        },
    ],
    "footer_end": [],
    "search_bar_text": "Search the Portfolio...",
}
html_static_path = ["_static"]
html_show_sphinx = False
html_show_sourcelink = False
