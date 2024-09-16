from bs4 import BeautifulSoup
import json
import csv

# HTML A JSON
# Función para parsear recursivamente las carpetas y enlaces
def parse_bookmarks(dl, folder_hierarchy=None):
    if folder_hierarchy is None:
        folder_hierarchy = []

    bookmarks = []
    
    # Procesa cada elemento <DT> dentro de la lista <DL>
    for dt in dl.find_all('dt', recursive=False):
        h3 = dt.find('h3')  # Buscar carpeta
        links = dt.find_all('a')  # Buscar todos los enlaces dentro del <DT>

        # Si encontramos una carpeta (etiqueta <H3>), procesamos su contenido
        if h3:
            current_folder = h3.get_text()
            # Añadir la carpeta actual a la jerarquía
            new_folder_hierarchy = folder_hierarchy + [current_folder]
            next_dl = dt.find_next_sibling('dl')
            if next_dl:
                # Llama recursivamente para procesar el contenido de la carpeta
                bookmarks.extend(parse_bookmarks(next_dl, new_folder_hierarchy))  # Usar extend para agregar todos los elementos
        
        # Procesar todos los enlaces encontrados dentro de <DT>
        for link in links:
            bookmarks.append({
                'title': link.get_text(),
                'url': link.get('href'),
                'folder_hierarchy': folder_hierarchy
            })
    
    return bookmarks

# Cargar el archivo HTML de marcadores
with open('bookmarks.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    dl = soup.find('dl')
    
    # Parsear los marcadores
    bookmarks_json = parse_bookmarks(dl)

# Guardar los marcadores en un archivo JSON
with open('bookmarks.json', 'w', encoding='utf-8') as json_file:
    json.dump(bookmarks_json, json_file, indent=2, ensure_ascii=False)

# Mostrar el resultado para verificar
for bookmark in bookmarks_json:
    print(bookmark)

#---------------------------------------------------------------------------------

# JSON A CSV
# Lee el archivo JSON
with open('bookmarks.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Prepara una lista para almacenar las filas CSV
csv_rows = []

# Procesa cada entrada del JSON
for item in data:
    folder_hierarchy = item.get('folder_hierarchy', [])
    
    # Asigna los valores de las carpetas, si existen
    level1 = folder_hierarchy[0] if len(folder_hierarchy) > 0 else ''
    level2 = folder_hierarchy[1] if len(folder_hierarchy) > 1 else ''
    level3 = folder_hierarchy[2] if len(folder_hierarchy) > 2 else ''
    level4 = folder_hierarchy[3] if len(folder_hierarchy) > 3 else ''
    
    # Agrega los datos a csv_rows
    csv_rows.append([
        item['title'],
        item['url'],
        level1,
        level2,
        level3,
        level4
    ])

# Escribe el archivo CSV
with open('bookmarks.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Link', '1', '2', '3', '4'])
    writer.writerows(csv_rows)