from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class Item:
    """
    Represents an item in the console application.

    Attributes:
        id: Unique identifier for the item (auto-incremented)
        title: Title of the item
        description: Description of the item
        created_at: Timestamp when the item was created
    """
    id: int
    title: str
    description: str
    created_at: datetime

    def __post_init__(self):
        """Validate the item after initialization."""
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")

    def to_dict(self) -> dict:
        """Convert the item to a dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }