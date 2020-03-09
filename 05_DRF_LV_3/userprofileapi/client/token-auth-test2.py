import requests

def client():
    token_h = "Token 88c3a183197b6a09ceee3df44824e0a497fec5a4"
    # credentials = {"username" : "admin", "password" : "admin"}

    # data = {
    #     "username" : "resttest",
    #     "email" : "test@rest.com",
    #     "password1" : "cambiami123",
    #     "password2" : "cambiami123"
    # }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    headers = {"Authorization" : token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)
                            
    print(f"status_code {response.status_code}")
    print(response.json())

if __name__ + "__main__":
    # client()
    client()
