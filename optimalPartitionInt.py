#this was made after a lecture about partitioning in Harvard Extension Math E-15 (Spring 2017)
#it isn't good for much, but I was just really excited about it
#by the time I'm adding this header (Aug 2018) I don't totlaly remember why this was so cool to me
#but this is the product of inspiration sparked by general exitement about math
#so I'm keeping it anyway

xVal = input("what integer should I partition?")
rVal = xVal%3
if rVal == 2:
    print("Optimal Partition Product is (3^"+str((xVal-2)/3)+")2")
elif rVal == 1:
    print("Optimal Partition Product is (3^"+str((xVal-4)/3)+")4")
else:
    print("Optimal Partition Product is 3^"+str(xVal/3))
