import pandas as pd
n=list(map(int,input().split()))
s=pd.Series(n)
print("Series:\n",s)
print(s*s)
for i in s:
    print(i*i,end=" ")


