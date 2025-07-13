import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page +=1


#uso do gerador
for product in fetch_products("https://api.exemple.com/products"):
    print(product['name'])

#########################

# outro exemplo de gerador
def meu_gerador(lista: list[int]):
    for i in lista:
        yield i * 2 

for i in meu_gerador(lista=[1, 2, 3]):
    print(i)
