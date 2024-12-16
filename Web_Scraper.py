import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página a scrape
URL = "https://www.escueladirecta.com/"  # Cambia esto a la página que quieras scrape

# Encabezado para simular un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Hacer la solicitud HTTP a la página
response = requests.get(URL)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar los elementos que contienen los datos (ajustar según la página)
    articles = soup.find_all('article')  # Cambia 'article' según el HTML de la página

    # Crear listas para almacenar los datos
    titles = []
    links = []

    # Extraer títulos y enlaces
    for article in articles:
        title = article.find('h2').get_text(strip=True)  # Cambia 'h2' según el HTML de la página
        link = article.find('a')['href']

        titles.append(title)
        links.append(link)

    # Crear un DataFrame con los datos
    data = pd.DataFrame({
        'Title': titles,
        'Link': links
    })

    # Guardar los datos en un archivo CSV
    data.to_csv('scraped_data.csv', index=False, encoding='utf-8')
    print("Datos extraídos y guardados en 'scraped_data.csv'.")

else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")