#!/usr/bin/env python3
"""
Entry point for the In-Memory Python Console Application.

This application provides a menu-driven CLI interface for managing items
with full CRUD operations. All data is stored in memory only.
"""

from storage import InMemoryStorage
from services import ItemService
from cli import CLIInterface


def main():
    """
    Initialize and run the console application.
    """
    print("Starting In-Memory Python Console Application...")

    # Initialize components
    storage = InMemoryStorage()
    item_service = ItemService(storage)
    cli_interface = CLIInterface(item_service)

    # Run the application
    cli_interface.run()


if __name__ == "__main__":
    main()