from src.main.python.api.app import app
from src.main.python.models.db_connection import setup_db_config

# app = Flask(__name__)
setup_db_config(app)


# db = SQLAlchemy(app)


def create_app():
    from src.main.python.models.database import create_tables
    create_tables()

    from src.main.python.api.fiu_controller import fiu_blueprint
    from src.main.python.api.fip_controller import fip_blueprint
    from src.main.python.api.aa_controller import aa_blueprint
    # Register the blueprints
    app.register_blueprint(fiu_blueprint, url_prefix='/v1/FIU')
    app.register_blueprint(fip_blueprint, url_prefix='/v1/FIP')
    app.register_blueprint(aa_blueprint, url_prefix='/v1/AA')

    return app


if __name__ == '__main__':
    create_app = create_app()
    create_app.run(port=8000)
else:
    gunicorn_app = create_app()
