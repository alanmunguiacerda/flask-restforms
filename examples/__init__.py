import flask

from flask_restforms import FlaskRestForms

app = flask.Flask(__name__)
flask_restforms = FlaskRestForms(app)

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def index():
    return flask.render_template('index.html', method=flask.request.method)
