from flask_login import LoginManager
from .. import app

# ---------------------------------------------------------------------------
# Define and Configure the login manager
# ---------------------------------------------------------------------------

login_manager = LoginManager()
login_manager.login_view = "auth.signin"
login_manager.init_app(app)