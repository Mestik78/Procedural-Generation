import array
import os
import math
import random
import time



from render import render
from worldGeneration import generate


while True:	#game loop

	generate()
	render()	
	input()

