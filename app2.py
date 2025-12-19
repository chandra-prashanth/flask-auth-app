from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

def create_app2():
    app = Flask(__name__,template_folder='./templates1')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO']=False
    app.secret_key = 'SOME KEY'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models1 import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app)

    from routes2 import register_routes1
    register_routes1(app,db,bcrypt)

    migrate = Migrate(app,db)

    return app
