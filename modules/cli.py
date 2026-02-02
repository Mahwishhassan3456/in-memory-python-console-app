"""
CLI module for the Todo Console Application
Handles user interface and command processing
"""

from typing import Optional
from .tasks import TaskManager
from .utils import (
    validate_title, validate_task_id, format_task, format_task_detailed,
    parse_command, is_valid_command
)


class TodoCLI:
    """Command Line Interface for the Todo Application"""

    def __init__(self):
        self.task_manager = TaskManager()
        self.running = True

    def display_help(self):
        """Display help information"""
        help_text = """
Available Commands:
  add "title" ["description"]    - Add a new task
  list                          - List all tasks
  show <id>                     - Show details of a specific task
  update <id> "title" ["desc"]  - Update a task
  complete <id>                 - Mark task as complete
  incomplete <id>               - Mark task as incomplete
  delete <id>                   - Delete a task
  help                          - Show this help message
  quit/exit                     - Exit the application
        """
        print(help_text)

    def handle_add(self, args: list):
        """Handle add command"""
        if len(args) < 1:
            print("Error: Please provide a title for the task")
            print("Usage: add \"title\" [\"description\"]")
            return

        title = args[0]
        description = args[1] if len(args) > 1 else ""

        if not validate_title(title):
            print("Error: Task title cannot be empty")
            return

        try:
            task = self.task_manager.add_task(title, description)
            print(f"Added task: {format_task(task)}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_list(self, args: list):
        """Handle list command"""
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nYour tasks:")
        for task in tasks:
            print(f"  {format_task(task)}")

    def handle_show(self, args: list):
        """Handle show command"""
        if len(args) != 1:
            print("Error: Please provide a task ID")
            print("Usage: show <id>")
            return

        is_valid, task_id = validate_task_id(args[0])
        if not is_valid:
            print("Error: Task ID must be a positive integer")
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        print(f"\n{format_task_detailed(task)}")

    def handle_update(self, args: list):
        """Handle update command"""
        if len(args) < 2:
            print("Error: Please provide task ID and new title")
            print("Usage: update <id> \"title\" [\"description\"]")
            return

        is_valid, task_id = validate_task_id(args[0])
        if not is_valid:
            print("Error: Task ID must be a positive integer")
            return

        title = args[1]
        description = args[2] if len(args) > 2 else ""

        if not validate_title(title):
            print("Error: Task title cannot be empty")
            return

        success = self.task_manager.update_task(task_id, title, description)
        if success:
            task = self.task_manager.get_task(task_id)
            print(f"Updated task: {format_task(task)}")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_complete(self, args: list, completed: bool = True):
        """Handle complete/incomplete commands"""
        if len(args) != 1:
            print(f"Error: Please provide a task ID to {'complete' if completed else 'mark as incomplete'}")
            print(f"Usage: {'complete' if completed else 'incomplete'} <id>")
            return

        is_valid, task_id = validate_task_id(args[0])
        if not is_valid:
            print("Error: Task ID must be a positive integer")
            return

        action = self.task_manager.mark_completed if completed else self.task_manager.mark_incomplete
        success = action(task_id)

        if success:
            task = self.task_manager.get_task(task_id)
            status = "completed" if completed else "marked as incomplete"
            print(f"Task {status}: {format_task(task)}")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_delete(self, args: list):
        """Handle delete command"""
        if len(args) != 1:
            print("Error: Please provide a task ID to delete")
            print("Usage: delete <id>")
            return

        is_valid, task_id = validate_task_id(args[0])
        if not is_valid:
            print("Error: Task ID must be a positive integer")
            return

        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"Deleted task with ID {task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def process_command(self, user_input: str):
        """Process a single command from user input"""
        command, args = parse_command(user_input)

        if command in ['', ' ']:
            return  # Empty command, just return

        if not is_valid_command(command):
            print(f"Unknown command: {command}. Type 'help' for available commands.")
            return

        if command == 'help':
            self.display_help()
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
        elif command in ['quit', 'exit']:
            print("Goodbye!")
            self.running = False

    def run(self):
        """Main CLI loop"""
        print("Welcome to the Todo Console Application!")
        print("Type 'help' for available commands or 'quit' to exit.")

        while self.running:
            try:
                user_input = input("\n> ").strip()
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break