from pathlib import Path

# Absolute path
# /urs/locale/bin
# Relative path

path = Path()

print(path.exists())

# Path.mkdir("Emails")

# Path.rmdir("Emails")

# print(path.glob('*.*'))

for file in path.glob("*"):
    print(file)

