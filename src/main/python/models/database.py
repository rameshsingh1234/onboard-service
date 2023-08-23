from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from src.main.python.api.main import app

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
