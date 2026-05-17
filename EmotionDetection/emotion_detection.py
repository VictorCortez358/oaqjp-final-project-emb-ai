import json
import requests


def emotion_detector(text_to_analyze):
    """Sends a text snippet to the Watson Emotion Detection API.

    Parses the JSON response to extract individual emotion scores
    and determines the dominant emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    myobj = {"raw_document": {"text": text_to_analyze}}

    # ID Oficial para el entorno de laboratorios de IBM
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Petición HTTP POST a la API de Watson
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # 1. Convertir el texto de respuesta en un diccionario usando la biblioteca json
    formatted_response = json.loads(response.text)

    # 2. Extraer el conjunto requerido de emociones y sus puntuaciones
    # Navegamos por la estructura del JSON devuelto por Watson
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # 3. Lógica para encontrar la emoción dominante (la puntuación más alta)
    # Creamos un diccionario local con las emociones mapeadas
    emotions_dict = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    # La función max() con el argumento key=emotions_dict.get evalúa los valores
    # numéricos de cada clave y devuelve el nombre de la clave con el valor más alto.
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)

    # 4. Modificar la función para devolver el formato de salida requerido
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
