import os

print("Directory contents:")
for f in os.listdir():
    print(f)
with open('test.json', 'w') as outfile:
    outfile.write("This file was made with Github actions!")