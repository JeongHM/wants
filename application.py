import os
import logging

from flask import Flask, current_app, request
from flask_cors import CORS
from logging.handlers import RotatingFileHandler
from utils.decorators import formatting_response
from utils.response_codes import RESPONSE_CODE


def create_app():

    # Setting Flask App
    app = Flask(import_name=__name__)

    # Setting App config
    app.secret_key = os.urandom(16)
    app.config["CORS_HEADERS"] = "Content-Type"

    # Setting SqlAlchemy Config
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}?charset=utf8"

    # Setting Logging Spec
    logger = logging.getLogger(name=__name__)
    logger.setLevel(level=logging.INFO)
    logger_formatter = logging.Formatter(fmt="[%(asctime)s] %(pathname)s:%(lineno)d %(levelname)s - %(message)s")
    logger_handler = RotatingFileHandler(filename="./application.log",
                                         mode="a",
                                         maxBytes=1024 * 1024 * 5,
                                         backupCount=3,
                                         encoding="utf-8")
    logger_handler.setFormatter(fmt=logger_formatter)
    logger.addHandler(hdlr=logger_handler)

    app.logger.addHandler(hdlr=logger_handler)
    app.logger.setLevel(level=logging.INFO)

    # Setting CORS to App
    CORS(app=app)

    # Setting Blueprint (Controller)
    from controllers.company import company_blueprint
    app.register_blueprint(blueprint=company_blueprint, url_prefix="/company")

    # Protect Package Conflict
    # Setting SqlAlchemy ORM
    with app.app_context():
        from models import db
        db.init_app(app=app)
        db.create_all()

    return app


application = create_app()


@application.route(rule="/", methods=["GET"], endpoint="health_check")
@formatting_response
def health_check():
    return RESPONSE_CODE["SUCCESS"], None, 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=False)