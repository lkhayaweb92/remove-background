from rembg import remove
from PIL import Image
input_path = 'foto 2.jpg'
output_path = 'foto4.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)