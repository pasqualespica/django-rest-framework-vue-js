import requests

def client():
    credentials = {"username" : "admin", "password" : "admin"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                        data=credentials)

    print(f"status_code {response.status_code}")
    print(response.json())

def client_get_profile():
    token_h ="Token f056c5ad019b023aec9118cf4c41753342157407"

    headers = {"Authorization" : token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print(f"status_code {response.status_code}")
    print(response.json())
    # senza token la risposta e'
    # status_code 403
    # {'detail': 'Authentication credentials were not provided.'}

if __name__ + "__main__":
    # client()
    client_get_profile()
