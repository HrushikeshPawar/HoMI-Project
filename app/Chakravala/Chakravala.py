from math import sqrt, floor
from random import choice

def chakravala(n):
    
  iteration = []

  n=int(n)
  p=1
  #while p+1<sqrt(n):
  #  p=p+1
  p = floor(sqrt(n))
  q = 1
  m = (p**2) - n * (q**2)
  m = int(m)

  #print(f"\np={p}")
  #print(f"q={q}")
  #print(f"m={m}\n")
  iteration.append((p,q,m))

  i=1
  if m!=1:
    x = abs(m) - p
    x = int(x)
    j = 2
    while x + abs(m) < sqrt(n):
      x = abs(m) * j - p
      x = int(x)
      j = j + 1
    
    print(f"x={x}")
    
    old_x = x
    old_p = p
    old_q = q
    old_m = m

    p = ((old_p*x)+n) // abs(old_m)
    q = (old_p+x) // abs(old_m)
    m = (x**2-(n)) // old_m

    p = int(p)
    q = int(q)
    m = int(m)                       
    
    #print(f"p={p}")
    #print(f"q={q}")
    #print(f"m={m}\n")  
    iteration.append((p,q,m))
    
    i=1
  while m!=1:
    x=abs(m)-old_x
    x=int(x)
    j=2
    while x+abs(m)<sqrt(n):
      x=abs(m)*(j)-old_x
      x=int(x)
      j=j+1
    print(f"x={x}")  

    old_x=x
    old_p=p
    old_q=q
    old_m=m

    p=int(int(old_p*x)+int(n*old_q))//abs(old_m)
    q=int(old_p+int(x*old_q))//abs(old_m)
    m=(x**2-(n))//old_m 

    p=int(p)
    q=int(q)
    m=int(m)  

    #print(f"p={p}")
    #print(f"q={q}")
    #print(f"m={m}\n")
    iteration.append((p,q,m))
    i=i+1
    
  return iteration

def samasabhavana(n,p,q,m):
    
    n=int(n)
    sol_list=[(p,q)]
    
    if m>1:  
      
      old_p=p
      old_q=q
    
      p=old_p**2+(n*(old_q**2))
      q=(old_p*old_q)+(old_q*old_p)
      sol_list.append((p,q))
      
      while len(sol_list)!=m:
        x1=choice(sol_list)
        x2=choice(sol_list)

        #print(x1)
        p1=x1[0] 
        q1=x1[1]
        p2=x2[0]
        q2=x2[1]

        p3=(p1*p2)+(n*q1*q2)
        q3=(p1*q2)+(q1*p2)
        if (p3,q3) not in sol_list:
          sol_list.append((p3,q3))

    return sol_list  
      

