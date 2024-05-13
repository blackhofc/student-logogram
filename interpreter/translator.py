import json, math
from PIL import Image, ImageDraw
from utils.tendril import Tendril
from utils.circularStroke import CircularStroke


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
			


def logogram(symbol, imgSize, varThickness, varCenter, nmbCirc, varRad):
	
	print(imgSize, varThickness, varCenter, nmbCirc, varRad)
	image = Image.new("RGBA", imgSize, (255, 255, 255, 0))
	x = image.width/2
	y = image.width/2
	print(x, y)

	draw = ImageDraw.Draw(image)
	
	stroke = CircularStroke(nmbCirc, (x,y), varCenter, varThickness, 0, varRad)

	disks      = symbol['disks']
	tendrils   = symbol['tendrils']	
  
	blobCircles  = symbol['blobCircles']

	make_disks(draw, (x,y), 0, 0, disks, tendrils)
	
	stroke.drawCircleBlob(draw=draw, angle=0, blobCircles=blobCircles)
		
	return image

def read(filename: str):

    with open('{}.json'.format(filename), 'r', encoding='utf-8') as file:
        # Load JSON data from the file
        return json.load(file)

if __name__ == '__main__':
	seeds    = read(filename='seeds')

	for seed in seeds:
		for symbol in seeds[seed]:
			image = logogram(seeds[seed][symbol], (900, 900), 10, 10, 100, (1, 1))
			#image.show()
			image.resize((250, 250)).save("./translator/{}.png".format(seeds[seed][symbol]['id']))	
		