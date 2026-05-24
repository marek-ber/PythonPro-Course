# Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
# Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
# headers (słownik) i body (string).
# Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
# czytelnej formie, np.:
# --- HTTP Request ---
# Method: GET
# Target: /index.html
# Headers:
# Host: example.com
# User-Agent: PythonClient/1.0
# Body:
# (empty)
# --------------------
# Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi

class HttpRequest:
    def __init__(self, method: str, target: str, headers={}, body=""):
        self.method = method
        self.target = target
        self.headers = headers
        self.body = body

    def display(self):
        return f"""
                --- HTTP Request ---
                Method: {self.method}
                Target: {self.target}
                Headers: 
                    {self.headers}
                Body:
                    {self.body}

    """

get_request = HttpRequest('GET',
                          'api.google.com',
                          {"Accept": "application/json",
                           "User-Agent": "python-script1.0"})

print(get_request.display())