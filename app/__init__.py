from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes import routes
    app.register_blueprint(routes)

    return app


if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)
    app.run(port=5000, debug=True, host='0.0.0.0')
