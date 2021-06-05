from pathlib import Path
path = Path("ecomers")
print (path.exists())
"mor"
"make a diritori"
#path1 = Path("email")
#print (path1.mkdir())
"delite diritori"
#path2 = Path("email")
#print (path2.rmdir())
"glob"

path3=Path()
print (path3.glob('*.*'))
"list all file"

for file in path3.glob('*.*'):
    print (file)










