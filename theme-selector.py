#!/usr/bin/python3
import os

home_dir = os.path.expanduser("~")
kitty_dir = os.path.join(home_dir, ".config", "kitty")
config_file = os.path.join(kitty_dir, "kitty.conf")
theme_link = os.path.join(kitty_dir, "theme.conf")
themes_dir = os.path.join(kitty_dir, "kitty-themes", "themes")

def check_kitty_config():
    print("Verificando rutas:")
    print("Config File:", config_file)
    print("Theme Link:", theme_link)
    print("Themes Dir:", themes_dir)
    if not os.path.exists(config_file) or not os.path.exists(theme_link) or not os.path.exists(themes_dir):
        print("Falta algún archivo o directorio necesario en la carpeta 'kitty'.")
        return False
    return True

def list_themes():
    # Mostrar los archivos contenidos en la carpeta 'themes'
    themes_files = [file for file in os.listdir(themes_dir) if file.endswith(".conf")]

    print("Temas disponibles:")
    max_columns = 2
    for idx, theme in enumerate(themes_files, start=1):
        print(theme.replace(".conf", ""), end='\t')
        if idx % max_columns == 0:
            print()
    if len(themes_files) % max_columns != 0:
        print('\n \n \n' * (max_columns - len(themes_files) % max_columns - 1))

def link_theme():
    # Solicitar el nombre del tema y enlazarlo con 'themes.conf'
    theme_name = input("\nIngresa el nombre del tema que deseas enlazar: ") + ".conf"

    theme_file = os.path.join(themes_dir, theme_name)

    if not os.path.exists(theme_file):
        print(f"El tema '{theme_name}' no existe en la carpeta 'themes'.")
        return

    # Crear el enlace simbólico
    try:
        os.remove(theme_link)
        os.symlink(theme_file, theme_link)
        print(f"El tema '{theme_name}' ha sido enlazado con éxito.")
        print("Ejecute la combinación de teclas ctrl+shift+f5 para recargar la configuración de kitty...")

    except Exception as e:
        print(f"Error al enlazar el tema: {e}")

if __name__ == "__main__":
    if check_kitty_config():
        list_themes()
        link_theme()
