import math

class Tendril:

	def __init__(self, x, y, width, angle):

		self.x = x
		self.y = y
		self.width = width
		self.angle = angle 
		self.segments = []
		self.v = 0

	def create(self, distance, curl, vSegments):

		for v in vSegments:
			self.x += math.cos(self.angle) * distance
			self.y += math.sin(self.angle) * distance
			self.v = 0
			self.v += v
			self.v *= 0.9 + curl * 0.1
			self.angle += self.v

			self.segments.append((self.x, self.y, self.angle))

	def draw(self, draw):

		n = len(self.segments)
		for i, (x, y, angle) in enumerate(self.segments):

				r = self.width
				#r = (1-float(i)/2*n) * self.width # size gradually decreases.
				draw.ellipse([(x,y),((x+r),(y+r))], fill=(0,0,0))