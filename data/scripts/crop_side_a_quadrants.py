from PIL import Image
import pathlib

SRC = pathlib.Path('data/derived/side-a-crops/disc_full.jpg')
OUT = pathlib.Path('data/derived/side-a-crops/quadrants')
OUT.mkdir(parents=True, exist_ok=True)

img = Image.open(SRC)
w, h = img.size
quads = {
    'NW': (0, 0, int(w * 0.58), int(h * 0.58)),
    'NE': (int(w * 0.42), 0, w, int(h * 0.58)),
    'SW': (0, int(h * 0.42), int(w * 0.58), h),
    'SE': (int(w * 0.42), int(h * 0.42), w, h),
}
for name, box in quads.items():
    c = img.crop(box)
    cw, ch = c.size
    c2 = c.resize((cw * 2, ch * 2), Image.LANCZOS)
    c2.save(OUT / f'quad_{name}.jpg', quality=92)
print('done')
