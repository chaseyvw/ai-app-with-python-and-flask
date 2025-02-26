import requests

def emotion_detection(textToAnalyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": textToAnalyze } }

    response = requests.post(url, headers=headers, json=input_json)
    emotion_result = response.json()
    return emotion_result

# Example usage
text = "I love coding!"
emotion_result = emotion_detection(text)
print(emotion_result)
