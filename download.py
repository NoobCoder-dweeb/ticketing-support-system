from pathlib import Path
from src.utils.logger import logger
from huggingface_hub import snapshot_download

model_folder = Path(__file__).parent.resolve() / "src" / "models"
logger.debug(f"Model folder at: {model_folder}")
logger.debug(f"Folder at: {Path.home()}")

def get_hf_model(ver: str):
    mistral_model_path = model_folder / "mistral" / f"7B-Instruct-v{ver}"
    mistral_model_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created Directory at {mistral_model_path}")

    try:
        snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_model_path)
        logger.info(f"Successfully downloaded HuggingFace model")
    except:
        logger.error("Error downloading HuggingFace model")

def main():
    print("Hello from ticketing-support-system!")


if __name__ == "__main__":
    main()
    get_hf_model("0.3")
