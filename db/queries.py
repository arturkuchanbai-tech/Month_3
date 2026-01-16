# C-R_U_D
#cerat ,read, update ,delet
task_table = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
"""

#creat 
insert_task = 'INCERT INTO task (task) VALUES (?)'

#read
selecr_task = 'SELECT id, task FROM tasks'

#update
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

#delete
delete_task = 'DELETE FROM tasks WHERE id = ?'