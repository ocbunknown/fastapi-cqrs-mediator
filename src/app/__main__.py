import logging

import uvicorn

from src.app.main.web import create_app

if __name__ == "__main__":
    uv_config = uvicorn.Config(
        app=create_app,
        log_level=logging.INFO,
        loop="uvloop",
    )

    server = uvicorn.Server(uv_config)
    server.run()
