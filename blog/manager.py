from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from blog import app
from exts import db

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)
###

if __name__=="__mian__":
    manager.run()