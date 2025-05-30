# Task Tracker CLI

## Project URL: https://github.com/jvinagray/task-tracker-cli
A simple command-line interface (CLI) to manage tasks, built with Python. Tasks are stored in a `tasks.json` file.

## Requirements
- Python 3.6 or higher

## Setup
1. Clone or download the project to your local machine.
2. Navigate to the project directory in Command Prompt:

cd path\to\task\tracker

3. Ensure Python is installed: `python --version`.

## Usage
Run commands using:

python task_cli.py <command> [arguments]</command>


### Commands
- **Add a task**: `python task_cli.py add "Task description"`
  - Example: `python task_cli.py add "Buy groceries"`
- **List tasks**: `python task_cli.py list [status]`
  - Status: `todo`, `in-progress`, `done` (optional)
  - Example: `python task_cli.py list done`
- **Update a task**: `python task_cli.py update <id> "New description"`
  - Example: `python task_cli.py update 1 "Buy groceries and cook dinner"`
- **Delete a task**: `python task_cli.py delete <id>`
  - Example: `python task_cli.py delete 1`
- **Mark as in-progress**: `python task_cli.py mark-in-progress <id>`
  - Example: `python task_cli.py mark-in-progress 1`
- **Mark as done**: `python task_cli.py mark-done <id>`
  - Example: `python task_cli.py mark-done 1`

## Task Properties
Tasks are stored in `tasks.json` with:
- `id`: Unique identifier
- `description`: Task description
- `status`: `todo`, `in-progress`, or `done`
- `createdAt`: Creation timestamp
- `updatedAt`: Last updated timestamp

## Example Workflow
```cmd
python task_cli.py add "Write report"
python task_cli.py list
python task_cli.py mark-in-progress 1
python task_cli.py list in-progress
python task_cli.py mark-done 1
python task_cli.py list done


**Save and Test**:
- Run all commands again to ensure everything works.
- Check `tasks.json` for correctness.
- Read the `README.md` to ensure it’s clear.

### Step 10: Learning Takeaways
- **CLI Parsing**: Using `sys.argv` to handle user input.
- **File I/O**: Reading/writing JSON with `json` and `os`.
- **Error Handling**: Using `try/except` for robust code.
- **Data Structures**: Lists and dictionaries for task management.
- **Modularity**: Breaking code into functions for clarity and reuse.
- **Testing**: Incremental testing ensures each feature works.

### Next Steps
- **Enhancements** (optional, for learning):
  - Add input validation (e.g., prevent empty descriptions).
  - Allow sorting tasks by `createdAt` or `updatedAt`.
  - Add a `clear` command to delete all tasks.
- **Practice**:
  - Try modifying the code to store tasks in a different format (e.g., CSV).
  - Add a feature to list tasks by creation date.
- **Debugging**:
  - If you encounter issues, use `print()` statements to inspect variables or use VSCode’s debugger.
  - Check `tasks.json` manually if file operations fail.

### Questions for You
1. Do you understand each function’s role? Want to dive deeper into any (e.g., JSON handling, argument parsing)?
2. Are there specific features you’re struggling with?
3. Want to try an enhancement (e.g., sorting tasks) to practice more?


Let me know how you’d like to proceed!