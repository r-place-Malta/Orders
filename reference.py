import json
from PIL import Image

im = Image.open('reference.png') 
pix = im.load()

color_mappings = {
    '#6D001A': 0, 
    '#BE0039': 1, # Dark red
    '#FF4500': 2, # Red
    '#FFA800': 3,
    '#FFD635': 4,
    '#FFF8B8': 5,
    '#00A368': 6,
    '#00CC78': 7,
    '#7EED56': 8,
    '#00756F': 9,
    '#009EAA': 10,
    '#00CCC0': 11,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#493AC1': 15,
    '#6A5CFF': 16,
    '#94B3FF': 17,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#E4ABFF': 20,
    '#DE107F': 21,
    '#FF3881': 22,
    '#FF99AA': 23,
    '#6D482F': 24,
    '#9C6926': 25,
    '#FFB470': 26,
    '#000000': 27,
    '#898D90': 29, # Gray
    '#515252': 28, 
    '#D4D7D9': 30, # Light Grey
    '#FFFFFF': 31 # White
}
orders = []

def rgb_to_hex(rgb):
	return '#' + (('%02x%02x%02x' % rgb).upper())

formatted_out = '[\n'

for x in range(2000):
	for y in range(2000):
		colors = pix[x, y]
		if colors[3] == 0:
			continue
		hex = rgb_to_hex((colors[0], colors[1], colors[2]))
		colorid = color_mappings[hex]
		orders.append([x, y, colorid])
		formatted_out += '[' + str(x) + ', ' + str(y) + ', ' + str(colorid) + '],\n'

formatted_out += ']'

print(formatted_out)

# Save the formatted_out data to the JSON file
with open("orders.json", "w") as json_file:
    json_file.write(formatted_out)

print("Data has been written to 'orders.json'.")
