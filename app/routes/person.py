from flask import Blueprint, request, jsonify
from app.models.Person import Person
from app.config import db

person_bp = Blueprint('person', __name__)

@person_bp.route('/', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    return jsonify([person.serialize() for person in persons])


@person_bp.route('/register', methods=['POST'])
def register_person():
    try:
        data = request.get_json()  # Obtener los datos enviados en formato JSON
        
        # Validar que los datos requeridos están presentes
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')

        if not name or not age or not email:
            return jsonify({'error': 'El nombre, la edad y el correo son requeridos.'}), 400

        # Crear una nueva persona y agregarla a la base de datos
        new_person = Person(name=name, age=age, email=email)
        db.session.add(new_person)
        db.session.commit()

        return jsonify({'message': 'Persona registrada exitosamente.'}), 201
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error: {str(e)}'}), 500