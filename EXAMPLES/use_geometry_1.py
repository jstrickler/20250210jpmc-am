import sys
import alpha.mathlib.geometry as geometry # find and load geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# 1. current folder
# 2. folders in PYTHONPATH
#        Windows PATH1;PATH2
#        Non-Windows PATH1:PATH2
# 3. installation dir + /lib
print(f"{sys.prefix = }")
print(f"{sys.executable = }")
print()
for path in sys.path:
    print(path)
