import requests

def emotion_detector(text_to_analyze):
    """
    Esta función envía el texto a la API de Watson NLP para detectar emociones.
    Devuelve el texto de respuesta recibido del servicio.
    """
    # URL del servicio Watson NLP para detección de emociones
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Encabezados requeridos por la API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Cuerpo de la solicitud (payload)
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Enviar la solicitud POST
    response = requests.post(url, json=input_json, headers=headers)

    # Devolver el texto de la respuesta
    return response.text
