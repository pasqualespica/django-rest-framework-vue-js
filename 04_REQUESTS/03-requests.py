# https://exchangeratesapi.io/
import requests

def main():
    # response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP")

    prima_valuta = input("Inserisci prima valuta : ")
    seconda_valuta = input("Inserisci seconda valuta : ")

    payload = {'base': prima_valuta, 'symbols': seconda_valuta}
    response = requests.get("https://api.exchangeratesapi.io/latest",
                        params=payload)

    if response.status_code != 200:
        print(f"Status code: {response.status_code}")
        raise Exception("La richiesta API non e' andata a buon fine")

    response_data = response.json()
    tasso_di_cambio = response_data["rates"][seconda_valuta]
    
    print("Data:", response_data["date"])
    print(f" 1 {prima_valuta} corrisponda a {tasso_di_cambio} {seconda_valuta} ")

if __name__ == "__main__":
    main()
