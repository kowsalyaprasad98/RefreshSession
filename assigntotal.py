a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
file=open("totalofproducts","w")
if a<=0 or b<=0 or c<=0 or d<=0 or e<=0:
    print("Zero or Negative number")
else:
    t=a+b+c+d+e
    file.write("total: %d"%t)
    print(t)
#t=a+b+c+d+e
file.close()
