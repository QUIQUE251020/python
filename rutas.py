import os

rutas = [
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010060200',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM470M_800x800',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\GYP150-36',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM540M-72HL4-V',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM545M-72HL4-V',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM395M-6RL3-V',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\AJ-2100-12-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC020050200',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC020035000',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010020020',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010030020',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010015050R',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010010000',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC010005000',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN012351110',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN242120500',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN243020100',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN241800500',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\AJ1000-12-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\AJ 275-12-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\XPC2200-24-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\AJ 500-12-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\XTM 2400-24-01',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PMP243021102',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\450W-CS3W-M',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN123020100',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\GYP100-36',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\VESP-JKM550M-72HL4-V',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM575N-72HL4-V',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN122122500',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\PIN123750500',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\QUA485021100',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC110030210',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC115035210',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\SCC110050210',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\OMNI1500LCDT',
    r'c:\Users\tecnologia\Documents\Productos\Fotos\JKM580N-72HL4-V'
]

nombres_archivos = [os.path.basename(ruta) for ruta in rutas]

print(nombres_archivos)