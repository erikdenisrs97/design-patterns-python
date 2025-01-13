# ToDoList class handle multiple responsabilities
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter a task: ")
        self.add_task(task)

    def remove_task(self):
        task = input("Enter a task to remove: ")
        self.delete_task(task)

# Refactoring:

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        return input("Enter a task: ")

    @staticmethod
    def remove_task():
        return input("Enter a task to remove: ")