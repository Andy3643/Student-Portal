
from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Course, User


# app = create_app('development')
app = create_app('production')
manager =  Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('Tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def  add_shell_context():
    return dict(db=db,app=app,User=User,Course=Course)
if __name__== "__main__":
    manager.run()

