mylist = map(float, raw_input("Enter your list : ").split(","))
for i in mylist:
  try:
     result = 2/i
  except ZeroDivisionError:
     print ("divisio by zero")
  else:
     print result
 
 
