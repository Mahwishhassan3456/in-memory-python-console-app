# Phase I: In-Memory Python Console Todo App

A simple, in-memory console-based todo application implemented in Python. This application allows users to manage their tasks through a command-line interface without any external dependencies.

## Features

- Add new tasks with titles and descriptions
- List all tasks with their completion status
- Show detailed information about a specific task
- Update existing tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Clean, intuitive command-line interface

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application using Python

```bash
python main.py
```

## Usage

Once the application is running, you can use the following commands:

- `add "title" ["description"]` - Add a new task
- `list` - List all tasks
- `show <id>` - Show details of a specific task
- `update <id> "title" ["description"]` - Update a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `delete <id>` - Delete a task
- `help` - Show help information
- `quit` or `exit` - Exit the application

### Examples

```bash
# Add a task
> add "Buy groceries" "Milk, bread, eggs"

# List all tasks
> list

# Show details of task #1
> show 1

# Update task #1
> update 1 "Buy groceries and cook dinner" "Milk, bread, eggs, chicken"

# Mark task #1 as complete
> complete 1

# Delete task #1
> delete 1
```

## Architecture

The application follows a modular design with clear separation of concerns:

- `main.py`: Entry point of the application
- `modules/cli.py`: Command-line interface and user interaction
- `modules/tasks.py`: Business logic for task operations
- `modules/storage.py`: In-memory data storage
- `modules/utils.py`: Utility functions for validation and formatting
- `tests/test_todo.py`: Unit tests for the application

## Running Tests

To run the unit tests:

```bash
python -m pytest tests/test_todo.py -v
```

Or if pytest is available globally:

```bash
pytest tests/test_todo.py -v
```

## Data Persistence

This application stores all data in memory only. When the application exits, all tasks are lost. This is intentional for Phase I to keep the implementation simple and focused on core functionality.

## Contributing

This application was developed as part of a Phase I implementation. Future phases may include persistent storage, web interfaces, and additional features.

## License

This project is open-source and available under the MIT License.