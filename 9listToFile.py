import json
f = open("data.txt","r")
keyList = ['Name','Roll Number','Marks']
list = []
for line in f:
	list.append(dict (zip (keyList,line.split(",") ) ) )
f.close()

#change marks value
for dict in list:
	dict['Marks'] = str(50)

f1 = open("file.txt","w")

for dic in list:
	f1.write(",".join(dic.values()))
	f1.write("\n");
f1.close()
