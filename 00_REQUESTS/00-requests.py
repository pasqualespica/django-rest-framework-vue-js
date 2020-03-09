import requests

def main():
    response = requests.get("http://www.google.com")
    # response = requests.get("http://www.google.com/randomaddr")
    print(f"Status code: {response.status_code}")
    # print(f"Headers: {response.headers}")
    print(f"Headers Content-Type: {response.headers['Content-Type']}")
    print(f"Contenuto: {response.text}")


if __name__ == "__main__":
    main()
