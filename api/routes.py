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
    def get(sefl):
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

api.add_resource(TodoList, "/todos")