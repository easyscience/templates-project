from copier.templates import DEFAULT_JINJA_ENV

# Custom filter to ignore GitHub Actions variables
def ignore_github(value):
    if value.startswith("${{"):
        return value  # Keep GitHub Actions variables unchanged
    return value  # Jinja processes other values normally

# Register the filter in the Jinja environment
DEFAULT_JINJA_ENV.filters["ignore_github"] = ignore_github
