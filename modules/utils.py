"""
Utilities module for the Todo Console Application
Contains validation, formatting, and utility functions
"""

import re
from typing import Tuple, Optional
from .storage import Task


def validate_title(title: str) -> bool:
    """
    Validate task title
    Returns True if title is valid, False otherwise
    """
    return bool(title and title.strip())


def validate_task_id(task_id: str) -> Tuple[bool, Optional[int]]:
    """
    Validate task ID
    Returns (is_valid, parsed_id) tuple
    """
    try:
        parsed_id = int(task_id)
        return parsed_id > 0, parsed_id
    except ValueError:
        return False, None


def format_task(task: Task) -> str:
    """
    Format a task for display
    """
    status = "X" if task.completed else "O"
    return f"[{status}] {task.id}. {task.title}"


def format_task_detailed(task: Task) -> str:
    """
    Format a task with detailed information
    """
    status = "Completed" if task.completed else "Pending"
    return (
        f"ID: {task.id}\n"
        f"Title: {task.title}\n"
        f"Description: {task.description or 'No description'}\n"
        f"Status: {status}\n"
        f"Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Updated: {task.updated_at.strftime('%Y-%m-%d %H:%M:%S')}"
    )


def parse_command(user_input: str) -> Tuple[str, list]:
    """
    Parse user command and return (command, args) tuple
    Handles quoted strings properly
    """
    if not user_input.strip():
        return "", []

    parts = user_input.strip().split(maxsplit=1)
    command = parts[0].lower()

    if len(parts) == 1:
        return command, []

    # Parse arguments, considering quoted strings
    args = []
    arg_part = parts[1]
    current_arg = ""
    in_quotes = False
    i = 0

    while i < len(arg_part):
        char = arg_part[i]

        if char == '"' or char == "'":
            in_quotes = not in_quotes
        elif char == ' ' and not in_quotes:
            if current_arg:
                args.append(current_arg)
                current_arg = ""
        else:
            current_arg += char

        i += 1

    if current_arg:
        args.append(current_arg)

    return command, args


def is_valid_command(command: str) -> bool:
    """
    Check if the command is valid
    """
    valid_commands = {
        'add', 'list', 'show', 'update', 'complete', 'incomplete', 'delete', 'help', 'quit', 'exit'
    }
    return command in valid_commands