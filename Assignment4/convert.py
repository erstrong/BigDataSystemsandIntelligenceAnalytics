import os
from PIL import Image
import random

for filename in os.listdir('aligned'):
    
    name = 'aligned/'+filename
    new_name = 'test/'+filename
    img = Image.open( name )
    img.load()
    img = img.resize((32,32), Image.ANTIALIAS)
    img.save(new_name)


