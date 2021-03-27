import array
import os
import math
import random

from data.items import *
from data.world import *
from data.colors import *



renderStep = 0



def getRoomRender():
	
	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			for SpriteY in range(renderSizeMultiplier["Y"]):	#por cada sprite

				for SpriteX in range(renderSizeMultiplier["X"]):

					roomRenderCellY = y * renderSizeMultiplier["Y"] + SpriteY 
					roomRenderCellX = x * renderSizeMultiplier["X"] + SpriteX 

					content = roomContent[y][x]

					roomContentInfo = itemsInfo[content]

					roomContentSprite = roomContentInfo["sprite"]

					color = colors[roomContentInfo["color"]]
					effect = effects[roomContentInfo["effect"]]
					background = backgroundColors[roomContentInfo["backgroundColor"]]

					roomRender[roomRenderCellY][roomRenderCellX] = "\033[" + effect + ";" + color + ";" + background + "m" + roomContentSprite[renderStep % len(roomContentSprite)][SpriteY][SpriteX] + "\u001b[0m"	#Añade el subSprite correspondiente






def render():

	clear = lambda: os.system('cls')
	clear()


	getRoomRender()

	#---------renderiza la room
	for y in range(len(roomRender)):
		separator = ''
		print(separator.join(roomRender[y]))


	print()




	global renderStep
	renderStep += 1