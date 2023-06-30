import os

# Lista de nombres de las carpetas
lista_nombres = [
    "GXT5-EBC144VRT2U",
    "Primo 15.0-1",
    "GXT5-EBC48VRT2U",
    "GXT5-EBC288VRT4U",
    "GXT5-EBC192VRT3U",
    "RIVERMAX2",
    "RIVER2",
    "DELTA2",
    "EPOWER-40",
    "2JBO321RNA-HJWX-300",
    "2JBO481CNA-HKWR-300",
    "BPC121031104R",
    "SCC010005000",
    "SCC010010000",
    "SCC010015050R",
    "RCC-03",
    "EL2510",
    "EL2017",
    "SE-1555A",
    "SES-2352",
    "PSC-124000",
    "PSC-12250A",
    "DSR138",
    "PUP1-U-1-6-C-002",
    "SC1339",
    "SE-70MA",
    "SE-2151MA",
    "SE-125A",
    "SE-40MAP",
    "SC1355",
    "SE-1072",
    "SE-1052",
    "SE-82-6",
    "SC1320",
    "FR01236",
    "SE-1010-2",
    "MC-1",
    "SY87829",
    "SC-8020A",
    "SC-1362",
    "SE-6030",
    "SE-8050",
    "SE-2352",
    "SC1325",
    "SE-4020",
    "SE-3000",
    "SC1364",
    "SC1437",
    "SC1324",
    "SC1352",
    "PSW-70300A",
    "PSC-300S",
    "PSC-550S",
    "SC1358",
    "SSC-1000A",
    "SS-210A",
    "DSR127",
    "DSR125",
    "SEM-1562A",
    "SC1306",
    "SE-1275A",
    "SC1340",
    "SC1308",
    "DSR134",
    "SC-1000A",
    "SC-600A",
    "SC1357",
    "520A-PE",
    "CXC-2105",
    "01028 CLIPLIGHT",
    "GES161B105700-N",
    "SCC010030020",
    "SCC010020020",
    "SCC020035000",
    "SCC020050200",
    "BPC240831104R",
    "BPC121531104R",
    "GXT5-EBC72VRT2U",
    "SCC010060200",
    "450041033",
    "3025658",
    "BE01254",
    "LC2400",
    "EL2544",
    "PSJ-2212",
    "DSR114",
    "DSR-141",
    "PSJ-1812",
    "DSR119",
    "SJ1330",
    "SJ1331",
    "DSR115",
    "PSJ-4424",
    "EL9796",
    "SL1312",
    "SL1314",
    "SL1452",
    "EL2467",
    "ITA2-BCI0020K02"]


# Ruta de la carpeta principal donde se crearán las subcarpetas
ruta_principal = "C:/Users/tecnologia/Documents/Productos/Fotos"

# Crear las carpetas
for nombre in lista_nombres:
    # Ruta completa de la carpeta
    ruta_carpeta = os.path.join(ruta_principal, nombre)
    
    # Verificar si la carpeta ya existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Se ha creado la carpeta '{nombre}'")
    else:
        print(f"La carpeta '{nombre}' ya existe")