"""
In-memory storage module for the Todo Console Application
Handles all data storage using Python lists and dictionaries
"""

from typing import Dict, List
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """Represents a single task in the todo list"""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


class InMemoryStorage:
    """Manages in-memory storage for tasks"""

    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to storage"""
        task = Task(
            id=self._next_id,
            title=title,
            description=description
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """Retrieve a task by ID"""
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: str = None, description: str = None,
                   completed: bool = None) -> bool:
        """Update a task's properties"""
        task = self._tasks.get(task_id)
        if not task:
            return False

        if title is not None:
            task.title = title
            task.updated_at = datetime.now()

        if description is not None:
            task.description = description
            task.updated_at = datetime.now()

        if completed is not None:
            task.completed = completed
            task.updated_at = datetime.now()

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID"""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed"""
        task = self._tasks.get(task_id)
        if task:
            task.completed = True
            task.updated_at = datetime.now()
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete"""
        task = self._tasks.get(task_id)
        if task:
            task.completed = False
            task.updated_at = datetime.now()
            return True
        return False