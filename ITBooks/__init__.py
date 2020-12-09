from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key="1kansknkanfkasfsaknfksanfkasnfksafknasni"
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:1851050129@localhost/itbooks?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name='Quản Lý Sách', template_mode='bootstrap4')

login = LoginManager(app=app)