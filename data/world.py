import random


roomSize = {
	"X": 230,
	"Y": 150
}

renderSizeMultiplier = {
	"X": 1,
	"Y": 1
}


noiseSettings = {

	"worldNoise": [
		{
			"strength": 0.35,

			"XOffset": random.randrange(-8192,8192),
			"YOffset": random.randrange(-8192,8192),

			"XResolution": 512,
			"YResolution": 512
		},
		{
			"strength": 0.4,

			"XOffset": random.randrange(-8192,8192),
			"YOffset": random.randrange(-8192,8192),

			"XResolution": 128,
			"YResolution": 128
		},
		{
			"strength": 0.25,

			"XOffset": random.randrange(-8192,8192),
			"YOffset": random.randrange(-8192,8192),

			"XResolution": 64,
			"YResolution": 64
		},
		{
			"strength": 0.05,

			"XOffset": random.randrange(-8192,8192),
			"YOffset": random.randrange(-8192,8192),

			"XResolution": 8,
			"YResolution": 8
		}
	],
		

	"grassNoise": {
		"XOffset": random.randrange(-8192,8192),
		"YOffset": random.randrange(-8192,8192),

		"XResolution": 16,
		"YResolution": 16
	}

}


# X * Y * roomsX * roomsY
roomContent = [ [ "" for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ]

roomRender = [ [ "" for i in range(roomSize["X"] * renderSizeMultiplier["X"]) ] for j in range(roomSize["Y"] * renderSizeMultiplier["Y"]) ]