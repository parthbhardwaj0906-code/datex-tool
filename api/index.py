# If application.py has: app = Flask(__name__)
from application import app

# If application.py only has: application = Flask(__name__)
from application import application as app
