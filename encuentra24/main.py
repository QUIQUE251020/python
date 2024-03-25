from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 
import csv

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\esantiago\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Default') #e.g. Profile 3
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

datos_inmuebles={
    "url":[],
    "Precio":[]
	}
url="https://www.encuentra24.com/panama-es/bienes-raices-venta-de-propiedades-apartamentos?regionslug=prov-panama,panama-oeste&q=f_price.-163000|number.50"

def main():
    driver.get(url)
    driver.implicitly_wait(15)
    primer_anuncio()
    siguiente()
      
    generar_csv(datos_inmuebles)
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
    
def primer_anuncio():
#recorre los 50 anuncios
  for i in range(5,7):
    try:
      driver.implicitly_wait(10)
      anuncio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,f"//*[@id='listingview']/div[3]/div[{i}]"))
      )
      anuncio.click()
      extraer_datos()
      atras()
    except:
      driver.get(url)
      continue
  #va a la siguiente pagina  

def siguiente():
  siguiente = driver.find_element(By.CLASS_NAME,"arrow-next")
  siguiente.click()

def atras():
  siguiente = driver.find_element(By.CLASS_NAME,"d3-detailpager__element--back")
  siguiente.click()


def extraer_datos():
  driver.implicitly_wait(10)
  info_name = driver.find_elements(By.CLASS_NAME,"info-name")
  driver.implicitly_wait(10)
  info_value = driver.find_elements(By.CLASS_NAME,"info-value")
  url = driver.current_url
  short_url = url.split("?")[0]
  
  datos = []
  for name,value in zip(info_name,info_value):
    datos.append((name.text.strip(":"),value.text))
    print(f"{name.text} {value.text}")
    
  almacenar_datos(datos,short_url)
  
    
def almacenar_datos(datos,url):
  for variable,valor in datos:
    print(variable, valor)
    if variable not in datos_inmuebles.keys():
      datos_inmuebles[variable] = []
      datos_inmuebles[variable].append(valor)
    elif variable == "Precio":
      valor_precio= int(valor.split(' ')[0].replace("B/.", "").replace(",", ""))
      datos_inmuebles[variable].append(valor_precio)
    else:
      datos_inmuebles[variable].append(valor)
  datos_inmuebles["url"].append(url)  
  print(datos_inmuebles)
   
def generar_csv(datos):
  
  datos_inmuebles ={}
  nombre_archivo_csv = "datos_inmuebles.csv"
  
  datos_inmuebles.update(datos)

  # Escribir los datos en el archivo CSV
  with open(nombre_archivo_csv, "w", newline="", encoding="utf-8") as archivo_csv:
      escritor_csv = csv.writer(archivo_csv)

      # Escribir la cabecera (nombres de las variables)
      escritor_csv.writerow(datos_inmuebles.keys())

      # Encontrar la longitud máxima de las listas de valores
      longitud_maxima = max(len(valores) for valores in datos_inmuebles.values())

      # Escribir los datos
      for i in range(longitud_maxima):
          fila = [datos_inmuebles[variable][i] if i < len(datos_inmuebles[variable]) else "" for variable in datos_inmuebles.keys()]
          escritor_csv.writerow(fila)

  print(f"Archivo CSV '{nombre_archivo_csv}' creado exitosamente.")

if __name__ == "__main__":
    main()