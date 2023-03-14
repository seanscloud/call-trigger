import azure.functions as func
import logging
import json
import random
import datetime
import requests

for package in ['requests', 'datetime']:
    install(package)

def main(req: func.HttpRequest, items: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Get a random phone number from the database
    phone_numbers = [item['phone_number'] for item in items]
    random_phone_number = random.choice(phone_numbers)
    for item in items:
        logging.info(f'Phone number: {item["phone_number"]}')

    # Send the random phone number to the API
    output_data = {
        "_links": {},
        "conversationState": "Unknown",
        "positionInQueue": 0,
        "queueName": "Test ACD Queue",
        "queueReporting": "P101",
        "agentName": "Test ACD Group",
        "agentId": "6201",
        "agentReporting": "201",
        "timeOfferedToAgent": datetime.datetime.utcnow().isoformat(),
        "timeOfferedToQueue": datetime.datetime.utcnow().isoformat(),
        "timeOfferedToSystem": datetime.datetime.utcnow().isoformat(),
        "variableData": random_phone_number
    }
    
    api_uri = "https://"
    response = requests.post(api_uri, data=output_json, headers = {'Content-Type': 'application/json'})
    if response.status_code >= 200 and response.status_code < 300:
        result = {'result': 'success'}
    else:
        result = {'result': 'failure'}
    
    return func.HttpResponse(
        json.dumps(result),
        mimetype='application/json'
    )
