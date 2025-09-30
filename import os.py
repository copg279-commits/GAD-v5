import os
import re

def modificar_html(archivo_entrada, archivo_salida):
    """
    Modifica un archivo HTML para eliminar la cabecera, el pie de página
    y la fila de botones de navegación.
    """
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Usar expresiones regulares para eliminar bloques completos
        # 1. Eliminar la cabecera
        contenido_modificado = re.sub(
            r'<header[^>]*>.*?<\/header>',
            '',
            contenido,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # 2. Eliminar el pie de página
        contenido_modificado = re.sub(
            r'<footer[^>]*>.*?<\/footer>',
            '',
            contenido_modificado,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # 3. Eliminar la fila de botones de navegación
        contenido_modificado = re.sub(
            r'<div class="navigation-buttons-row"[^>]*>.*?<\/div>',
            '',
            contenido_modificado,
            flags=re.DOTALL | re.IGNORECASE
        )

        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(contenido_modificado)
        
        print(f"Archivo modificado con éxito: {archivo_salida}")

    except Exception as e:
        print(f"Error al procesar el archivo {archivo_entrada}: {e}")

if __name__ == "__main__":
    # La carpeta donde están tus archivos HTML originales
    carpeta_entrada = "archivos_originales"
    # La carpeta donde se guardarán los archivos modificados
    carpeta_salida = "archivos_modificados"

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    for nombre_archivo in os.listdir(carpeta_entrada):
        if nombre_archivo.endswith(".html"):
            ruta_entrada = os.path.join(carpeta_entrada, nombre_archivo)
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
            modificar_html(ruta_entrada, ruta_salida)