import os, requests, uuid, json, config

#You need to create a config.py file and add your Azure keys in that file
subscription_key = config.sentiment_key

# Our Flask route will supply four arguments: input_text, input_language,
# output_text, output_language.
# When the run sentiment analysis button is pressed in our Flask app,
# the Ajax request will grab these values from our web app, and use them
# in the request. See main.js for Ajax calls.

def get_sentiment(input_text, input_language, output_text, output_language):
    base_url = 'https://' + config.region + '.api.cognitive.microsoft.com/text/analytics'
    path = '/v2.0/sentiment'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            },
            {
                'language': output_language,
                'id': '2',
                'text': output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()