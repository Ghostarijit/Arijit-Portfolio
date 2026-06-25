"""
Export the Django portfolio to a static HTML site for GitHub Pages.
Run: python export_static.py
"""
import os
import sys
import shutil

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")

import django
django.setup()

from django.test import RequestFactory
from core.views import home

# Generate HTML from Django view
factory = RequestFactory()
request = factory.get("/")
response = home(request)
if hasattr(response, "render"):
    response.render()
html = response.content.decode("utf-8")

# Fix static paths for GitHub Pages (relative paths)
html = html.replace('/static/', './static/')

# Write to docs/index.html
output_dir = os.path.join(os.path.dirname(__file__), "docs")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

# Copy static files
static_src = os.path.join(os.path.dirname(__file__), "static")
static_dst = os.path.join(output_dir, "static")
if os.path.exists(static_dst):
    shutil.rmtree(static_dst)
shutil.copytree(static_src, static_dst)

print(f"Static site exported to {output_dir}/")
print(f"  - index.html")
print(f"  - static/css/style.css")
print(f"  - static/js/main.js")
