n=2
while 1:
 n*=2;m=n-1
 if~any([m%i==0for i in range(2,m)]):print(m)