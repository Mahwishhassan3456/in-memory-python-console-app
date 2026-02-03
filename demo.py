#!/usr/bin/env python3
"""
Demo script for the In-Memory Python Console Application
Demonstrates all CRUD operations
"""

from storage import InMemoryStorage
from services import ItemService
from datetime import datetime


def demo_crud_operations():
    print("DEMO: In-Memory Python Console Application")
    print("=" * 50)

    # Initialize the service
    storage = InMemoryStorage()
    service = ItemService(storage)

    # CREATE operations
    print("\n1. CREATE OPERATIONS")
    print("-" * 20)

    item1 = service.create_item("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"+ Created item: ID={item1.id}, Title='{item1.title}', Description='{item1.description}'")

    item2 = service.create_item("Complete project", "Finish the Python console app")
    print(f"+ Created item: ID={item2.id}, Title='{item2.title}', Description='{item2.description}'")

    item3 = service.create_item("Call dentist", "")
    print(f"+ Created item: ID={item3.id}, Title='{item3.title}', Description='{item3.description}'")

    # READ operations
    print("\n2. READ OPERATIONS")
    print("-" * 20)

    all_items = service.get_all_items()
    print(f"+ Total items retrieved: {len(all_items)}")

    for item in all_items:
        print(f"  - ID: {item.id}, Title: '{item.title}', Description: '{item.description}', Created: {item.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    # READ single item
    print(f"\n+ Retrieving specific item (ID={item1.id}):")
    specific_item = service.get_item(item1.id)
    if specific_item:
        print(f"  Found: ID={specific_item.id}, Title='{specific_item.title}', Description='{specific_item.description}'")

    # UPDATE operation
    print("\n3. UPDATE OPERATION")
    print("-" * 20)

    updated_item = service.update_item(item2.id, "Complete project urgently", "Finish the Python console app by EOD")
    if updated_item:
        print(f"+ Updated item: ID={updated_item.id}, Title='{updated_item.title}', Description='{updated_item.description}'")

    # Verify the update worked
    print("+ Verifying update:")
    updated_verification = service.get_item(item2.id)
    print(f"  After update: ID={updated_verification.id}, Title='{updated_verification.title}', Description='{updated_verification.description}'")

    # DELETE operation
    print("\n4. DELETE OPERATION")
    print("-" * 20)

    print(f"+ Deleting item with ID={item3.id}")
    delete_success = service.delete_item(item3.id)
    print(f"  Deletion result: {delete_success}")

    # Verify deletion
    all_after_delete = service.get_all_items()
    print(f"+ Items remaining after deletion: {len(all_after_delete)}")
    for item in all_after_delete:
        print(f"  - ID: {item.id}, Title: '{item.title}'")

    # ATTEMPT TO GET DELETED ITEM
    print(f"\n+ Attempting to retrieve deleted item (ID={item3.id}):")
    deleted_item = service.get_item(item3.id)
    print(f"  Result: {deleted_item}")  # Should be None

    print("\n" + "=" * 50)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("All CRUD operations (Create, Read, Update, Delete) are working correctly.")


if __name__ == "__main__":
    demo_crud_operations()