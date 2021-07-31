import glob
import os
print(os.name)
print(os.cpu_count())
for file in os.listdir():
    print(file)
