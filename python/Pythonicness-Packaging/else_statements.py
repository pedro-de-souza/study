for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

# Unbroken 1

try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

# 1
# 3
# 4


for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)

# for range(10) = [0,1,2,3,4,5,6,7,8,9]
# Now if 10/0 == 2
# then print(1)

# then looping... 10/1 == 2
# print(2)

# again 10/2 == 2
# print(2)

# again 10/3 == 2
# print(2)

# again 10/4 == 2
# print(2)

# again 10/5 == 2
# here conditon is True. so
# break

# Now 1 + 2 + 2 + 2 + 2 = 9