items = [
    ("prodect",10),
    ("prodect1",5),
    ("prodect2",12),
    ("prodect3",7)
]
filtered = list(filter(lambda item: item[1] >= 10,items))
print (filtered)
