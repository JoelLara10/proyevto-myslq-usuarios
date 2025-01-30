from app import create_app, db
from app.models.Person import Person

app = create_app()

with app.app_context():  # Asegúrate de que el contexto de la aplicación esté disponible.
    if not Person.query.filter_by(email='joeel12@gmail.com').first():
        default_person = Person(name='Joeeel', age=21, email='joeel12@gmail.com')
        db.session.add(default_person)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
