import requests
import os
import re


PATH = os.path.dirname(__file__) # el path de la carpeta actual
DOWNLOAD_LIST = os.path.join(PATH, 'modList.txt') # la lista de mods
PATTERN = r'[\w1.12.2-]+=[https://\w.]+' #Filtra solo los mods y sus url


pepe = open(DOWNLOAD_LIST, "r") # abre el archivo xd

# lee la monda esa y aplica el filtro con el regex
mod_list = re.findall(PATTERN, pepe.read())

mod_list = [pepe.split('=') for pepe in mod_list] # ahora los separa por el =
mod_list = {value[0]:value[1] for value in mod_list} # lo pasa a diccionario xd
"""
{
    nombre_del_mod: link_descarga,
    ...
}
"""
os.makedirs('mods')
for mod_name, mod_url in mod_list.items():
    response = requests.get(mod_url)
    file_size = int(response.headers.get('content-length', 0))
    progress_bar = '-' * 20
    
    with open(f'mods/{mod_name}.jar', 'wb') as mod:
        downloaded = 0
        for block in response.iter_content(1024):
            mod.write(block)
            # Actualiza la barrita de progreso
            downloaded += len(block)
            progress = int(downloaded / file_size * 20)
            progress_bar = '-' * progress + ' ' * (20 - progress)
            print(f"\rDescargando {mod_name}: [{progress_bar}] {downloaded}/{file_size} bytes", end="")
        
        print()
    
    print(f"""
        Mod: {mod_name}
        URL: {mod_url}
        """)



pepe.close()