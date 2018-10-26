from blog import app
from models import User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
import config
# app = Flask(__name__)
app.config.from_object(config)
# db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()