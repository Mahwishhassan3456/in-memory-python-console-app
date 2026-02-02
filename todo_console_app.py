"""
Phase I: In-Memory Console Todo Application
Simple CLI-based todo manager with in-memory storage
"""

import sys
from typing import Dict, List, Optional


class TodoItem:
    """Represents a single todo item"""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}. {self.title}"

    def details(self):
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {status}"


class TodoManager:
    """Manages the collection of todo items in memory"""

    def __init__(self):
        self.todos: Dict[int, TodoItem] = {}
        self.next_id = 1

    def add_todo(self, title: str, description: str = "") -> TodoItem:
        """Add a new todo item"""
        if not title.strip():
            raise ValueError("Todo title cannot be empty")

        todo = TodoItem(self.next_id, title.strip(), description.strip())
        self.todos[self.next_id] = todo
        self.next_id += 1
        return todo

    def get_todo(self, todo_id: int) -> Optional[TodoItem]:
        """Get a todo by ID"""
        return self.todos.get(todo_id)

    def list_todos(self) -> List[TodoItem]:
        """Get all todos"""
        return list(self.todos.values())

    def update_todo(self, todo_id: int, title: Optional[str] = None,
                   description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        """Update a todo item"""
        if todo_id not in self.todos:
            return False

        todo = self.todos[todo_id]
        if title is not None:
            todo.title = title.strip()
        if description is not None:
            todo.description = description.strip()
        if completed is not None:
            todo.completed = completed

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item"""
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False

    def toggle_completion(self, todo_id: int) -> bool:
        """Toggle the completion status of a todo"""
        if todo_id not in self.todos:
            return False

        self.todos[todo_id].completed = not self.todos[todo_id].completed
        return True

    def get_next_id(self) -> int:
        """Get the next available ID"""
        return self.next_id


class TodoConsoleApp:
    """Console application for managing todos"""

    def __init__(self):
        self.manager = TodoManager()

    def print_help(self):
        """Print available commands"""
        print("\nAvailable commands:")
        print("  add <title> [description]    - Add a new todo")
        print("  list                         - List all todos")
        print("  show <id>                    - Show details of a specific todo")
        print("  update <id> <title> [desc]   - Update a todo")
        print("  complete <id>                - Mark todo as complete")
        print("  incomplete <id>              - Mark todo as incomplete")
        print("  delete <id>                  - Delete a todo")
        print("  quit                         - Exit the application")
        print("  help                         - Show this help message")

    def parse_command(self, user_input: str) -> tuple:
        """Parse user command and return (command, args)"""
        parts = user_input.strip().split(' ', 1)
        command = parts[0].lower() if parts else ""

        if len(parts) > 1:
            # Split the remaining part by space, but keep quoted strings together
            args_parts = []
            current_arg = ""
            in_quotes = False

            for char in parts[1]:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ' ' and not in_quotes:
                    if current_arg:
                        args_parts.append(current_arg)
                        current_arg = ""
                else:
                    current_arg += char

            if current_arg:
                args_parts.append(current_arg)

            args = args_parts
        else:
            args = []

        return command, args

    def handle_add(self, args: List[str]):
        """Handle add command"""
        if len(args) < 1:
            print("Error: Please provide a title for the todo")
            return

        title = args[0]
        description = ' '.join(args[1:]) if len(args) > 1 else ""

        try:
            todo = self.manager.add_todo(title, description)
            print(f"Added todo: {todo}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_list(self, args: List[str]):
        """Handle list command"""
        todos = self.manager.list_todos()

        if not todos:
            print("\nNo todos found.")
            return

        print("\nYour todos:")
        for todo in todos:
            print(f"  {todo}")

    def handle_show(self, args: List[str]):
        """Handle show command"""
        if len(args) != 1:
            print("Error: Please provide a todo ID")
            return

        try:
            todo_id = int(args[0])
        except ValueError:
            print("Error: ID must be a number")
            return

        todo = self.manager.get_todo(todo_id)
        if todo is None:
            print(f"Error: Todo with ID {todo_id} not found")
            return

        print(f"\n{todo.details()}")

    def handle_update(self, args: List[str]):
        """Handle update command"""
        if len(args) < 2:
            print("Error: Please provide ID and new title")
            return

        try:
            todo_id = int(args[0])
        except ValueError:
            print("Error: ID must be a number")
            return

        title = args[1]
        description = ' '.join(args[2:]) if len(args) > 2 else ""

        if self.manager.update_todo(todo_id, title, description if description else None):
            todo = self.manager.get_todo(todo_id)
            print(f"Updated todo: {todo}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_complete(self, args: List[str], completed=True):
        """Handle complete/incomplete commands"""
        if len(args) != 1:
            print(f"Error: Please provide a todo ID to {'complete' if completed else 'mark as incomplete'}")
            return

        try:
            todo_id = int(args[0])
        except ValueError:
            print("Error: ID must be a number")
            return

        if self.manager.toggle_completion(todo_id):
            status = "completed" if completed else "marked as incomplete"
            todo = self.manager.get_todo(todo_id)
            print(f"Todo {status}: {todo}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_delete(self, args: List[str]):
        """Handle delete command"""
        if len(args) != 1:
            print("Error: Please provide a todo ID to delete")
            return

        try:
            todo_id = int(args[0])
        except ValueError:
            print("Error: ID must be a number")
            return

        if self.manager.delete_todo(todo_id):
            print(f"Deleted todo with ID {todo_id}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def run(self):
        """Main application loop"""
        print("Welcome to the Todo Console Application!")
        print("Type 'help' for available commands or 'quit' to exit.\n")

        while True:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                command, args = self.parse_command(user_input)

                if command in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self.print_help()
                elif command == 'add':
                    self.handle_add(args)
                elif command == 'list':
                    self.handle_list(args)
                elif command == 'show':
                    self.handle_show(args)
                elif command == 'update':
                    self.handle_update(args)
                elif command == 'complete':
                    self.handle_complete(args, completed=True)
                elif command == 'incomplete':
                    self.handle_complete(args, completed=False)
                elif command == 'delete':
                    self.handle_delete(args)
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def main():
    """Entry point of the application"""
    app = TodoConsoleApp()
    app.run()


if __name__ == "__main__":
    main()