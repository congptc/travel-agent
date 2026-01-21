from dataclasses import dataclass
from typing import Optional


@dataclass
class Place:
    name: str
    address: str
    rating: float