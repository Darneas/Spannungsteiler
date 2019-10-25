import json
import requests

types = {'publish', 'subscribe', 'unsubscribe', 'subscribed', 'request'}


def send(send_type, payload):
    url = 'http://194.94.239.125:9000/'
    if send_type in types:
        url += send_type
    else:
        raise Exception('Give a valid send type.')

    json_payload = json.dumps(payload)

    headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=json_payload, headers=headers)
    return response


def send_demand(sender, timestamp, value):

    payload={
        "type": "demand_publish",
        "sender": sender,
        "payload": {
            "timestamp": timestamp,
            "demand": value
        } 
    }

    send("publish", payload)

def send_fill_level(sender, timestamp, value):
    payload={
        "type": "fill_level_publish",
        "sender": sender,
        "payload": {
            "timestamp": timestamp,
            "fill_level": value
        }

    }

    send("publish", payload)