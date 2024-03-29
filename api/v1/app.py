import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_context(exception):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    # Get host and port from environment variables or use default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask app
    app.run(host=host, port=port, threaded=True, debug=True)
