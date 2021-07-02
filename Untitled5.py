#!/usr/bin/env python
# coding: utf-8

# In[1]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[3]:


i=int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)


# In[1]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    


# In[ ]:




# input sale amount
amt = int(input("Enter Sale Amount: "))

# checking conditions and calculating discount
if(amt>0):
    if amt<=5000:
       disc = amt*0.05
    elif amt<=15000:
        disc=amt*0.12
    elif amt<=25000:
        disc=0.2 * amt
    else:
         disc=0.3 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")



# In[ ]:




