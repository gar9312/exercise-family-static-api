from flask import jsonify, url_for

class APIException(Exception):
    """Custom exception class to handle API errors with a JSON response."""
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """Initialize the exception with a message, optional status code, and additional payload."""
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Convert the exception details to a dictionary."""
        response = dict(self.payload or {})
        response['message'] = self.message
        return response

def has_no_empty_params(rule):
    """Check if a route rule has no empty parameters."""
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    """Generate a sitemap for all available routes in the Flask application."""
    links = []
    for rule in app.url_map.iter_rules():
        # Include only GET routes that don't require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)

    links_html = "".join([f"<li><a href='{url}'>{url}</a></li>" for url in links])
    return f"""
        <div style="text-align: center;">
            <img src='https://github.com/breatheco-de/exercise-family-static-api/blob/master/rigo-baby.jpeg?raw=true' alt='Rigo Baby' />
            <h1>Hello Rigo!</h1>
            <p>This is your API home. Remember to specify a valid endpoint path, like:</p>
            <ul style="text-align: left;">{links_html}</ul>
        </div>
    """
