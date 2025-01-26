email = input("enter your Email Id :")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():#check the start with alphabate 
        #check "@" in email only at once
        if ("@" in email) and (email.count("@")==1):
            #"." apears only third and fourth place 
           if (email[-4]==".") ^ (email[-3]=="."):
               
                for i in email:
                    if i==i.isspace():       
                      k=1
                    elif i.isalpha():
                      if i==i.upper():
                        j=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or i=="."or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1: 
                    print("invailid email id 5")      
            
           else:
               print("invailid email id 4")
        else:
            print("invailid email id 3")
    else:
        print("invailid email id 2")
else:
    print("invailid email id 1")
    
