# this exists because why not. I think I wrote this once when I was bored and just needed something to code.
# I still really like it. It's a very simple algorithm, yet it's so elegant. I also learned what overflow 
# is because of this project.

on = True
nmin2 = 1
nmin1 = 1
n = 0
num = input("how many terms do you want (pick an intgeger 3 or greater)")
nth = (num - 2)
print("1")
print("1")
for i in range (nth):
  n = (nmin1 + nmin2)
  print(n)
  nmin2 = nmin1
  nmin1 = n
