from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pymongo


#2️⃣ Configurar Selenium para obtener la página


# Configurar el driver de Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para no abrir la ventana del navegador
driver = webdriver.Chrome(options=options)

# URL de la página de ESPN con los resultados del america
url = "https://www.espn.com.mx/futbol/equipo/resultados/_/id/227/mex.america"
driver.get(url)

# Obtener el HTML de la página
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Cerrar el navegador
driver.quit()

#3️⃣ Extraer la información de los partidos
matches = []
# Buscar los divs que contienen los resultados
tables = soup.find_all("div", class_="ResponsiveTable Table__results")

for table in tables:
    # Buscar la tabla dentro del div actual
    table_element = table.find("table", class_="Table")
    if table_element:
        tbody = table_element.find("tbody")
        rows = tbody.find_all("tr") if tbody else []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 4:  # Asegurar que la fila tiene suficientes columnas
                fecha = cols[0].text.strip()
                equipo_local = cols[1].text.strip()
                resultado = cols[2].text.strip()
                equipo_visitante = cols[3].text.strip()
                competencia = cols[4].text.strip() if len(cols) > 4 else "Desconocido"

                # Determinar el ganador
                try:
                    goles_local, goles_visitante = map(int, resultado.split("-"))
                    if goles_local > goles_visitante:
                        ganador = equipo_local
                    elif goles_local < goles_visitante:
                        ganador = equipo_visitante
                    else:
                        ganador = "Empate"
                except ValueError:
                    ganador = "Desconocido"

                partido = {
                    "fecha": fecha,
                    "equipo_local": equipo_local,
                    "goles_local": goles_local if 'goles_local' in locals() else None,
                    "goles_visitante": goles_visitante if 'goles_visitante' in locals() else None,
                    "equipo_visitante": equipo_visitante,
                    "competencia": competencia,
                    "ganador": ganador
                }
                matches.append(partido)


#4️⃣ Guardar la información en MongoDB

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb+srv://omar:elrubius24@saludproject.cw3nz.mongodb.net/")
db = client["futbol"]
collection = db["resultados"]

# Insertar los datos
if matches:
    collection.insert_many(matches)
    print("Datos insertados en MongoDB exitosamente.")
else:
    print("No se encontraron datos para insertar.")
