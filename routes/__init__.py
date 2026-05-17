from .main import main_bp
from .aritmatika import aritmatika_bp
from .logika import logika_bp
from .konversi import konversi_bp
from .bonus import bonus_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(aritmatika_bp)
    app.register_blueprint(logika_bp)
    app.register_blueprint(konversi_bp)
    app.register_blueprint(bonus_bp)
