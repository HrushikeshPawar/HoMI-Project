from math import sqrt
from random import choice

def cakravala(d):
    
    iterations = []
    d=int(d)
    
    #Finding a,b and k
    j=1
    i=0
    while i<1:
        if j**2-d>0: 
            if ((j-1)**2)-d!=0:  
                if (j**(2)-d)>abs((j-1)**(2)-d):
                    a=j-1
                else:
                    a=j  
                i=i+1
            else:
                if (j**(2)-d)>abs((j-2)**(2)-d):
                    a=j-2
                else:
                    a=j  
            i=i+1
        j=j+1

    b=1
    k=a**(2)-d*(b**(2))
    #print(f"Iteration 1")
    #print(f"a={a}, b={b}, k={k}\n")
    iterations.append((a, b, k))
    
    #Finding m
    i=1 
    while k!=1: 
        
        # Find positive value for m
        mp=1
        while (a+(mp*b))%k!=0 or (a+(mp*b))==0 or (mp**2)-d==0:
            mp=mp+1
        old_mp=mp
        
        while (mp**2)-d<=0 or ((a*mp)+(d*b))==0  or (a+(mp*b))==0:
            if (mp**2)-d<0 and ((a*mp)+(d*b))!=0 and (a+(mp*b))!=0:
                old_mp=mp
            mp=mp+abs(k)

        new_mp=mp
        
        if ((old_mp**2)-d)!=0 and ((a*old_mp)+(d*b))!=0 and (a+(old_mp*b))!=0:
            if abs((new_mp**2)-d)>abs((old_mp**2)-d):
                mp=old_mp
            elif abs((new_mp**2)-d)==abs((old_mp**2)-d):  
                mp=choice([old_mp,new_mp]) 
        
        m=mp



        #Assign values to old a,b & k
        old_a=a
        old_b=b
        old_k=k  

        #Assign new values to a,b & k
        a=((old_a*m)+(d*old_b))//abs(old_k)
        b=(old_a+(m*old_b))//abs(old_k)
        k=((m**2)-d)//old_k

        a=int(a)
        b=int(b)
        k=int(k) 

        #print(f"a={a}, b={b}, k={k}\n")
        iterations.append((a, b, k))
        i=i+1
    return iterations

def Bhramhagutas_Shortcuts(d, a, b, k):

    if k==-1:
        old_a=a
        old_b=b
        
        a=2*((old_a)**2)+1
        b=2*old_a*old_b
        k=(a**2)-(d*(b**2))
        
    elif k==2:
        old_a=a
        old_b=b
        
        a=((old_a)**2)-1
        b=old_a*old_b
        k=(a**2)-(d*(b**2))
        
    elif k==-2:
        old_a=a
        old_b=b
        
        a=((old_a)**2)+1
        b=old_a*old_b
        k=(a**2)-(d*(b**2))

    elif k==4:
        if a%2==0:
            old_a=a
            old_b=b
        
            a=((old_a**2)-2)//2
            b=(old_a*old_b)//2
            k=(a**2)-(d*(b**2))
        
        else:
            old_a=a
            old_b=b
        
            a=(old_a*((old_a**2)-3))//2
            b=(old_b*((old_a**2)-1))//2
            k=(a**2)-(d*(b**2))

    elif k==-4:
      
        if a%2==0:
            old_a=a
            old_b=b

            a=((old_a**2)+2)//2
            b=(old_a*old_b)//2
            k=(a**2)-(d*(b**2))

        else:
            old_a=a
            old_b=b

            a=(((old_a**2)+2)*((((old_a**2)+1)*((old_a**2)+3))-2))//2
            b=(old_a*old_b*((old_a**2)+1)*((old_a**2)+3))//2
            k=(a**2)-(d*(b**2))

    return a, b, k

def Cakravala_with_Bhramhaguptas_shortcut(d):

    iterations = []
    d=int(d)
    #Finding a,b and k
    j=1
    i=0
    while i<1:
        if j**2-d>0: 
            if ((j-1)**2)-d!=0:  
                if (j**(2)-d)>abs((j-1)**(2)-d):
                    a=j-1
                else:
                    a=j  
                i=i+1
            else:
                if (j**(2)-d)>abs((j-2)**(2)-d):
                    a=j-2
                else:
                    a=j  
                i=i+1
        j=j+1
    b=1
    k=a**(2)-d*(b**(2))
    # print(f"Iteration 1")
    # print(f"a={a}, b={b}, k={k}\n")
    iterations.append((a, b, k))

    a, b, k = Bhramhagutas_Shortcuts(d, a, b, k)
    if (a, b, k) not in iterations:
        iterations.append((a, b, k))

    #Finding m
    i=1 
    while k!=1:
        
        # Find positive value for m
        mp = 1
        while (a+(mp*b))%k!=0 or (a+(mp*b))==0 or (mp**2)-d==0:
            mp=mp+1
        old_mp=mp
        
        while (mp**2)-d<=0 or ((a*mp)+(d*b))==0  or (a+(mp*b))==0:
            if (mp**2)-d<0 and ((a*mp)+(d*b))!=0 and (a+(mp*b))!=0:
                old_mp=mp
            mp=mp+abs(k)
        new_mp=mp
           
        if ((old_mp**2)-d)!=0 and ((a*old_mp)+(d*b))!=0 and (a+(old_mp*b))!=0:
            if abs((new_mp**2)-d)>abs((old_mp**2)-d):
                mp=old_mp
            elif abs((new_mp**2)-d)==abs((old_mp**2)-d):  
                mp=choice([old_mp,new_mp]) 
        
        m=mp

        #Assign values to old a,b & k
        old_a=a
        old_b=b
        old_k=k  

        #Assign new values to a,b & k
        a=((old_a*m)+(d*old_b))//abs(old_k)
        b=(old_a+(m*old_b))//abs(old_k)
        k=((m**2)-d)//old_k 

        a=int(a)
        b=int(b)
        k=int(k)

        #print(f"a={a}, b={b}, k={k}\n")
        iterations.append((a, b, k))

        a, b, k = Bhramhagutas_Shortcuts(d, a, b, k)
        if (a, b, k) not in iterations:
            iterations.append((a, b, k))
    
        i=i+1
    return iterations

def LagrangeMethod(D):

    # Initialize the req var
    m = 0
    d = 1
    a0 = int(sqrt(D))
    a = a0
    num1, num2 = a, 1
    den1, den2 = 1, 0
    results = []
    n=1

    # Loop until we get solution
    while True:

        # Update variables
        m = d*a - m
        d = int((D - m*m) / d)
        a = int((a0 + m) / d)

        # Get numerator and denominator
        numerator = a * num1 + num2
        denominator = a * den1 + den2

        results.append((numerator, denominator, numerator*numerator - D*denominator*denominator))
        n += 1
        # Check if this satisfies the equation
        if numerator*numerator - D*denominator*denominator == 1:
            return results
        
        # Update values of num and den
        num2 = num1
        num1 = numerator
        den2 = den1
        den1 = denominator
