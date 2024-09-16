# Convertidor de favoritos en CSV

Este proyecto convierte un archivo de marcadores en formato HTML exportado desde navegadores como Chrome en un archivo CSV, pasando por una estructura intermedia en formato JSON.

## Descripción

Este script realiza las siguientes tareas:

1. **HTML a JSON**: Extrae los marcadores de un archivo HTML (formato Netscape utilizado por navegadores) y los convierte en un archivo JSON estructurado. Mantiene la jerarquía de carpetas en las que se encuentran los marcadores.
2. **JSON a CSV**: Convierte el archivo JSON generado en un archivo CSV. En el CSV, se mantienen las carpetas jerárquicas como columnas separadas para facilitar su manejo.

## Estructura del CSV

El archivo CSV generado tendrá las siguientes columnas:
- `Nombre`: El nombre del marcador.
- `Link`: La URL del marcador.
- `1`, `2`, `3`, `4`: Las carpetas donde está ubicado el marcador. El nivel `1` representa la carpeta principal, y los niveles `2`, `3`, y `4` representan subcarpetas anidadas, si existen. Si no hay más subcarpetas, las columnas estarán vacías.

## Requisitos

- Python 3.x
- Librerías:
  - `BeautifulSoup4` (para parsear HTML)
  - `lxml` (para análisis más eficiente de XML/HTML)
  - `json` (para manejar archivos JSON)
  - `csv` (para generar archivos CSV)
 
  
Para instalar las dependencias necesarias, puedes ejecutar:

```bash
pip install beautifulsoup4 lxml
```

## Uso

### 1. HTML a JSON

1. Exporta tus marcadores desde el navegador como un archivo HTML.
2. Coloca el archivo HTML en la misma carpeta que el script y asegúrate de que se llame `bookmarks.html`.
3. Ejecuta el script. Esto generará un archivo `bookmarks.json` que contiene los marcadores extraídos.

```bash
python html_a_csv.py
```

### 2. JSON a CSV

Una vez generado el archivo `bookmarks.json`, el script también lo convertirá automáticamente en un archivo `bookmarks.csv` con la estructura descrita anteriormente.

### Ejemplo de JSON generado

```json
[
  {
    "title": "Google",
    "url": "https://www.google.com",
    "folder_hierarchy": ["Carpeta Principal", "Subcarpeta"]
  },
  {
    "title": "YouTube",
    "url": "https://www.youtube.com",
    "folder_hierarchy": ["Carpeta Principal"]
  }
]
```

### Ejemplo de CSV generado
| Nombre  | Link                    | 1                 | 2          | 3   | 4   |
|---------|-------------------------|-------------------|------------|-----|-----|
| Google  | https://www.google.com   | Carpeta Principal | Subcarpeta |     |     |
| YouTube | https://www.youtube.com  | Carpeta Principal |            |     |     |


### Contribuciones
Si encuentras algún problema o deseas mejorar este proyecto, siéntete libre de abrir un issue o enviar un pull request.

### Licencia
Este proyecto está bajo la Licencia MIT. Puedes ver más detalles en el archivo LICENSE.
