from app import create_app,db
from flask_script import Manager,Server

app = create_app("development")
manager = Manager(app)



if __name__ == "__main__":
    manager.run()