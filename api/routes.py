from api import api,db
from flask_restful import Resource, reqparse
from .models import Todo
from .serializer import response_serializer
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("description")
parser.add_argument("completed")

class TodoList(Resource):
    def get(self):
        todos = Todo.query.all()
        response = response_serializer(todos)
        return {"data" : response}, 200
    
    def post(self):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        
        data = parser.parse_args()
        data["created_at"] = date
        data["completed"] = bool(data["completed"])
        
        new_data = Todo(**data)
        db.session.add(new_data)
        db.session.commit()
        
        data["created_at"] = str(date)
        
        return {"data" : data}, 201

class TodoAction(Resource):
    def get(self, id):
        todo = Todo.query.get(int(id))
        
        if todo:
            response = response_serializer([todo])
            return {"data" : response[0]}, 200
        else:
            return {"msg": "Not found"}, 404

    def put(self, id):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        data = parser.parse_args()
        
        try:
            todo = Todo.query.get(int(id))
            if todo:
                todo.name = data["name"]
                todo.description = data["description"]
                todo.completed = bool(data["completed"])
                todo.updated_at = date
                
                db.session.commit()
                
                response = response_serializer([todo])
                return {"data" : response[0]}, 200
            else:
                return {"msg": "Not found"}, 404
        except:
            return {"msg": "Invalid data, make sure name of todo unique"}, 404
    
    def delete(self, id):
        todo = Todo.query.get(int(id))
        if todo:
            db.session.delete(todo)
            db.session.commit()
            
            return {"data" : f"Data {todo.name} is deleted!"}, 200
        else:
            return {"msg": "Not found"}, 404


api.add_resource(TodoList, "/todos")
api.add_resource(TodoAction, "/todos/<int:id>")