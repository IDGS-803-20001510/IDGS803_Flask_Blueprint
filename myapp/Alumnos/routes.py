from flask import Blueprint

alumnos=Blueprint('alumno', __name__)

@alumnos.route('/getalumn', methods=['GET'])
def getalum():
    return {'key': 'Alumnos'}