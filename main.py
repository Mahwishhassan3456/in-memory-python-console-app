"""
Phase I: In-Memory Python Console Todo Application
Main entry point for the application
"""

from modules.cli import TodoCLI


def main():
    """Main entry point of the application"""
    app = TodoCLI()
    app.run()


if __name__ == "__main__":
    main()