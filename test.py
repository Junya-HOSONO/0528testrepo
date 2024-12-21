import sys
import platform
import os
import cpuinfo

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()

print(sys.version)
print(platform.platform())
print(sys.executable)
print(platform.architecture())
print(platform.version())
print(os.uname().machine)
print(cpuinfo.get_cpu_info()['brand_raw'])

