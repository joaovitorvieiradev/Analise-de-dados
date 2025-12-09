import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

class Settings:

    def __init__(self):
        
        self.SUPABASE_URL = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY = os.getenv("SUPABASE_KEY")

        if not self.SUPABASE_URL or not self.SUPABASE_KEY:
            raise ValueError("Erro Critico, url ou key da supabase não encontradas, verifique no .env")
        
settings = Settings()