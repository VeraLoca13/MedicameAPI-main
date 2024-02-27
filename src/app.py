
from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import VisitaMedica
from routes import Pirula

app = Flask(__name__)

CORS(app)


def page_not_found(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(VisitaMedica.main, url_prefix='/api/visita')
    app.register_blueprint(Pirula.main, url_prefix='/api/visita')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=5000)
