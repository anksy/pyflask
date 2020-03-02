from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database import db
from run import Serve

# import db models
from database.Category import Category

# instantiate app
app = Serve("config").get_instance()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
