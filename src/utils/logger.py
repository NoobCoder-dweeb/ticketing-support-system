import logging
import logging.config
from pathlib import Path

loggers = "app_logger"

logs_folder = Path(__file__).parent.parent.parent.resolve() / "logs"
logging_config_path = Path(__file__).parent.parent.parent.resolve() / "configs" /"logging.ini"
logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)

logger = logging.getLogger(name=loggers)
# formatter = logging.Formatter(
#     fmt="%(asctime)s:%(lineno)d:%(levelname)s:%(name)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     )

# app_handler = logging.FileHandler(logs_folder / "app.log")
# app_handler.setLevel(logging.WARNING)
# app_handler.setFormatter(formatter)

# error_handler = logging.FileHandler(logs_folder / "errors.log")
# error_handler.setLevel(logging.ERROR)
# error_handler.setFormatter(formatter)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# logger.addHandler(app_handler)
# logger.addHandler(error_handler)

if __name__ == "__main__":
    logger.debug("Info")
    logger.error("Shit Happened")