import os

from flask_migrate import Migrate

from app import create_app, db
# Import models
from app.models.user import User
from utils.encrypt import encrypt

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


@app.after_request
def after_request(response):
    # get the request object somehow
    response.data = encrypt(response.data)
    return response
