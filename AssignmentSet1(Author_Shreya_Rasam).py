
# coding: utf-8

# In[3]:


1.#Basic arithmatic operation

a=int(input("Input first number"))
b=int(input("Input second number"))
Addition=a+b
Subtraction=a-b
Multiplication=a*b
Division=a/b
print ("Addition is:",Addition)
print ("Subtraction is:",Subtraction)
print ("Multiplication is:",Multiplication)
print ("Division is:",Division)


# In[6]:


2. #Biggest of 3 numbers 

a=int(input("Input first number"))
b=int(input("Input second number"))
c=int(input("Input third number"))

if (a>b) and (b>c):
    biggest_number=a
elif (b>a) and (b>c):
    biggest_number=b
else:
    biggest_number=c
print ("Biggest of 3 numbers is:",biggest_number)


# In[11]:


3. #Even or Odd number

a=int(input("Input number"))
b=int(a/2)*2
if(b==a):
    print("This Number is Even")
else:
    print("This Number is Odd")



# In[15]:


4. #Prime number


def primenum(Number):
primenumber = []
    for Primes in range(2, Number + 1):
        isPrime = True
        for num in range(2, Primes):
            if Primes % num == 0:
                isPrime = False
        if isPrime:
            primenumber.append(Primes)
    return(primenumber)


# In[ ]:


5. #Read string and print each character separately

