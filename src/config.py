from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


class AppSettings(BaseModel):
    app_env: str = "development"
    default_visibility: str = "private"
    vector_db_path: Path = PROJECT_ROOT / "data" / "vector_store"


settings = AppSettings()