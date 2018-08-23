import os

from application.app import create_app

config_name = os.getenv('ENVIRONMENT')  # config_name = "development"
app = create_app(config_name)

from managers import migrate
migrate()

if __name__ == '__main__':
    app.run(debug=True)