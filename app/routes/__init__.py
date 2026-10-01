"""Route registration for the application."""

from app.routes.api import route_specs as api_routes
from app.routes.home import route_specs as home_routes


def register_routes(app):
    for route in [*home_routes, *api_routes]:
        app.add_api_route(**route)
