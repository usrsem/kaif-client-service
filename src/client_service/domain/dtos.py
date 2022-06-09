from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Client:
    telegram_id: int
    telegram_username: Optional[str]
    telegram_fullname: str

