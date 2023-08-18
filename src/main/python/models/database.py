import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import inspect

from src.unittest.python.utils import read_config_file


def setup_db_config(app):
    db_params = read_config_file.read_config(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "db_config.yaml"))

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
    return db_params


app = Flask(__name__)
db_params = setup_db_config(app)
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
        app.logger.error("Failed to Insert data :", e)
        return False
