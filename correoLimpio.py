import re
correos= [
    "enrique509@gmail.com",
    "enrique@gm1ail.com/",
    "enrique@gmail.com / ana@gmail.com",
    "enrique@gmail.com  ana@gmail.com",
    "ejejdhdh3323@pedro.e!s"
]

def limpiarCorreo():
     for correo in correos:
       
        correoBueno = re.findall(r'[\w]+@[a-zA-Z]+\.[\w]+',correo) 
        if len(correoBueno) > 0:
            print(correoBueno[0])
            
        else:
            print("---")
        

limpiarCorreo()










def prueba():
    s = 'Hello, World!!'
    res = re.sub('[.,!]', '', s)
    print(res)
    

#prueba() 

