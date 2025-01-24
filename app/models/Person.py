from app.config import db 

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f'<Person {self.name}>'
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
        }
