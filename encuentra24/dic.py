

mi_diccionario = {
    'precio':["B/.120,000","B/.120,000 (rebajado 1%) "]
}

for item in mi_diccionario["precio"]:
  nuevo =int(item.split(' ')[0].replace("B/.", "").replace(",", ""))
  print(nuevo)
