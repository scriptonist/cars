from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('configModule.cfg')

from .search.views import search
from .recomendation.views import recomendation
from .compare.views import compare
from .catalog.views import catalog
from .location.views import location


app.register_blueprint(search)
app.register_blueprint(recomendation)
app.register_blueprint(compare)
app.register_blueprint(catalog)
app.register_blueprint(location)


@app.route("/")
def landing():
    return render_template("landing.html", title="home")


@app.route("/home")
def home():
    return render_template("home.html", title="home")


@app.errorhandler(404)
def handle_404_error(e):
    return render_template('404.html'), 404

@app.errorhandler(404)
def handle_500_error(e):
    return render_template('500.html'), 404


@app.route("/test")
def test_components():
    return render_template("test.html", title="test")
