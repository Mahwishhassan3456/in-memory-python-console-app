from datetime import datetime
from typing import List, Optional
from models import Item
from storage import InMemoryStorage


class ItemService:
    """
    Service layer containing business logic for item operations.
    """

    def __init__(self, storage: InMemoryStorage):
        self.storage = storage

    def create_item(self, title: str, description: str) -> Item:
        """
        Create a new item with validation.

        Args:
            title: Title of the item
            description: Description of the item

        Returns:
            The created item

        Raises:
            ValueError: If title is invalid
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        item = Item(
            id=0,  # Will be assigned by storage
            title=title.strip(),
            description=description.strip() if description else "",
            created_at=datetime.now()
        )
        return self.storage.create_item(item)

    def get_item(self, item_id: int) -> Optional[Item]:
        """
        Get an item by ID.

        Args:
            item_id: ID of the item to retrieve

        Returns:
            The item if found, None otherwise
        """
        return self.storage.get_item(item_id)

    def get_all_items(self) -> List[Item]:
        """
        Get all items.

        Returns:
            List of all items
        """
        return self.storage.get_all_items()

    def update_item(self, item_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Item]:
        """
        Update an item.

        Args:
            item_id: ID of the item to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            Updated item if successful, None if item doesn't exist
        """
        existing_item = self.storage.get_item(item_id)
        if not existing_item:
            return None

        # Use existing values if new values are not provided
        new_title = title if title is not None else existing_item.title
        new_description = description if description is not None else existing_item.description

        updated_item = Item(
            id=item_id,
            title=new_title.strip() if new_title else "",
            description=new_description.strip() if new_description else "",
            created_at=existing_item.created_at  # Preserve original creation time
        )

        return self.storage.update_item(item_id, updated_item)

    def delete_item(self, item_id: int) -> bool:
        """
        Delete an item by ID.

        Args:
            item_id: ID of the item to delete

        Returns:
            True if deletion was successful, False if item doesn't exist
        """
        return self.storage.delete_item(item_id)