# db_config.py

import os
import yaml
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import inspect  # Import the inspect function

app = Flask(__name__)


# Read database configuration from the resources
def get_db_config():
    test_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(test_script_dir, '..', '..', '..', '..'))
    config_path = os.path.join(project_root, 'src', 'main', 'python', 'resources', 'db_config.yaml')
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)


# Set up SQLAlchemy with your Flask app
db_params = get_db_config()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
db = SQLAlchemy(app)


class UserInfo(db.Model):
    __tablename__ = 'user_info'

    entity_id = db.Column(db.String(255), primary_key=True)
    clientId = db.Column(db.String(255), nullable=False)
    userType = db.Column(db.String(255), nullable=False)


def create_tables():
    # Check if the table exists before creating it
    with app.app_context():
        if not inspect(db.engine).has_table('user_info'):
            db.create_all()


def insert_data(entity_id, client_id, user_type):
    try:
        new_user = UserInfo(entity_id=entity_id, clientId=client_id, userType=user_type)
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        app.logger.error("Failed to create new user:", e)
        return False
