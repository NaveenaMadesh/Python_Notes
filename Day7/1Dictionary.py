#stores values as key : value pairs
#mutable
#key cant be duplicated

dic ={}
print(type(dic))

#stuct
'''d={key1:value,
   key2:value,
   .....
   key3:value}'''

#keys should be unique
'''d={k1:{v1,v2,v3},
   k2:{v1,v2,v3}}'''
#keys and values can be of different type
d={101: "Naveena",
   102:"Mohith",
   103:"Karthiga"}

print(d)

#duplicate keys are not allowed
d={101: "Naveena",
   102:"Mohith",
   103:"Karthiga",
   101: "Monisha"}
#here the first value gets updated as per the duplicates
print(d)

#accessing via keys

print(d[101])#Monisha
print(d.get(102))#Mohith

#Insertion

d[104] = "Ajay"
print(d)

#update
d[101]="Mahi"
print(d)


#looping
for i in d:
    print(i,d[i])

#merging of two dictionaries

bookdetails = {"sn1":["Dr.Seuss","The cat in the Hat"],
               "sn2":{"E.B.White","Charlotee's Web"}}
print(bookdetails["sn1"][1])

bookdetails["sn3"] = ["xyz","zxe"]
print(bookdetails)

bookdetails["sn4"] = [{"101":"Harry Potter"},{"102","Harris"}]
print(bookdetails)

#merging
lib1 = {101:"xeys",
        102:"zxey"}

lib2 ={103 : "IJUK",
       105: "Hujk"}

combined_lib = {"lib1": lib1,
                "lib2": lib2}

print(combined_lib)

#print only keys
print(d.keys()) #([101,102,103,104])
#print values
print(d.values())

#removing elements
