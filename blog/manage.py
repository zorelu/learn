from blog import app
from models import User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
import config
#数据库执行脚本 如果是新装要执行1.python manage.py db init 2.python manage.py db migrate 3.更新python manage.py db upgrade
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()