def view_tasks():
    if not tasks:
        print("No tasks available")
    for i, task in enumerate(tasks, 1):
        print(i, task)
