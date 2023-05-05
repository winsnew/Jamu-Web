from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = 'image'

from views import *