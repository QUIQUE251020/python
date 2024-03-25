from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time 

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\esantiago\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Default') #e.g. Profile 3
driver = webdriver.Chrome(options=options)


def main():
    driver.get("https://www.instagram.com/itsquique25/followers")
    driver.implicitly_wait(15)
    desplazamiento()
    recorrer_seguidores()
    follow()
    unfollow()
    almacenamiento()

    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
    
def desplazamiento():
    
    contenedor_principal = driver.find_element(By.CLASS_NAME, "_aano")
    posicion_anterior = 0
    posicion_actual = None

    while True:
        try:
            driver.execute_script("arguments[0].scrollTop += 20000;", contenedor_principal)
            time.sleep(1.4)
            print("deplazando")
            
            # Obtenemos la posición actual después del desplazamiento
            posicion_actual = driver.execute_script("return arguments[0].scrollTop;", contenedor_principal)
            print("Posición actual:", posicion_actual)
            
            print(posicion_actual)
            print(posicion_anterior)
            
        except StaleElementReferenceException:
            print("El elemento se ha vuelto 'caduco', volvamos a buscarlo")
            contenedor_principal = driver.find_element(By.CLASS_NAME, "_aano")

         # Compara la posición actual con la posición anterior
        if posicion_actual == posicion_anterior:
            print("No se pudo hacer más desplazamientos. Llegaste al final.")
            break
        posicion_anterior = posicion_actual
    
   
    
def recorrer_seguidores():
    seguidores = []
    seguidor = driver.find_elements(By.CLASS_NAME,"x1dm5mii")
    
    for elemento in seguidor:
        # Encontrar la etiqueta 'a' dentro de cada elemento x1dm5mii
        enlace = elemento.find_element(By.TAG_NAME,"a")

        # Obtener y mostrar el valor del atributo 'href'
        href = enlace.get_attribute("href")
        href = href.split("/")[3]
        seguidores.append(href)

    return seguidores

def almacenamiento():
    seguidores = recorrer_seguidores()
    with open("seguidoresEnrique.txt","w") as archivo:
        for seguidor in seguidores:
            seguidor=seguidor+"\n"
            archivo.write(seguidor)

def leerSeguidoresAntiguos():
    seguidores_antiguos=[]
    with open("seguidoresEnrique.txt","r") as archivo:
            for linea in archivo:
                seguidor= linea.strip()
                seguidores_antiguos.append(seguidor)
    return seguidores_antiguos

def unfollow():
    seguidores = recorrer_seguidores()
    seguidores_antiguos = leerSeguidoresAntiguos()
    
    for seguidor_antiguo in seguidores_antiguos:
        if seguidor_antiguo.strip() not in seguidores:
            print("Te ha dejado de seguir: ",seguidor_antiguo)
    
def follow():
    seguidores = recorrer_seguidores()
    seguidores_antiguos = leerSeguidoresAntiguos()
    
    for nuevo_seguidor in seguidores:
        if nuevo_seguidor.strip() not in seguidores_antiguos:
            print("Te ha empezado a seguir: ",nuevo_seguidor)

    
        
    
    
if __name__ == "__main__":
    main()