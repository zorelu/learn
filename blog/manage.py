from blog import app
from models import User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
import config

app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()