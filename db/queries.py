# C-R-U-D

task_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
    )
"""

# Create - Insert a new task
insert_task = 'INSERT INTO tasks (task) VALUES (?)'

# Read - Get all tasks
selected_task = 'SELECT id, task FROM tasks'

# Update - Update a task by id
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# Delete - Delete a task by id
delete_task = 'DELETE FROM tasks WHERE id = ?'

