for i in range(5):
    if i==3:
        break
    print("hello", i )

print("break terminated")


for i in range(5):
    if i == 3:
        continue
    print("hello" ,i)

x = (2,4,6,7,8,10,12)
for i in x:
  print(i)
  if i<6:
    continue