Places =["Mumbai","Pune","Surat","Katch","Bhuj"]
Things =["Books","Pen","Pensil","Sharpner","Eraser"]


print("List after Operation: ",Places)
#insert Function
Places.insert(0,"Dwarka")
print("List after Operation: ",Places)
Places.append("Navsari")
print("List after Operation: ",Places)
Places.remove("Katch")
print("List after Operation: ",Places)

print(Places[0:2])
print(Places[2:])


print(Places.count("Pune"))

Things.pop(2)
print("List after Pop Operation: ",Things)

print("Index is ",Things.index("Pen"))

Places.extend(Things)

CopyThings = Places.copy()
print(Places)
print("CopyList",CopyThings)

CopyThings.clear()
print("CopyList after clear",CopyThings)
