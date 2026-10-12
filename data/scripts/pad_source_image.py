"""Pads data/derived/side-a-original.jpg with a uniform 400px gray border on all sides, so
generate_polar_unwrap.py has generous radius headroom in every angular direction regardless of
the disc's own real eccentricity (its hand-carved rim isn't a perfect circle). Run once; the
padded output is then the polar-unwrap script's own source.
"""
from PIL import Image, ImageOps

SRC = 'data/derived/side-a-original.jpg'
OUT = 'data/derived/side-a-original-padded.jpg'
PAD = 400

im = Image.open(SRC)
padded = ImageOps.expand(im, border=PAD, fill=(128, 128, 128))
padded.save(OUT, quality=92)
print('wrote', OUT, 'size', padded.size)
