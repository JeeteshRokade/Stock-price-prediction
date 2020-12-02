# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 07:51:14 2020

@author: op.felix1
"""

string1 = "abdfsdfnkfgkccbcavcbbclj"
string2 ="nkf"

string2list=[]
for v in string2:
    string2list.append(v)
    
print(string1)
i=0
n = len(string1)
print(n)
subn={}
while i<=(n-1):
     #n-1
    substr=string1[i:n]
    print("subst",i,substr)    
    temp=[]
    j=0
    for ele in substr:
        j=j+1

       
        if set(temp) == set(string2list):
            subn[i]=j-1
            break
        if ele in string2:
        
            if ele in temp:
                continue
            else:
                temp.append(ele)
        else:
            temp=[]
        
        print(temp,j)
    
    i=i+1
#end while    

val = subn.values
print(subn)