# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:56:18 2018

@author: karupaa
"""

print "***** For Area *****"
from math import pi
r=input("enter radius=");
area=pi*r*r
print "AREA of circle=",area
print "####### For Fibbonaci ########"
f=0
s=1
n=input("enter the nth fibbonci no=");
for i in range(0,n):
    
    c=s+f
    f=s
    s=c
    print c
print "last no=",c    
print "$$$$$$$$$ Factorial $$$$$$$$$"
m=input("enter fctoril value=");
f=1
for i in range(m):
    f=f*i
print "factorial is=",f
     
import math
for i in range(7):
    c=random()
print c
     
    
    
    