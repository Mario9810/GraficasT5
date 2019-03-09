import struct
from collections import namedtuple

from objj import Obj

"""
funciones para escribir bmp
"""
def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([b,g,r])

"""
operaciones vectoriales utiles
"""
vector = namedtuple('vector',['Xaxis','Yaxis','Zaxis'])
def pcruz(vector1,vector2):
    vector = vector(
        vector1.Xaxis * vector2.Xaxis - vector1.Zaxis * vector2.Yaxis, vector1.Zaxis * vector2.Xaxis - vector1.Xaxis * vector2.Zaxis,
        vector1.Xaxis * vector2.Yaxis - vector1.Yaxis * vector2.Xaxis)
#clase de render
class SR(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.color = color(0,0,0)
        self.framebuffer = []
    def glClean(self):
        self.framebuffer = [
		[
			color(0,0,0) 
				for x in range(self.width)
			]
		
			for y in range(self.height)
		]


    def write(self):
        file = open(filnemae,'bw') 
        # File header (14 bytes)
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14 + 40 + self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(14 + 40))

        # Image header (40 bytes)
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
        f.close()
    def objeto(self,filename,):
        objeto = obj()
               
        
