"""
Unit tests for the Todo Console Application
Tests each module and the full workflow
"""

import pytest
from modules.storage import InMemoryStorage, Task
from modules.tasks import TaskManager
from modules.utils import (
    validate_title, validate_task_id, format_task,
    format_task_detailed, parse_command, is_valid_command
)
from modules.cli import TodoCLI


class TestStorageModule:
    """Test the storage module functionality"""

    def test_add_task(self):
        """Test adding a task"""
        storage = InMemoryStorage()
        task = storage.add_task("Test task", "Test description")

        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False

    def test_get_task(self):
        """Test retrieving a task"""
        storage = InMemoryStorage()
        added_task = storage.add_task("Test task", "Test description")
        retrieved_task = storage.get_task(1)

        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title
        assert retrieved_task.description == added_task.description

    def test_get_all_tasks(self):
        """Test retrieving all tasks"""
        storage = InMemoryStorage()
        storage.add_task("Task 1", "Description 1")
        storage.add_task("Task 2", "Description 2")

        tasks = storage.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"

    def test_update_task(self):
        """Test updating a task"""
        storage = InMemoryStorage()
        task = storage.add_task("Old title", "Old description")

        success = storage.update_task(1, "New title", "New description", True)
        updated_task = storage.get_task(1)

        assert success is True
        assert updated_task.title == "New title"
        assert updated_task.description == "New description"
        assert updated_task.completed is True

    def test_delete_task(self):
        """Test deleting a task"""
        storage = InMemoryStorage()
        storage.add_task("Test task", "Test description")

        success = storage.delete_task(1)
        deleted_task = storage.get_task(1)

        assert success is True
        assert deleted_task is None

    def test_mark_completed(self):
        """Test marking a task as completed"""
        storage = InMemoryStorage()
        task = storage.add_task("Test task", "Test description")

        success = storage.mark_completed(1)
        updated_task = storage.get_task(1)

        assert success is True
        assert updated_task.completed is True

    def test_mark_incomplete(self):
        """Test marking a task as incomplete"""
        storage = InMemoryStorage()
        task = storage.add_task("Test task", "Test description")
        storage.mark_completed(1)  # First mark as complete

        success = storage.mark_incomplete(1)
        updated_task = storage.get_task(1)

        assert success is True
        assert updated_task.completed is False


class TestTasksModule:
    """Test the tasks module functionality"""

    def test_add_task(self):
        """Test adding a task through TaskManager"""
        manager = TaskManager()
        task = manager.add_task("Test task", "Test description")

        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.completed is False

    def test_add_task_empty_title(self):
        """Test adding a task with empty title raises ValueError"""
        manager = TaskManager()

        with pytest.raises(ValueError):
            manager.add_task("", "Test description")

    def test_update_task(self):
        """Test updating a task through TaskManager"""
        manager = TaskManager()
        task = manager.add_task("Old title", "Old description")

        success = manager.update_task(1, "New title", "New description", True)
        updated_task = manager.get_task(1)

        assert success is True
        assert updated_task.title == "New title"
        assert updated_task.description == "New description"
        assert updated_task.completed is True

    def test_delete_task(self):
        """Test deleting a task through TaskManager"""
        manager = TaskManager()
        manager.add_task("Test task", "Test description")

        success = manager.delete_task(1)
        deleted_task = manager.get_task(1)

        assert success is True
        assert deleted_task is None


class TestUtilsModule:
    """Test the utils module functionality"""

    def test_validate_title(self):
        """Test title validation"""
        assert validate_title("Valid title") is True
        assert validate_title("") is False
        assert validate_title("   ") is False
        assert validate_title("  Valid  ") is True

    def test_validate_task_id(self):
        """Test task ID validation"""
        is_valid, parsed_id = validate_task_id("123")
        assert is_valid is True
        assert parsed_id == 123

        is_valid, parsed_id = validate_task_id("-1")
        assert is_valid is False
        assert parsed_id == -1

        is_valid, parsed_id = validate_task_id("abc")
        assert is_valid is False
        assert parsed_id is None

    def test_format_task(self):
        """Test task formatting"""
        task = Task(id=1, title="Test task", completed=False)
        formatted = format_task(task)
        assert "[O] 1. Test task" == formatted

        task.completed = True
        formatted = format_task(task)
        assert "[X] 1. Test task" == formatted

    def test_parse_command(self):
        """Test command parsing"""
        command, args = parse_command('add "Test task" "Test description"')
        assert command == "add"
        assert args == ["Test task", "Test description"]

        command, args = parse_command('list')
        assert command == "list"
        assert args == []

        command, args = parse_command('show 5')
        assert command == "show"
        assert args == ["5"]

    def test_is_valid_command(self):
        """Test command validation"""
        assert is_valid_command("add") is True
        assert is_valid_command("invalid") is False


def test_full_workflow():
    """Test the full workflow through the CLI"""
    cli = TodoCLI()

    # Add a task
    cli.process_command('add "Test task" "Test description"')
    tasks = cli.task_manager.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test task"

    # List tasks
    # (We can't easily test the printed output, but we know the list is correct)

    # Update task
    cli.process_command('update 1 "Updated task" "Updated description"')
    updated_task = cli.task_manager.get_task(1)
    assert updated_task.title == "Updated task"

    # Complete task
    cli.process_command('complete 1')
    completed_task = cli.task_manager.get_task(1)
    assert completed_task.completed is True

    # Incomplete task
    cli.process_command('incomplete 1')
    incomplete_task = cli.task_manager.get_task(1)
    assert incomplete_task.completed is False

    # Show task details
    # (We can't easily test the printed output)

    # Delete task
    cli.process_command('delete 1')
    tasks = cli.task_manager.get_all_tasks()
    assert len(tasks) == 0


if __name__ == "__main__":
    pytest.main([__file__])