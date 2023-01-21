from .models import Todo

def response_serializer(todos: Todo):
    return [
        {
            "id" : todo.id,
            "name" : todo.name,
            "description": todo.description,
            "completed": todo.completed,
            "create_at": str(todo.created_at),
            "updated_at": str(todo.updated_at)
        } 
        for todo in todos
    ]