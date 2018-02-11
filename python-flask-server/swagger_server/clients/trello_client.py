import requests

def trello_url(model, id):
    return "https://api.trello.com/1/boards/{0}".format(id)

def model_id_put(model, id, key, token):
    url = trello_url(model,id)
    querystring = {
        "key": key,
        "token": token
    }

    response = requests.request("GET", url, params=querystring)

    return response.text
