"""
Tasks module for the Todo Console Application
Handles business logic for task operations
"""

from typing import List, Optional
from .storage import InMemoryStorage, Task


class TaskManager:
    """Manages task operations and business logic"""

    def __init__(self):
        self.storage = InMemoryStorage()

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task"""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        return self.storage.add_task(title.strip(), description.strip())

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID"""
        return self.storage.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.storage.get_all_tasks()

    def update_task(self, task_id: int, title: str = None, description: str = None,
                   completed: bool = None) -> bool:
        """Update a task"""
        if title is not None and title.strip() == "":
            raise ValueError("Task title cannot be empty")

        if title is not None:
            title = title.strip()
        if description is not None:
            description = description.strip()

        return self.storage.update_task(task_id, title, description, completed)

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        return self.storage.delete_task(task_id)

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed"""
        return self.storage.mark_completed(task_id)

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete"""
        return self.storage.mark_incomplete(task_id)

    def get_next_id(self) -> int:
        """Get the next available ID (for UI purposes)"""
        if not self.storage._tasks:
            return 1
        return max(self.storage._tasks.keys()) + 1