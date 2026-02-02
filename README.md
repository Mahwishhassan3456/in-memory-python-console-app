# Todo Console Application (Phase I)

This is the Phase I implementation of the Progressive Todo Application System - a simple in-memory console application written in Python.

## Features

- Add, list, show, update, complete/incomplete, and delete todo items
- In-memory storage (todos are lost when the application exits)
- Command-line interface for easy interaction
- Proper error handling and validation

## Usage

Run the application:

```bash
python todo_console_app.py
```

Once running, you can use the following commands:

- `add <title> [description]` - Add a new todo
- `list` - List all todos
- `show <id>` - Show details of a specific todo
- `update <id> <title> [description]` - Update a todo
- `complete <id>` - Mark a todo as complete
- `incomplete <id>` - Mark a todo as incomplete
- `delete <id>` - Delete a todo
- `help` - Show available commands
- `quit` - Exit the application

## Example Session

```
> add Buy groceries Milk and bread
Added todo: [○] 1. Buy groceries

> add Complete project Write documentation
Added todo: [○] 2. Complete project

> list
Your todos:
  [○] 1. Buy groceries
  [○] 2. Complete project

> complete 1
Todo completed: [✓] 1. Buy groceries

> list
Your todos:
  [✓] 1. Buy groceries
  [○] 2. Complete project

> show 2
ID: 2
Title: Complete project
Description: Write documentation
Status: Pending
```

## Architecture

- `TodoItem`: Represents a single todo item with ID, title, description, and completion status
- `TodoManager`: Handles all business logic for managing todos in memory
- `TodoConsoleApp`: Handles user input/output and command parsing