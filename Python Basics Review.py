#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# # Arithmatic Operators
# x=3
# y=5
# 
# x*y

# In[2]:


x+y


# In[3]:


5/2


# In[4]:


8/2


# In[5]:


2/8


# In[6]:


5/10


# # Comparision Operators gives boolean results(True/False)
# 5>2

# In[8]:


2>6


# In[9]:


2==9


# In[10]:


9==9


# In[11]:


"Mahesh">"Rajesh"


# In[13]:


"Rajesh">"Mahesh"


# In[14]:


#Not equal to
3!=3


# In[15]:


3!=4


# In[16]:


1>=2


# In[17]:


2>=1


# In[18]:


3<=1


# In[19]:


3<=5


# # Logical Operators(and, or, not)

# In[20]:



x=5
x>6 and x <4


# In[21]:


x=5
x>6 or x<4


# In[22]:


x=5
x>5 or x<7


# In[23]:


not(x>2 and x<4)


# In[24]:


not (x>2 or x<4)


# # #Variables

# In[25]:


#variable name=value o information
x=6
y="Mahesh"


# In[26]:


#Input and print functions
print("Hellow Mahesh")


# In[27]:


"hello Mahesh"


# In[38]:


x=input("What is your Age?")


# In[39]:


type(x)
#by default the data type of the input taken from the user is string


# In[41]:


#Type Conversion/Converting into Integer
z=int(x)
type(z)


# In[31]:


x=input("Your name?")


# In[32]:


type(x)


# In[34]:


X=int(x)


# In[48]:


y=36/4*(3+2)*4+2
print(y)


# In[49]:


2**3


# In[50]:


2*2**3


# In[51]:


x=input("The cube of Number")


# In[56]:


#Accessing String Elements using index
string="Mahesh"
print(string[1]) #indexing always start from "0"


# In[57]:


string[4]


# In[58]:


string[5]


# # String Slicing

# In[59]:


#strinf slicing and remember
#in index of the string,Character of the end index is not included n-1
m="Mahesh Varma"
m[0]


# In[60]:


m[1:5]


# In[61]:


m[:4]


# In[62]:


m[0]


# In[63]:


m[1]


# In[64]:


m[2]


# In[72]:


m[0:5]


# In[74]:


m[2:4]


# In[75]:


m[2:]


# In[77]:


m[6:9]


# # String Concatenation
# 

# In[93]:


x="Mahesh!"
y="Varma"
z= x + y
print(z)


# In[94]:


#adding space between two strings
x+' '+y


# In[95]:


#finding leangth of the string
len(z)


# In[96]:


len(x)


# In[97]:


x[-1]


# In[281]:


m="mahesh"
m.append("z")


# In[282]:


len(m)


# In[294]:


m.count("lf")


# # list

# In[98]:


#list is a mutable data type
#list can hold different types of data types
#It can be of any data type
#collection of values
#can be combination of different types
M=['Mahesh','India',630171282,60.3]


# In[101]:


#we can change values in list because it is mutable
M[0]="Varma" #changed values using index
M


# In[102]:


#adding values to the list
M.append("Age: 26")


# In[103]:


M


# In[114]:


#now I would like to add at specified index
M.insert(0,'Added value using index')
print(M)


# In[127]:


M=['Mahesh','India',630171282,60.3]


# In[128]:


M.insert(2,'hello')
M


# In[129]:


x=["he",1,'they']


# In[130]:


M+x


# In[131]:


M+"adding string to list "


# In[132]:


len(M)


# In[135]:


#looking up values in list
"Mahesh" in M


# In[136]:


"Raju"in M


# In[137]:


M.sort()


# In[149]:


x=[1,6,8,2,3]
x


# In[150]:


x.sort()
x


# In[152]:


x.count(3)


# In[145]:


x=['hi','hello','one','seven','and']
x.sort()
x


# In[146]:


x.len()


# In[172]:


len(x)


# In[148]:


x.count(hi)


# In[254]:


l1=[1,3,9,7]
l1[1:3]=[6,5]
l1


# In[260]:


l1*3


# In[262]:


l2=[]*3
l2


# In[268]:


l3=[]
l3=[1,2]
print(l3)
type(l3)


# In[270]:


l3.append(3)
l3


# # tuple

# In[192]:


#tuples are immutable
x=(2,3,4,8,9,4)
x


# In[183]:


type(x)


# In[193]:


print(x.count(4))


# In[184]:


x[2]


# In[185]:


x[2]=7


# In[186]:


x.count(2)


# In[195]:


len(x)


# In[188]:


x.append(3)


# In[189]:


y=(5,9,"Hi",7,3.6)
y


# In[190]:


x


# In[191]:


print(x[8])


# In[166]:


max(x)


# In[167]:


max(y)


# In[168]:


z=x+y
z


# In[170]:


z=y+x
z


# In[171]:


z.sort()


# In[173]:


len(z)


# In[174]:


min(z)


# In[175]:


min(x)


# In[176]:


del x


# In[177]:


z


# In[178]:


x


# In[179]:


z=x+y


# # Dictionary

# In[198]:


my_dict={"key1":"value1", 
        "key2":"value2"}
my_dict


# In[197]:


print(my_dict)


# In[199]:


d={}


# In[200]:


d["1"]="Mahesh"
d["2"]="Madhu"
d["3"]="Ramu"


# In[201]:


d


# In[207]:


d1={"Mahesh":"25","Rajesh":30}


# In[203]:


d1


# In[204]:


d1+d


# In[244]:


d1.sort()


# In[206]:


d1[1]


# In[208]:


d1["Rajesh"]


# In[209]:


d1["30"]


# In[212]:


d["5"]="Adding extre value"
d


# In[222]:


#iteration in dict

for key, value in d.items():
    print("key:")    
    print(key,)
    print(value)
    print("")


# In[232]:


d2={}
d2[1]="hi"


# In[233]:


d2['2']="hello"


# In[235]:


d2[name]="mass"


# In[239]:


d2["name"]='Mahesh'


# In[240]:


d2


# In[241]:


d2['name']


# In[242]:


d2[2]


# In[243]:


d2['2']


# In[246]:


d3=dict()
d3


# In[247]:


d3[1]="name"
d3[2]="age"
d3


# In[248]:


d3[2]="something"


# In[249]:


d3


# In[271]:


d3.len()


# In[272]:


len(d3)


# In[273]:


d3.size()


# In[274]:


d3.keys()


# In[279]:


list(d3.keys())


# In[280]:


list(d3.values())


# In[ ]:




