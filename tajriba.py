
```
n=5
numbers=[1,2,0,3,4,5]
s=1
for i in range(0,n+1):
    if i in numbers:
        s*=1
    else:
        print(i)
        break
if s==1:
    print(0)
```