"""Flask server for the Emotion Detection application.

Provides routes to render the user interface and interact with the
EmotionDetection package via an API endpoint.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Iniciar la aplicación Flask
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Retrieves the text from the request arguments, analyzes it for emotions,

    and returns a formatted string response. Handles cases with invalid or
    blank input gracefully by returning an error message.
    """
    # Recuperar el texto a analizar desde los argumentos de la solicitud URL
    text_to_analyze = request.args.get("textToAnalyze")

    # Pasar el texto al paquete interno de análisis y guardar el diccionario
    response = emotion_detector(text_to_analyze)

    # Extraer la emoción dominante para validar el estado de la respuesta
    dominant_emotion = response["dominant_emotion"]

    # Si la emoción dominante es None (debido a una entrada en blanco),
    # se retorna el mensaje de error solicitado por el cliente.
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!."

    # Si la entrada es válida, se extraen de forma segura las puntuaciones
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    # Retornar la cadena de texto con el formato requerido para la interfaz web
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Renders the main application page (HTML user interface)."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
