a=input("enter a=");
b=input("enter b=");
c=a+b;
print c
print("enter no. of accounts");
n=input("enter no.=");
for i in range (0,n):
 print("enter the  account details");
 A=raw_input("enter account name");
 ag=raw_input("enter age");
 D=input("enter deposit");
 print("withdaw/no withdraw press 1/0");
 x=input("enter option");
 if(x==0):
   break;
 elif(x==1):
  
 	W=input("\twithdrw=");
 	if(W>D):
   	 print"\tammount cannot be processed";
         print"\tsince ammount is greater than balance";
 	elif(W<D):
         print"\tthe ammount withdraw=",W;
  	 nD=D-W;
  	 print"\tbalance=",nD;
 	elif(W==D):
  	 print"\tthe ammount withdrawn=",W;
  	 nD=D-W;
  	 print"\tbalance=",nD;
