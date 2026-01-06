data={
"Name":"Tushar",
"Surname":"Italiya",
"City" :"Bhavnagar",
"Dob":"01-01-2006",
"Taluka":"Palitana",
"Fav City":"Mumbai",
"Fav Book":"Geeta",
"Fav Fruit":"Mango",
"Fav Place":"MountAbu",
"State:":"Gujarat",
"Country":"india",
"College":"SSCCS",
"Cource":"BCA",
"Semester":6,
"Language":"Gujarati",
"IsMarried":False,
"Gender":"Male",
"Height":5.5,
"Weight":56,
"Age":20,
}

#Print Dictionary
print(data)
print(data["Name"],data["Gender"],data["Age"],data["Dob"])


#add pincode

data["Pincode"]=364150

#destinations

data["FavDestinations"]=["Pune","Surat","Mumbai","Bhuj","Dwarka"]


print("favorite Destinations :",data["FavDestinations"])