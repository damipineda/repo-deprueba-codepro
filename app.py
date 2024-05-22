from flask import Flask, render_template, jsonify, request, session
from conexion import app, db
from models import Pregunta
import random

app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar_juego')
def iniciar_juego():
    session['vidas'] = 3
    return render_template('game.html')

@app.route('/obtener_pregunta')
def obtener_pregunta():
    preguntas = Pregunta.query.all()
    pregunta = random.choice(preguntas)
    opciones = [
        pregunta.respuesta_correcta,
        pregunta.respuesta_incorrecta1,
        pregunta.respuesta_incorrecta2
    ]
    random.shuffle(opciones)
    return jsonify({
        'pregunta': pregunta.pregunta,
        'opciones': opciones,
        'id': pregunta.id
    })

@app.route('/verificar_respuesta', methods=['POST'])
def verificar_respuesta():
    data = request.json
    pregunta = Pregunta.query.get(data['id'])
    correcta = data['respuesta'] == pregunta.respuesta_correcta
    if not correcta:
        session['vidas'] -= 1
    return jsonify({'correcta': correcta, 'vidas': session['vidas']})

@app.route('/game_over')
def game_over():
    return render_template('game_over.html')

if __name__ == '__main__':
    app.run(debug=True)
