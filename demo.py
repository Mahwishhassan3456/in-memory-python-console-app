"""
Demo script showing how to use the todo console application
"""
from todo_console_app import TodoConsoleApp

def demo():
    print("This is a demo of the Todo Console Application.")
    print("To run the actual application, execute: python todo_console_app.py")
    print("\nThe application supports these commands:")
    print("- add <title> [description]: Add a new todo")
    print("- list: List all todos")
    print("- show <id>: Show details of a specific todo")
    print("- update <id> <title> [desc]: Update a todo")
    print("- complete <id>: Mark todo as complete")
    print("- incomplete <id>: Mark todo as incomplete")
    print("- delete <id>: Delete a todo")
    print("- quit: Exit the application")
    print("- help: Show help message")

if __name__ == "__main__":
    demo()