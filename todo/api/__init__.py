from flask import Blueprint
from flask_restx import Api

from todo.api.namespaces import todo_ns

api_blueprint = Blueprint("api", __name__)

API_VERSION = "v1"


def register_api(app):
    app.config["RESTX_ERROR_404_HELP"] = False
    app.register_blueprint(api_blueprint, url_prefix=f"/api/{API_VERSION}")


api = Api(
    api_blueprint,
    version=API_VERSION,
    title="Todo API",
    description="A simple todo API.",
)

api.add_namespace(todo_ns)
