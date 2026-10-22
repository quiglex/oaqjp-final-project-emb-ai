## Import the requests library to handle HTTP requests
# import requests

# def emotion_detector(text_to_analyze):
#     # URL of the Emotion Prediction service
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     # Set headers required for the API request
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     # JSON dictionary for the text to be analyzed
#     my_json = { "raw_document": { "text": text_to_analyze } }
#     # Send a POST request to the API with the text and headers
#     response = requests.post(url, json=my_json, headers=headers)
#     # Return the response text from the API
#     return response.text

##################################################################
## V2
##################################################################
import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Emotion Prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # JSON dictionary for the text to be analyzed
    my_json = { "raw_document": { "text": text_to_analyze } }
    # Set headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=my_json, headers=headers)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    my_dict = {}
    for a_key in formatted_response['emotionPredictions'][0]['emotion']:
        my_dict[a_key] = formatted_response['emotionPredictions'][0]['emotion'][a_key]

    my_dict['dominant_emotion'] = max(my_dict, key=my_dict.get)

    # Returning a dictionary containing sentiment analysis results
    return my_dict
