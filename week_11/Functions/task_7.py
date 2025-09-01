#Task 7 : Dynamic To-do List

"""
Manage a temporary to-do list by adding new tasks and updating task statuses.

parameters:
todo_list: Existing dictionary with tasks as keys and their status as values.
new_tasks: Any number of a new tasks to add (status defaults to "pending").
status_updates: Key-value pairs to update the status of existing tasks.
Example:
    todo = {}
    update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")

"""

def update_todo_list(todo_list, *new_tasks, **status_updates):
    todo_list.update({task: "pending" for task in new_tasks})
    todo_list.update(status_updates)
    return todo_list

todos = {}
update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")
print(todos)
print(todos['Read_book']) 
