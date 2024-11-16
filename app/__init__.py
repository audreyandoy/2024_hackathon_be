from flask import Flask
import asyncio
from app.voice import main as voice_main
from dotenv import load_dotenv
import asyncio



def create_app():
    load_dotenv()
    app = Flask(__name__)

    from app.routes import routes
    app.register_blueprint(routes)

    @app.before_first_request
    def start_voice_processing():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        import threading
        voice_thread = threading.Thread(
            target=lambda: loop.run_until_complete(voice_main()),
            daemon=True
        )
        voice_thread.start()

    return app


if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)
    asyncio.run(voice_main())
    app.run(port=5000, debug=True, host='0.0.0.0')
