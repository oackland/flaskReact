import os

from flask import Flask

from myapp.config import DevelopmentConfig, ProductionConfig
from myapp.routes import api


def create_app():
    app = Flask(__name__)

    # Configure the app based on the environment
    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Register the blueprint
    app.register_blueprint(api, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
