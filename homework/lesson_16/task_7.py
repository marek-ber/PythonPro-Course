# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() 

# def parse_url(url: str) -> dict:

#     dict_to_return = {}

#     url_split1 = url.split(sep="://", maxsplit=1)
#     dict_to_return.update({'protocol': url_split1[0]})

#     url_split2 = url_split1[1].split(sep="/", maxsplit=1)
#     dict_to_return.update({'path': url_split2[1]})

#     domain_and_port_split = url_split2[0].split(sep=":", maxsplit=1)
#     if len(domain_and_port_split) == 1:
#         dict_to_return.update({'domain': domain_and_port_split[0]})
#     else:
#         dict_to_return.update({'domain': domain_and_port_split[0]})
#         dict_to_return.update({'port': domain_and_port_split[1]})

#     return dict_to_return

# url = "https://api.example.com:8080/users/search?active=true"
# url2 = "https://api.example.com/users/search?active=true"

# print(parse_url(url2))


URL = "https://api.example.com:8080/users/search?active=true"


def parse_url(url: str) -> dict:
    dict_to_return = {}

    parts = url.split(sep="://")
    protocol = parts[0]
    domain_port_path = parts[1]
    dict_to_return.update({'protocol': protocol})

    if ":" in domain_port_path:
        parts2 = domain_port_path.split(sep=":")
        domain = parts2[0]
        port_path = parts2[1]
        dict_to_return.update({'domain': domain})

        parts3 = port_path.split(sep="/", maxsplit=1)
        port = parts3[0]
        path = "/" + parts3[1]
    else:
        parts2 = domain_port_path.split(sep="/", maxsplit=1)
        domain = parts2[0]

        if len(parts2) > 1:
            path = "/" + parts2[1]
        else:
            path = "/"

        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443
        else:
            port = None
    
    dict_to_return.update({'port': int(port), 'path': path})

    return dict_to_return

# print(parse_url(URL))

result = parse_url(URL)

for key, value in result.items():
    print(f"{key}: {value}")
