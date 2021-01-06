import logging


from flask import Flask, current_app, request
from flask_cors import CORS
from logging.handlers import RotatingFileHandler


def create_app():

    # Setting Flask App
    app = Flask(import_name=__name__)

    # Setting Logging Spec
    logger = logging.getLogger(name=__name__)
    logger.setLevel(level=logging.INFO)
    logger_formatter = logging.Formatter(fmt='[%(asctime)s] %(pathname)s:%(lineno)d %(levelname)s - %(message)s')
    logger_handler = RotatingFileHandler(filename='./application.log',
                                         mode='a',
                                         maxBytes=1024 * 1024 * 5,
                                         backupCount=3,
                                         encoding='utf-8')
    logger_handler.setFormatter(fmt=logger_formatter)
    logger.addHandler(hdlr=logger_handler)

    app.logger.addHandler(hdlr=logger_handler)
    app.logger.setLevel(level=logging.INFO)

    # Setting CORS to App
    CORS(app=app)

    return app


application = create_app()


@application.route(rule="/", methods=["GET"], endpoint="health_check")
def health_check():
    return ""


if __name__ == '__main__':
    application.run(host="127.0.0.1", port=5000, debug=False)