from typing import Optional
from services import ItemService
from models import Item


class CLIInterface:
    """
    Command-line interface for the console application.
    """

    def __init__(self, item_service: ItemService):
        self.item_service = item_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("           TODO APPLICATION - MAIN MENU")
        print("="*50)
        print("1. Create new item")
        print("2. List all items")
        print("3. Update an item")
        print("4. Delete an item")
        print("5. View item details")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """Get and validate user's menu choice."""
        while True:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            print("Invalid choice. Please enter a number between 1 and 6.")

    def create_item_prompt(self):
        """Prompt user for item creation details."""
        print("\n--- CREATE NEW ITEM ---")
        title = input("Enter title: ").strip()

        if not title:
            print("Error: Title cannot be empty.")
            return

        description = input("Enter description (optional, press Enter to skip): ").strip()

        try:
            item = self.item_service.create_item(title, description)
            print(f"\n✓ Successfully created item!")
            print(f"  ID: {item.id}")
            print(f"  Title: {item.title}")
            print(f"  Description: {item.description}")
            print(f"  Created: {item.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError as e:
            print(f"\n✗ Error creating item: {e}")

    def list_items(self):
        """Display all items in a formatted table."""
        print("\n--- ALL ITEMS ---")
        items = self.item_service.get_all_items()

        if not items:
            print("No items found.")
            return

        print(f"{'ID':<5} {'Title':<20} {'Description':<25} {'Created At':<20}")
        print("-" * 75)

        for item in items:
            title = item.title[:18] + ".." if len(item.title) > 18 else item.title
            description = item.description[:23] + ".." if len(item.description) > 23 else item.description
            created_at = item.created_at.strftime('%Y-%m-%d %H:%M')

            print(f"{item.id:<5} {title:<20} {description:<25} {created_at:<20}")

        print(f"\nTotal items: {len(items)}")

    def update_item_prompt(self):
        """Prompt user for item update details."""
        print("\n--- UPDATE ITEM ---")
        try:
            item_id_str = input("Enter item ID to update: ").strip()
            if not item_id_str:
                print("Item ID cannot be empty.")
                return

            item_id = int(item_id_str)
        except ValueError:
            print("Error: Invalid item ID. Please enter a number.")
            return

        # Check if item exists
        existing_item = self.item_service.get_item(item_id)
        if not existing_item:
            print(f"No item found with ID {item_id}.")
            return

        print(f"\nCurrent item details:")
        print(f"  ID: {existing_item.id}")
        print(f"  Title: {existing_item.title}")
        print(f"  Description: {existing_item.description}")
        print(f"  Created: {existing_item.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

        print("\nEnter new values (press Enter to keep current value):")
        new_title = input(f"  New title (current: '{existing_item.title}'): ").strip()
        new_description = input(f"  New description (current: '{existing_item.description}'): ").strip()

        # If inputs are empty, use None to indicate no change should be made
        title_to_update = new_title if new_title != "" else None
        description_to_update = new_description if new_description != "" else None

        # If both are None, no update is needed
        if title_to_update is None and description_to_update is None:
            print("\nNo changes made.")
            return

        try:
            updated_item = self.item_service.update_item(item_id, title_to_update, description_to_update)
            if updated_item:
                print(f"\n✓ Successfully updated item!")
                print(f"  ID: {updated_item.id}")
                print(f"  Title: {updated_item.title}")
                print(f"  Description: {updated_item.description}")
                print(f"  Created: {updated_item.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"\n✗ Failed to update item with ID {item_id}.")
        except ValueError as e:
            print(f"\n✗ Error updating item: {e}")

    def delete_item_prompt(self):
        """Prompt user for item deletion."""
        print("\n--- DELETE ITEM ---")
        try:
            item_id_str = input("Enter item ID to delete: ").strip()
            if not item_id_str:
                print("Item ID cannot be empty.")
                return

            item_id = int(item_id_str)
        except ValueError:
            print("Error: Invalid item ID. Please enter a number.")
            return

        # Check if item exists
        existing_item = self.item_service.get_item(item_id)
        if not existing_item:
            print(f"No item found with ID {item_id}.")
            return

        print(f"\nItem to delete:")
        print(f"  ID: {existing_item.id}")
        print(f"  Title: {existing_item.title}")
        print(f"  Description: {existing_item.description}")

        confirm = input(f"\nAre you sure you want to delete item {item_id}? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = self.item_service.delete_item(item_id)
            if success:
                print(f"\n✓ Successfully deleted item {item_id}.")
            else:
                print(f"\n✗ Failed to delete item {item_id}.")
        else:
            print("\nDeletion cancelled.")

    def view_item_details(self):
        """View details of a specific item."""
        print("\n--- VIEW ITEM DETAILS ---")
        try:
            item_id_str = input("Enter item ID to view: ").strip()
            if not item_id_str:
                print("Item ID cannot be empty.")
                return

            item_id = int(item_id_str)
        except ValueError:
            print("Error: Invalid item ID. Please enter a number.")
            return

        item = self.item_service.get_item(item_id)
        if not item:
            print(f"No item found with ID {item_id}.")
            return

        print(f"\nItem Details:")
        print(f"  ID: {item.id}")
        print(f"  Title: {item.title}")
        print(f"  Description: {item.description}")
        print(f"  Created: {item.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Age: {self._calculate_age(item.created_at)}")

    def _calculate_age(self, created_at) -> str:
        """Calculate age of an item."""
        from datetime import datetime
        now = datetime.now()
        diff = now - created_at

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if days > 0:
            return f"{days} day{'s' if days != 1 else ''}"
        elif hours > 0:
            return f"{hours} hour{'s' if hours != 1 else ''}"
        else:
            return f"{minutes} minute{'s' if minutes != 1 else ''}"

    def run(self):
        """Run the main application loop."""
        print("Welcome to the In-Memory Python Console Application!")
        print("This application stores all data in memory (no persistence).")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.create_item_prompt()
            elif choice == '2':
                self.list_items()
            elif choice == '3':
                self.update_item_prompt()
            elif choice == '4':
                self.delete_item_prompt()
            elif choice == '5':
                self.view_item_details()
            elif choice == '6':
                print("\nThank you for using the application. Goodbye!")
                break

            # Pause to let user see results before showing menu again
            input("\nPress Enter to continue...")