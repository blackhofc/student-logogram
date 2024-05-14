
import openpyxl, json
from collections import Counter

COLORS = ['FC4F27', 'A0E686', '00B5FF', 'FE76D9', 'F9DD60']

STYLES = ['cloud_1', 'cloud_2', 'cloud_3', 'birds']

GENDERS = {
    'H': 'Hombre',
    'M': 'Mujer',
    'NB': 'No Binario'
}

def output(filename, data):
    # Write the dictionary to a JSON file
    with open('{}.json'.format(filename), "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


# Create top 4 music genres and others
# Create top 3 sports and others
def createTops(data):
    # Count occurrences of each element in each category
    music_genres_counter = Counter()
    fav_sports_counter = Counter()
    languages_counter = Counter()

    for entry in data:
        music_genres_counter.update(entry["music_genres"])
        fav_sports_counter.update(entry["fav_sports"])
        languages_counter.update(entry["languages"])

    # Create the result JSON with elements ordered by count and assigned colors
    result_json = {
        "genres": {genre: {"count": count, "value": COLORS.pop(0)} if COLORS else {"count": count } for genre, count in music_genres_counter.most_common()},
        "sports": {sport: {"count": count, "value": STYLES.pop(0)} if STYLES else {"count": count } for sport, count in fav_sports_counter.most_common()},
        "languages": {language: {"count": count } for language, count in languages_counter.most_common() }
    }


    output('styles', result_json)



if __name__ == '__main__':
    print('Parsing')
    # Replace 'example.xlsx' with the path to your Excel file
    workbook = openpyxl.load_workbook('data.xlsx')

    # Assuming the first sheet is the one you want to read from
    sheet = workbook.active

    students = []
    indx = 0

    # Access cell values
    for row in sheet.iter_rows(min_row=2, values_only=True):
        indx += 1
        
        if row[1] is None:
            continue
        
        name      = row[0]
        age       = int(row[1])
        gender    = row[2]
        genres    = row[3].split(', ')
        sports    = row[4].split(', ')
        languages = row[5].split(', ')
        
        students.append({
            'id':           indx,
            'name':         name,
            'age':          age,
            'gender':       GENDERS[gender],
            'music_genres': genres,
            'fav_sports':   sports,
            'languages':    [lang for lang in languages if lang !='Español']
        })
    
    createTops(students)
    output('students', students)
    
        