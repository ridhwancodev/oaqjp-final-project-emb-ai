import requests

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url=url,headers=headers,json=input_obj)

    if res.status_code==400:
        return{
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response=res.json()

    emotion=formatted_response['emotionPredictions'][0]['emotion']
    max_emotion=max(emotion.values())
    max_list_emotion_index=list(emotion.values()).index(max_emotion)
    list_emotion=list(emotion.keys())
    emotion['dominant_emotion']=list_emotion[max_list_emotion_index]
    return emotion
