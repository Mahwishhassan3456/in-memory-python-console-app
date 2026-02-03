# In-Memory Python Console Application

A menu-driven console application that provides full CRUD operations for managing items with in-memory storage only.

## Features

- **Menu-driven CLI**: Easy-to-use interface with numbered options (1-6)
- **Full CRUD Operations**:
  - Create: Add new items with auto-incrementing IDs
  - Read: List all items or view specific items
  - Update: Modify existing items
  - Delete: Remove items from storage
- **Data Validation**: Proper validation for all inputs
- **Formatted Display**: Clean table-style output for item listings
- **In-Memory Storage**: All data stored in Python data structures (no persistence)

## Architecture

- `main.py`: Application entry point
- `models.py`: Data models (Item class with validation)
- `storage.py`: In-memory storage layer
- `services.py`: Business logic layer
- `cli.py`: Command-line interface
- `demo.py`: Functionality verification script

## Requirements

- Python 3.7+

## Usage

1. Clone the repository
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu options to manage your items

## Demo

To run the demo/test script:
```bash
python demo.py
```

This will demonstrate all CRUD operations and verify functionality.

## License

MIT