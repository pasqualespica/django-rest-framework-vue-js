# https://exchangeratesapi.io/
import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")

    if response.status_code != 200:
        print(f"Status code: {response.status_code}")
        raise Exception("La richiesta API non e' andata a buon fine")
    data = response.json()
    print("JSON data:", data)


if __name__ == "__main__":
    main()
