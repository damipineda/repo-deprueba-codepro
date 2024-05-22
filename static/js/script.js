document.addEventListener('DOMContentLoaded', () => {
    let vidas = 3;

    function obtenerPregunta() {
        fetch('/obtener_pregunta')
        .then(response => response.json())
        .then(data => {
            document.getElementById('pregunta').textContent = data.pregunta;
            const opcionesDiv = document.getElementById('opciones');
            opcionesDiv.innerHTML = '';
            data.opciones.forEach((opcion, index) => {
                const button = document.createElement('button');
                button.textContent = opcion;
                button.className = 'opcion';
                button.id = `boton-${data.id}`; // asignar ID dinámicamente
                button.onclick = () => verificarRespuesta(opcion, data.id, index);
                opcionesDiv.appendChild(button);
            });
            });
    }

    function verificarRespuesta(respuesta, id) {
        //boton respuesta
        const button = document.getElementById(`btn-${id}`);
        fetch('/verificar_respuesta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ respuesta: respuesta, id: id })
        })
            .then(response => response.json())
            .then(data => {
                const button = document.getElementById(`boton-${id}`);
                if (data.correcta) {
                    button.textContent = "Correcto!";
                    button.style.backgroundColor = "green";
                } else {
                    button.textContent = "Incorrecto";
                    button.style.backgroundColor = "red";
                    vidas--;
                    document.getElementById('vidas').textContent = vidas;
                    if (vidas === 0) {
                        window.location.href = '/game_over';
                    }
                }
                 // Esperar 2 segundos antes de pasar a la siguiente pregunta
                setTimeout(obtenerPregunta, 2000);
                //obtenerPregunta();
            });
    }

    obtenerPregunta();
});
