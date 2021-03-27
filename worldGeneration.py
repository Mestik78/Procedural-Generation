import math
import random
import noise

from data.items import *
from data.world import *

def spawnObject(x, y, id):

	roomContent[y][x] = id



def spawnRandomObject(x, y):

	randomObjects = [2,3,5]

	spawnObject(x, y, randomObjects[random.randint(0, len(randomObjects) - 1)])


def createPerlinNoise():


	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			spawnObject(x, y, 0)	#pone los suelos


			noiseValue = 0

			for noiseType in noiseSettings["worldNoise"]:

				noiseValue += (noise.snoise2(x / noiseType["XResolution"] + noiseType["XOffset"],
											(y / noiseType["YResolution"] + noiseType["YOffset"])) + 1) / 2 * noiseType["strength"]

			if noiseValue < 0.4:
				spawnObject(x, y, 2) #agua

			elif noiseValue < 0.45:
				spawnObject(x, y, 4) #arena

			elif noiseValue < 0.8:
				spawnObject(x, y, 0) #suelo

				grassNoiseValue = (noise.snoise2(x / noiseSettings["grassNoise"]["XResolution"] + noiseSettings["grassNoise"]["XOffset"],
												(y / noiseSettings["grassNoise"]["YResolution"] + noiseSettings["grassNoise"]["YOffset"])) + 1) / 2

				if grassNoiseValue < 0.2:
					spawnObject(x, y, 3) #grass

			else:
				spawnObject(x, y, 1) #montaña


			


def generate():
	createPerlinNoise()