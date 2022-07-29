from flask import Flask, redirect, render_template, request
from config.config_db import setup_db, db
from config.config_general import setup_general_config
from entities.User import User


app = Flask(__name__)

setup_general_config(app)
setup_db(app)

@app.before_first_request
def init_db():
    db.create_all()


@app.route('/')
def begin():
    return render_template('index.html', users=User.query.order_by(User.id).all())

@app.route('/', methods = ['POST', 'GET'])
def new():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        participation = request.form.get('participation')
        user = User(first_name=first_name, last_name=last_name, participation=participation)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return 'There are in error adding user.'
    else:
        return render_template('index.html', users=User.query.order_by(User.id).all())


if __name__ == '__main__':
    app.run(debug=True)