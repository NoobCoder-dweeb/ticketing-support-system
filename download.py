from pathlib import Path
from src.utils.logger import logger
from huggingface_hub import snapshot_download
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from sentence_transformers import SentenceTransformer

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

def setup_vectorstore():
    # setup embedding model
    encoder_name = "all-MiniLM-L6-v2"
    vector_path = Path(__file__).parent.resolve() / "src" / "data" / "chromadb"
    encoder = SentenceTransformer(model_name_or_path=encoder_name)

    try:
        # Setup chroma client
        chroma_client = chromadb.PersistentClient(path=vector_path)
        # chroma_client = chromadb.EphemeralClient()
        current_path = Path(vector_path)
        assert vector_path.exists(), logger.error("Vector store directory does not exist")

        if len(list(current_path.glob("*"))) > 0:
            # remove and create directory
            current_path.rmdir()
            vector_path.mkdir(parents=True, exist_ok=True)

        collection_path = vector_path / "documents"
        collection = chroma_client.get_or_create_collection(name=collection_path.as_posix())
        # setup vector store
        vector_store = ChromaVectorStore(chroma_collection=collection)

        # Create storage context
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        documents = SimpleDirectoryReader(vector_path).load_data()

        # build index and persistence
        index = VectorStoreIndex.from_documents(
            documents=documents,
            storage_context=storage_context,
            embed_model=encoder
        )

        # Query as index
        # query_engine = index.as_query_engine()
        
    except:
        logger.error("Failure to connect to vector store.")

if __name__ == "__main__":
    print("Downloading the model!")
    get_hf_model("0.3")
    setup_vectorstore()
