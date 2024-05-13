import json, math, copy
from PIL import Image, ImageDraw
from utils.tendril import Tendril
from utils.circularStroke import CircularStroke
from random import randint

ANGLES = {
    'GENDER':   90,
    'LANGUAGE': [45, 0, 315],
    'SPORTS':   [135, 180, 225 ],
}

    
def make_disks(draw, center, rad, angle, disks, tendrils):

	for disk in disks:
		xVar = center[0] + disk['xVar']
		yVar = center[1] + disk['yVar']

		x0 = xVar + rad * math.cos(angle)
		y0 = yVar + rad * math.sin(angle)

		x1 = x0 + disk['x1']
		y1 = y0 + disk['y1']
  
		# print(xVar, yVar, x1, y1) # This function will be genrated randomly only once when i give a language

		draw.ellipse([(x0, y0), (x1, y1)], fill = (0, 0, 0)) 
  
  
	for t in tendrils:
		tendril = Tendril(x=x0, y=y0, width=t['width'], angle=t['angle'])
		tendril.create(distance=t['distance'], curl=10.0, vSegments=t['segments'])
		tendril.draw(draw)
			


def logogram(symbols, imgSize, varThickness, varCenter, nmbCirc, varRad, student):
	
	print(imgSize, varThickness, varCenter, nmbCirc, varRad)
	image = Image.new("RGBA", imgSize, (255, 255, 255, 0))
	x = image.width/2
	y = x

	draw = ImageDraw.Draw(image)
	rad = imgSize[0]/3
	
	stroke = CircularStroke(nmbCirc, (x,y), varCenter, varThickness, rad, varRad)
 
	# Circle Angle
	angle = 90
 
	v = randint(0, 45) # randint(0, 360) this is based on AGEEE the cut of the circle

	# Draw cirlce
	stroke.draw(draw, angle, v) 

	for symb in symbols:
		print(symbols[symb]['angle'])
		
		increaser:int = 1
		# Its genre symbol
		if symbols[symb]['angle'] == 0:
			age:int = student['age']
			increaser=age

		disks      = symbols[symb]['seed']['disks'] # Lines out of sign
		tendrils   = symbols[symb]['seed']['tendrils']	
  
		blobCircles  = symbols[symb]['seed']['blobCircles'] # Size

		make_disks(draw, (x,y), rad, symbols[symb]['angle'] * (math.pi / 180), disks, tendrils)
	
		stroke.drawCircleBlob(draw=draw, angle=symbols[symb]['angle'], blobCircles=blobCircles)
		
	return image

def read(filename: str):

    with open('{}.json'.format(filename), 'r', encoding='utf-8') as file:
        # Load JSON data from the file
        return json.load(file)

def process_category(category, angles, seeds):
    symbols = {}

    if len(angles) > 0 and category in seeds:
        symbols[category] = {
            'angle': -angles.pop(),
            'seed': seeds[category]
        }
    return symbols

def process_student(student, angles, seeds):
    print(angles)

    symbols = { 'genre': { 'angle': -angles['GENDER'], 'seed': seeds['gender'][student['gender']] } }

    categories = {
        'fav_sports':   'SPORTS',
        'languages':    'LANGUAGE'
    }

    #categories = {}
    for key, value in categories.items():
        for item in student[key]:
            symbols.update(process_category(item, angles[value], seeds[key]))
    return symbols


if __name__ == '__main__':
	students = read(filename='students')
	seeds    = read(filename='seeds')
	
	for student in students:
		print(student['name'])

		ANG = copy.deepcopy(ANGLES)
		symbols = process_student(student, ANG, seeds)
	
		image = logogram(symbols, (2048, 2048), 10, 10, 100, (1, 1), student)
		#image.show()
		image.resize((450, 450)).save("./logograms/{}.png".format(student['id']))
		image.resize((1024, 1024)).save("./logograms/big_{}.png".format(student['id']))
