from flask import current_app

from app import db
from app.models.user import User
from app.utils import err_resp, internal_err_resp, message


class UserService:
    @staticmethod
    def get_user_data(id):
        """ Get user data by id """
        if not (user := User.query.filter_by(id=id).first()):
            return err_resp("User not found!", "user_404", 404)

        from .utils import load_data

        try:
            user_data = load_data(user)

            resp = message(True, "User data sent")
            resp["user"] = user_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def update_user(id, data):
        item = User.query.filter_by(id=id).first()
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
