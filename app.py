from flask import Flask
from routes import register_blueprints

def create_app():
    """
    Main entry point dari aplikasi Flask.
    Menggunakan arsitektur modular dengan Blueprints.
    """
    app = Flask(__name__)
    register_blueprints(app)
    return app

app = create_app()

if __name__ == "__main__":
    # Menjalankan server aplikasi
    app.run(debug=True, port=5000)
