from api import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False) 
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return self.name