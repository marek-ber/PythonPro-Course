# Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host").
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków

def validate_request(request_dict: dict):
    headers = request_dict.get("headers", {})

    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka 'Host'.")
    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka 'User-Agent'")

try:
    validate_request(
        {"headers": {
            "Host": "onet.pl",
            "User-Agent": "Marek-Berny"
        }}
    )
    print("Warunki spełnione")
except ValueError as e:
    print(e)

try:
    validate_request(
        {"headers": {
            "Host": "onet.pl"
        }}
    )
except ValueError as e:
    print(e)