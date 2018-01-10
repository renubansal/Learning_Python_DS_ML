f = open("data.txt","r")
keyList = ['Name','Roll Number','Marks']
list = []
for line in f:
	list.append(dict (zip (keyList,line.split(",") ) ) )

for element in list:
	print element

print list