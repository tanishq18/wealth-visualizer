import pandas as pd
import matplotlib.pyplot as plt

"x is per month saving amount"
"Let x be constant"

x = int(input())

"y is the constant return percentage of the investment"

y = int(input())
y = y/100

"n is the number of years for which the calculation is needed"

n = int(input())

def calc(a,b,c):
    if c == 1:
        z = (a + a*b)
    else:
        z = (a + a*b)
        z = z + calc(a+z,b,c-1)
    return z

l1=[]
l1.append(0)
for i in range(1,n+1):
    l1.append(i)

l2=[]
l2.append(x)
for i in range(1,n+1):
    l2.append(calc(x,y,i))

data = {'Year': l1, 'Your Money': l2}
df = pd.DataFrame(data,columns=['Year','Your Money'])
print(df)

df.plot(x ='Year', y='Your Money', kind = 'bar')
plt.show()
