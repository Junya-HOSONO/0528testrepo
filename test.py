import sys
import platform

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()

print (sys.version)
print (platform.platform())

