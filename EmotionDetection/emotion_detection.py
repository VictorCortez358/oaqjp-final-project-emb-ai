import json
import requests


def emotion_detector(text_to_analyze):
    """Sends a text snippet to the Watson Emotion Detection API.

    Parses the JSON response on success, or returns a dictionary with None
    values if the server responds with a 400 status code (blank inputs).
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

    # 1. Acceder al atributo status_code para manejar la respuesta del sistema
    if response.status_code == 400:
        # Para status_code = 400, devolvemos el mismo diccionario con valores None
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # 2. Si la respuesta es exitosa (status_code = 200), procesamos normalmente
    formatted_response = json.loads(response.text)

    # Extraer el conjunto de emociones y sus puntuaciones
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Lógica para encontrar la emoción dominante
    emotions_dict = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
# (Asegúrate de dejar una línea en blanco al final del archivo)