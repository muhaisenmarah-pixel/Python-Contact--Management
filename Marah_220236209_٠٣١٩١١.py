#Mraha Ratat Muhaisen
#ID=220236209
type_list={"family" , "personal","other"}
i1=-1
choice={}
while True:
            
    print("Welcome to our Address book, please to find what you want\n1. Add new contact.\n2. Search by name.\n3. Search by number. \n4. Delete contact by name.\n5. Delete contact by number.\n6. Show all contacts.\n7. Exit")
    c=input("Please to enter your choice:")   
   
    if c=="1":
            i1+=1
            name=input("Enter your contact name:")
            choice[i1]={"name":name,"number":[],"type":""}
            while True:
                type=input("Enter contact type(family,personal,other):")
                if type in type_list:
                    choice[i1]["type"]=type
                    break
                else:
                    print("Error you should enter correct chioce") 
            while True:
                    num=input("Enter your contact number:")
                    for contact in choice.values():
                        for number in contact["number"]:
                            if number==num:
                                print("This number is exists")
                    else:
                        choice[i1]["number"].append(num)
                        new=input("Do you want enter anther number(t/f):")
                        if new.lower()=="f":
                            print(contact)
                            break
    
    
    elif c=="2":
            name_find=input("Enter name to find:")
            found=False  
        
            for contact in choice.values(): 
                o=0
                count=0
                for caractar in name_find.lower() :
                    if caractar ==contact["name"][o].lower():
                        count+=1  
                        o+=1   
                if count >= len(contact["name"])-1:       
                    print(contact)
                    found=True
            
            if found==False:
                print("contact not found")
    
   
    elif c=="3":
            number_find=input("enter number to find:")
            found=False
            for contact in choice.values():
                if number_find in contact["number"]:
                    print(contact)
                    found=True
            if not found:
                print("not found")
     
     
  
    elif c =="4" :
            name = input("Enter choice name :")
            found=False
            o=-1
            for nam in choice.values() :
                o+=1
                if nam["name"].lower()==name.lower():
                    del choice[o]
                    print("deleted succsicc")
                    found=True           
                    break
            if found==False:
                print("contact not found")        
            
     
    elif c=="5":
            number_find = input("Enter choice number :")
            found=False
            o=-1
            for contact in choice.values():
                o+=1
                if number_find in contact["number"]:
                    del choice[o]
                    print("deleted succsicc")
                    found=True
                
                break
            if found==False:
               print("contact not found") 
                   
    elif c=="6" :
            for all_choice in choice.values():
                 print(all_choice)             
           
    elif c=="7" :
            break
    
    else:
          print("Error enter correct chioce")
               