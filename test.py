import os
prefix=('images/anim/trix/welcome2/start')
fps=24
trans=None
pause = 1.0 / fps
chain = []
for fn in os.listdir(prefix):
    if 0:
        continue
    basename = os.path.basename(fn)
    base, ext = os.path.splitext(basename)
    if not ext.lower() in [ ".jpg", ".jpeg", ".png", ".webp" ]:
        print(chain)
        continue
    chain.extend([fn, pause, trans])
print(chain)
        

        


