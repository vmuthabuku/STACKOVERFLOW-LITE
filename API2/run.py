import os

from ap.app import app

#config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
#app = create_app()

from manage import migrate
migrate()

if __name__ == '__main__':
    app.run(debug=True)