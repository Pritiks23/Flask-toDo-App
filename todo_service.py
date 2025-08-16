from models.todo import Todo

class TodoService:
    def __init__(self):
        self._todos = [
            Todo(1, "Sample Todo 1", "Description 1"),
            Todo(2, "Sample Todo 2", "Description 2")
        ]

    def get_all(self):
        return self._todos

    def get_by_id(self, todo_id):
        for todo in self._todos:
            if todo.todo_id == todo_id:
                return todo
        return None

    def add(self, title, description):
        if self._todos:
            new_id = max(todo.todo_id for todo in self._todos) + 1
        else:
            new_id = 1
        new_todo = Todo(new_id, title, description)
        self._todos.append(new_todo)

    def update(self, todo_id, title, description):
        todo = self.get_by_id(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            return True
        return False

    def delete(self, todo_id):
        todo = self.get_by_id(todo_id)
        if todo:
            self._todos.remove(todo)
            return True
        return False
