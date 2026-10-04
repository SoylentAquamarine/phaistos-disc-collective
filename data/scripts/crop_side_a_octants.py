from PIL import Image
import pathlib

SRC = pathlib.Path('data/derived/side-a-crops/disc_full.jpg')
OUT = pathlib.Path('data/derived/side-a-crops/octants')
OUT.mkdir(parents=True, exist_ok=True)

img = Image.open(SRC)
w, h = img.size
cx, cy = w / 2, h / 2
tile = 1500
half = tile / 2
offset_r = 650
dirs = {
    'N': (0, -1), 'NE': (0.7071, -0.7071), 'E': (1, 0), 'SE': (0.7071, 0.7071),
    'S': (0, 1), 'SW': (-0.7071, 0.7071), 'W': (-1, 0), 'NW': (-0.7071, -0.7071),
}
for name, (dx, dy) in dirs.items():
    tcx, tcy = cx + dx * offset_r, cy + dy * offset_r
    box = (int(tcx - half), int(tcy - half), int(tcx + half), int(tcy + half))
    img.crop(box).save(OUT / f'oct_{name}.jpg', quality=95)
print('done')
