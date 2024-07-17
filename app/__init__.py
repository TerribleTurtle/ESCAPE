from flask import Flask, render_template
from .blueprints.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    @app.route('/')
    def splash_screen():
        return render_template('splash_screen.html')

    #register blueprints here
    app.register_blueprint(auth_bp, url_prefix='/auth')


    return app