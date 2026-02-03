from typing import Dict, List, Optional
from models import Item


class InMemoryStorage:
    """
    In-memory storage for items using Python data structures.
    """

    def __init__(self):
        self._items: Dict[int, Item] = {}
        self._next_id: int = 1

    def create_item(self, item: Item) -> Item:
        """
        Create a new item in storage with auto-incremented ID.

        Args:
            item: The item to create (ID will be assigned automatically)

        Returns:
            The created item with assigned ID
        """
        item.id = self._next_id
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def get_item(self, item_id: int) -> Optional[Item]:
        """
        Retrieve an item by ID.

        Args:
            item_id: The ID of the item to retrieve

        Returns:
            The item if found, None otherwise
        """
        return self._items.get(item_id)

    def get_all_items(self) -> List[Item]:
        """
        Retrieve all items.

        Returns:
            List of all items
        """
        return list(self._items.values())

    def update_item(self, item_id: int, updated_item: Item) -> Optional[Item]:
        """
        Update an existing item.

        Args:
            item_id: The ID of the item to update
            updated_item: The updated item data

        Returns:
            The updated item if successful, None if item doesn't exist
        """
        if item_id not in self._items:
            return None

        # Preserve the original ID
        updated_item.id = item_id
        self._items[item_id] = updated_item
        return updated_item

    def delete_item(self, item_id: int) -> bool:
        """
        Delete an item by ID.

        Args:
            item_id: The ID of the item to delete

        Returns:
            True if deletion was successful, False if item doesn't exist
        """
        if item_id not in self._items:
            return False

        del self._items[item_id]
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID.

        Returns:
            The next ID that will be assigned
        """
        return self._next_id