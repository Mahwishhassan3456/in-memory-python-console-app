"""
Simple test script for the todo console application
"""
from todo_console_app import TodoManager, TodoItem

def test_basic_functionality():
    print("Testing basic functionality...")

    # Create a todo manager
    manager = TodoManager()

    # Test adding todos
    print("\n1. Testing add functionality:")
    todo1 = manager.add_todo("Buy milk", "Get 2% milk from the store")
    print(f"Added: {todo1}")

    todo2 = manager.add_todo("Walk the dog", "Don't forget the leash")
    print(f"Added: {todo2}")

    # Test listing todos
    print("\n2. Testing list functionality:")
    todos = manager.list_todos()
    for todo in todos:
        print(f"  {todo}")

    # Test getting a specific todo
    print("\n3. Testing get functionality:")
    retrieved = manager.get_todo(1)
    if retrieved:
        print(f"Retrieved: {retrieved.details()}")

    # Test updating a todo
    print("\n4. Testing update functionality:")
    success = manager.update_todo(1, "Buy almond milk", "Get unsweetened almond milk")
    if success:
        updated = manager.get_todo(1)
        print(f"Updated: {updated}")

    # Test toggling completion
    print("\n5. Testing completion toggle:")
    manager.toggle_completion(1)
    completed = manager.get_todo(1)
    print(f"Toggled: {completed}")

    # Test deleting a todo
    print("\n6. Testing delete functionality:")
    delete_success = manager.delete_todo(2)
    print(f"Deleted todo 2: {delete_success}")

    remaining = manager.list_todos()
    print("Remaining todos:")
    for todo in remaining:
        print(f"  {todo}")

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_basic_functionality()