from flask.ext.script import Manager, Shell, Server
from ocrmaven import app


def make_shell_context():
    return dict(app=app)

manager = Manager(app)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == "__main__":
    manager.run()
