from flask import Flask
from app.config import db, migrate, configure_app

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    configure_app(app)

    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de blueprints
    from app.routes.person import person_bp
    app.register_blueprint(person_bp, url_prefix='/persons')

    return app
