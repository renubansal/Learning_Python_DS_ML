import sys
str1 = ''.join(sys.argv[1:2])
str2 = ''.join(sys.argv[2:3])

print (str2 + ' find at '+str( str1.find(str2)))
