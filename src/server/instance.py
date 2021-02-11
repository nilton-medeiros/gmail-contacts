from flask import Flask, redirect, url_for, session
from flask_restplus import Api
from authlib.integrations.flask_client import OAuth
import os
from decouple import config
from datetime import timedelta

# decorador para rotas que devem ser acessíveis apenas por usuários conectados
from auth_decorator import login_required

# dotenv setup
from dotenv import load_dotenv
load_dotenv()

# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

class Server:
    def __init__(self, ):
        self.app = Flask(__name__)
        self.app.secret_key = config("APP_SECRET_KEY")
        self.app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
        self.app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
        self.app.debug = config("DEBUG")
        self.api = Api(
            self.app,
            version='1.0',
            title='Super OrgContact API',
            doc='/docs'
        )

    #

    def run(self, ):
        self.app.run(
            debug=True
        )


server = Server()
