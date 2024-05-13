import openpyxl, json, random
from collections import Counter
from random import randint

seedId: int = 0

GENDERS = {
    'H':  'Hombre',
    'M':  'Mujer',
    'NB': 'No Binario'
}

colors = ['F5A800', '57BDBA', 'E52F89', '8122E0']

def output(filename, data):
    # Write the dictionary to a JSON file
    with open('{}.json'.format(filename), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def create_music(values):
    musics = {}
    for key, count in values:
        if key == 'Variado':
            continue

        if len(colors) > 0:
            musics[key] = { 'color': colors.pop() }
        else:
            musics['Otros'] = { 'color': '00A3F5' }
    return musics, musics

def create_seeds(values):
    global seedId
    trans = {}
    seeds = {}
    for key, count in values:
        if key in ['Ninguno']:
            continue
        
        tendrils = []
        
        for i in range(0, randint(3, 10)):
            segments = randint(35, 80)
            
            tendrils.append({
                'distance':  randint(4, 6),
                'size':      randint(30, 70),
                'width':     randint(4, 15),
                'segments':  [random.uniform(-0.1, 0.1) for i in range(0, segments)],
                'angle':     random.uniform(0, 2*3.14158)
            })
        
        disks = []
        
        varCenter = 35
        size       = randint(70, 180)
        radVarDisk = random.uniform(size/4, size);
        
        for i in range(0, randint(70, 150)):
            disks.append({
                'xVar': random.uniform(-varCenter, varCenter),
                'yVar': random.uniform(-varCenter, varCenter),
                'x1':   random.uniform(0, radVarDisk),
                'y1':   random.uniform(0, radVarDisk)
            })
    
        centerVarBlob = 2
        blobLength    = randint(20, 35)
        blobWidth     = randint(30, 60)
        blobCircles   = []
        
        thick     = random.uniform(0, 4)
        thickness = int(round(10 * thick))

        width    = thickness
        widthMax = width
        
        segs = []
        for i in range(0, 100):
            segs.append({
                'i': i,
                'width': randint(-widthMax, widthMax)
            })
            
        for i in range(0, max(20, len(disks)-100)):
            blobCircles.append({
                'xVar':             random.uniform(-centerVarBlob/2, centerVarBlob),
                'yVar':             random.uniform(-centerVarBlob/2, centerVarBlob),
                'randomRad':        random.uniform(-blobWidth, blobWidth),
                'randomAngleStart': random.uniform(0, blobLength/2),
                'randomAngleEnd':   random.uniform(0, blobLength/2),
                'thickness':        thick,
                'segments':         segs
            })
            
        seeds[key] = {
            'id':          seedId,
            'disks':       disks,
            'blobCircles': blobCircles,
            'tendrils':    tendrils
        }
        trans[key] = { 'id': seedId }
        
        seedId+=1
    return seeds, trans

def create_tops(data):
    # Count occurrences of each element in each category
    genders_counter      = Counter()
    music_genres_counter = Counter()
    fav_sports_counter   = Counter()
    languages_counter    = Counter()

    for entry in data:
        genders_counter.update([entry['gender']])
        music_genres_counter.update(entry['music_genres'])
        fav_sports_counter.update(entry['fav_sports'])
        languages_counter.update(entry['languages'])

    gender_seeds    = create_seeds(genders_counter.most_common())
    musics_seeds    = create_music(music_genres_counter.most_common())
    sports_seeds    = create_seeds(fav_sports_counter.most_common())
    languages_seeds = create_seeds(languages_counter.most_common())
    
    result_json = {
        'gender':       gender_seeds[0],
        'fav_sports':   sports_seeds[0],
        'languages':    languages_seeds[0],
    }
    
    translations = {
        'gender':       gender_seeds[1],
        'music_genres': musics_seeds[1],
        'fav_sports':   sports_seeds[1],
        'languages':    languages_seeds[1],
    }

    output('seeds', result_json)
    output('translations', translations)


if __name__ == '__main__':
    workbook = openpyxl.load_workbook('data.xlsx')

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
            'languages':    languages # [lang for lang in languages if lang !='Español']
        })
    
    create_tops(students)
    output('students', students)
    
        