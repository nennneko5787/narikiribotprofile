import os
from typing import Optional

if os.path.isfile(".env"):
    from dotenv import load_dotenv

    load_dotenv()


class EnvironService:
    @classmethod
    def get(cls, key: str) -> Optional[str]:
        return os.getenv(key)
