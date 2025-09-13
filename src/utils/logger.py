import logging
from pathlib import Path

logs_folder = Path(__file__).parent.parent.parent.resolve() / "logs"

# logging.basicConfig(
#     filename=logs_folder / "app.log",
#     encoding="utf-8",
#     level=logging.INFO,
#     format="%(asctime)s - %(lineno)d - %(levelname)s - %(name)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt="%(asctime)s - %(lineno)d - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    )

app_handler = logging.FileHandler(logs_folder / "app.log")
app_handler.setLevel(logging.WARNING)
app_handler.setFormatter(formatter)

error_handler = logging.FileHandler(logs_folder / "errors.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(app_handler)
logger.addHandler(error_handler)