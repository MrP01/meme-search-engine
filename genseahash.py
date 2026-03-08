import seahash
import sys

with open(sys.argv[1], "rb") as f:
    print(seahash.hash(f.read()))
