import argparse
"""
parse = argparse.ArgumentParser(description="Saludar usuario")
arg = parse.add_argument('--nombre', type=str ,required=True, help="Ingresa un nombre")
args = parse.parse_args()

print(f"buen dia {args.nombre}")"""

from pathlib import Path
from datetime import datetime

"""#define un path
ruta = Path("notas")

#existe ruta? sino la crea
if not ruta.exists():
    ruta.mkdir()

#mostrar archivos en ruta
for archivo in ruta.iterdir():
    print(archivo.name)
"""
"""
parse = argparse.ArgumentParser(description="Notas")
parse.add_argument('--titulo', type=str, required=True, help="Ponele un titulo al archivo")
parse.add_argument('--contenido', type=str, required=True)
args = parse.parse_args()


hoy = datetime.now().strftime("%Y-%m-%d_%H-%M")
titulo = args.titulo.replace(" ","_")
nombre_archivo = f"{titulo}.txt"

ruta = Path("notas")

if not ruta.exists():
    ruta.mkdir()

archivo = ruta / nombre_archivo
archivo.write_text(args.contenido, encoding="utf-8")
"""