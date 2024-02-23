# config                    
from flask import Flask
from . import pets

def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'This is my home page!'

    app.register_blueprint(pets.bp)

    return app
