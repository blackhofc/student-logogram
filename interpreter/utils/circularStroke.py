import math, random
from random import randint

class CircularStroke:

	def __init__(self, nmb, center, centerVar, thicknessVar, rad, radVar):

		self.nmb = nmb
		self.center = center
		self.centerVar = centerVar
		self.thicknessVar = thicknessVar
		self.rad = rad
		self.radVar = radVar


	def arc(self, draw, bbox, start, end, fill, width=1.0, segments=100):

		# radians
		start *= math.pi / 180.0
		end *= math.pi / 180.0

		# angle step
		da = (end - start) / segments

		# shift end points with half a segment angle
		start -= da / 2
		end -= da / 2

		# ellips radii
		rx = (bbox[2] - bbox[0]) / 2
		ry = (bbox[3] - bbox[1]) / 2

		# box centre
		cx = bbox[0] + rx
		cy = bbox[1] + ry

		# segment length
		l = (rx+ry) * da / 2.0

		widthMax = width

		for i in range(segments):
			width = randint(-widthMax, widthMax)

			# angle centre
			a = start + (i+0.5) * da

			# x,y centre
			x = cx + math.cos(a) * rx
			y = cy + math.sin(a) * ry

			# derivatives
			dx = -math.sin(a) * rx / (rx+ry)
			dy = math.cos(a) * ry / (rx+ry)

			draw.line([(x-dx*l,y-dy*l), (x+dx*l, y+dy*l)], fill=fill, width=width)
   
	def draw(self, draw, angle, gapWidth):
		for i in range(1, self.nmb):
			xVar = self.center[0] + random.uniform(-self.centerVar,self.centerVar)
			yVar = self.center[1] + random.uniform(-self.centerVar,self.centerVar)

			thickness = self.thicknessVar
			randomRad = self.rad * random.uniform(self.radVar[0], self.radVar[1])

			#TODO
			holeAngle = angle
			v =  gapWidth

			randomAngleStart = random.uniform(v+holeAngle, 180+holeAngle-v)
			randomAngleEnd   = random.uniform(randomAngleStart, 360+holeAngle-v)

			self.arc(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness)

	def arc_v2(self, draw, bbox, start, end, fill, width, segments):

		# radians
		start *= math.pi / 180.0
		end *= math.pi / 180.0

		# angle step
		da = (end - start) / len(segments)

		# shift end points with half a segment angle
		start -= da / 2
		end -= da / 2

		# ellips radii
		rx = (bbox[2] - bbox[0]) / 2
		ry = (bbox[3] - bbox[1]) / 2

		# box centre
		cx = bbox[0] + rx
		cy = bbox[1] + ry

		# segment length
		l = (rx + ry) * da / 2.0

		for seg in segments:
			width = seg['width']

			# angle centre
			a = start + (seg['i'] + 0.5) * da

			# x,y centre
			x = cx + math.cos(a) * rx
			y = cy + math.sin(a) * ry

			# derivatives
			dx = -math.sin(a) * rx / (rx+ry)
			dy = math.cos(a) * ry / (rx+ry)

			draw.line([(x-dx*l,y-dy*l), (x+dx*l, y+dy*l)], fill=fill, width=width)
   	
	# blobLength, blobWidth, nmbCircles, centerVarBlob
	def drawCircleBlob(self, draw, angle, blobCircles):
		for blob in blobCircles:
			xVar = self.center[0] + blob['xVar']
			yVar = self.center[1] + blob['yVar']

			thickness = int(round(self.thicknessVar * blob['thickness']))

			randomRad = self.rad + blob['randomRad']

			randomAngleStart = angle + blob['randomAngleStart']
			randomAngleEnd   = angle - blob['randomAngleEnd']

			self.arc_v2(draw, (xVar-randomRad, yVar-randomRad, xVar+randomRad, yVar+randomRad), 
			randomAngleStart, randomAngleEnd, fill=(0,0,0), width=thickness, segments=blob['segments'])