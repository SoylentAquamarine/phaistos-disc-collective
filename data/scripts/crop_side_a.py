from PIL import Image
import hashlib, pathlib

SRC = pathlib.Path('data/derived/side-a-original.jpg')
OUT = pathlib.Path('data/derived/side-a-crops')
OUT.mkdir(parents=True, exist_ok=True)

with open(SRC, 'rb') as f:
    print('source sha256:', hashlib.sha256(f.read()).hexdigest())

img = Image.open(SRC)
print('source size:', img.size)

# disc region within the full photograph (determined by visual inspection)
crop = img.crop((1150, 140, 3740, 2920))
crop.save(OUT / 'disc_full.jpg', quality=92)

w, h = crop.size
margin = 100
quads = {
    'q_tl': (0, 0, w // 2 + margin, h // 2 + margin),
    'q_tr': (w // 2 - margin, 0, w, h // 2 + margin),
    'q_bl': (0, h // 2 - margin, w // 2 + margin, h),
    'q_br': (w // 2 - margin, h // 2 - margin, w, h),
}
for name, box in quads.items():
    crop.crop(box).save(OUT / f'{name}.jpg', quality=95)

print('done')
