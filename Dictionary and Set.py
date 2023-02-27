#DICTIONARY

names = {"riya":"kerala","pramod":"hyderabad"}
age = {}
print(names)
print(age)
roll_no = dict()
print(roll_no)
#no duplicate keys
places = {"riyadh":"16","hyderabad":"19","riyadh":"17"}
print(places)
#key cant be any muttable type, values can be in a key- value pair
#dict are unordered so use key to access the elements
print(names["riya"])
#muttable
del names["pramod"]
print(names)
names["pramod"] = "kompally"
print(names)
school = {"riyadh":"NMEIS", "india":{12:"PLS","UG":"ASE"}}
print(school)
print(school["india"])

#SET
s = set()
print(s)
s1 = set("riya pramodh")
print(s1)
s2 = {1,2,3}
print(s2)
#takes no duplicate values
s3 = {1,2,3,3,2,1,4,4,4}
print(s3)
s4 = {3,1,2}
#set is unordered
print(s2 == s4)
#muttable
s4.add(4)
s4.remove(1)
print(s4)
#set can only have immutable elements as objects
#s = {[1,2,3],4} --> error so set is not nested
#can have different types of elements
set5 = {"riya",49,21.5,"india"}
print(set5)
print("riya" in set5)
print("pramod" in set5)

