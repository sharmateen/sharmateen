import random 
import datetime 

name = [] 
phno = [] 
add = [] 
checkin = [] 
checkout = [] 
room = [] 
price = [] 
rc = [] 
p = [] 
roomno = [] 
custid = [] 
day = [] 
   
i = 0
   
def Home(): 
    print("\t\t**** WELCOME TO WONDERLAND HOTEL***\n") 
    print("   MENU...\n") 
    print("1. Booking") 
    print("2. Room Info") 
    print("3. Restaurant")
    print("4. Payment") 
    print("5. Record") 
    print("0. Exit") 
    ch=int(input("Please choose any one option from above Menu:")) 
      
    if ch == 1: 
        print(" ") 
        Booking() 
      
    elif ch == 2: 
        print(" ") 
        Rooms_Info() 
      
    elif ch == 3: 
        print(" ") 
        restaurant() 
      
    elif ch == 4: 
        print(" ") 
        Payment() 
      
    elif ch == 5: 
        print(" ") 
        Record() 
      
    else: 
        exit() 
        
   
def date(c): 
      
    if c[2] >= 2019 and c[2] <= 2022: 
          
        if c[1] != 0 and c[1] <= 12: 
              
            if c[1] == 2 and c[0] != 0 and c[0] <= 31: 
                  
                if c[2]%4 == 0 and c[0] <= 29: 
                    pass
                  
                elif c[0]<29: 
                    pass
                  
                else: 
                    print("Invalid date\n") 
                    name.pop(i) 
                    phno.pop(i) 
                    add.pop(i) 
                    checkin.pop(i) 
                    checkout.pop(i) 
                    Booking() 
              
              
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31: 
                pass
             
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2: 
                pass
              
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31: 
                pass
              
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:   
                pass
              
            else:  
                print("Invalid date\n") 
                name.pop(i) 
                phno.pop(i) 
                add.pop(i) 
                checkin.pop(i) 
                checkout.pop(i) 
                Booking() 
                  
        else: 
            print("Invalid date\n") 
            name.pop(i) 
            phno.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
              
    else: 
        print("Invalid date\n") 
        name.pop(i) 
        phno.pop(i) 
        add.pop(i) 
        checkin.pop(i) 
        checkout.pop(i) 
        Booking() 
   
   
def Booking(): 
      
        global i 
        print(" BOOKING ROOMS") 
        print(" ") 
          
        while 1: 
            n = str(input("Name: ")) 
            p1 = str(input("Phone No.: ")) 
            a = str(input("Address: ")) 
              
            if n!="" and p1!="" and a!="": 
                name.append(n) 
                add.append(a) 
                break
                  
            else: 
                 print("\tName, Phone no. & Address cannot be empty..!!") 
               
        cii=str(input("Check-In: ")) 
        checkin.append(cii) 
        cii=cii.split('/') 
        ci=cii 
        ci[0]=int(ci[0]) 
        ci[1]=int(ci[1]) 
        ci[2]=int(ci[2]) 
        date(ci) 
           
        coo=str(input("Check-Out: ")) 
        checkout.append(coo) 
        coo=coo.split('/') 
        co=coo 
        co[0]=int(co[0]) 
        co[1]=int(co[1]) 
        co[2]=int(co[2]) 
          
        if co[1]<ci[1] and co[2]<ci[2]: 
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]: 
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        else: 
            pass
          
        date(co) 
        d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
        d2 = datetime.datetime(co[2],co[1],co[0]) 
        d = (d2-d1).days 
        day.append(d) 
           
        print("----SELECT ROOM TYPE----") 
        print(" 1. Standard Non-AC") 
        print(" 2. Standard AC") 
        print(" 3. 3-Bed Non-AC") 
        print(" 4. 3-Bed AC") 
        print(("\t\tPress 0 for Room Prices")) 
          
        ch=int(input("->")) 
        
        if ch==0: 
            print(" 1. Standard Non-AC - Rs. 3500") 
            print(" 2. Standard AC - Rs. 4000") 
            print(" 3. 3-Bed Non-AC - Rs. 4500") 
            print(" 4. 3-Bed AC - Rs. 5000") 
            ch=int(input("->")) 
        if ch==1: 
            room.append('Standard Non-AC') 
            print("Room Type- Standard Non-AC")   
            price.append(3500) 
            print("Price- 3500") 
        elif ch==2: 
            room.append('Standard AC') 
            print("Room Type- Standard AC") 
            price.append(4000) 
            print("Price- 4000") 
        elif ch==3: 
            room.append('3-Bed Non-AC') 
            print("Room Type- 3-Bed Non-AC") 
            price.append(4500) 
            print("Price- 4500") 
        elif ch==4: 
            room.append('3-Bed AC') 
            print("Room Type- 3-Bed AC") 
            price.append(5000) 
            print("Price- 5000") 
        else: 
            print(" Wrong choice..!!") 
   
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
          
          
        while rn in roomno or cid in custid: 
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
              
        rc.append(0) 
        p.append(0) 
                
        if p1 not in phno: 
            phno.append(p1) 
        elif p1 in phno: 
            for n in range(0,i): 
                if p1== phno[n]: 
                    if p[n]==1: 
                        phno.append(p1) 
        elif p1 in phno: 
            for n in range(0,i): 
                if p1== phno[n]: 
                    if p[n]==0: 
                        print("\tPhone no. already exists and payment yet not done..!!") 
                        name.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking() 
        print("") 
        print("\t\t\t**ROOM BOOKED SUCCESSFULLY**\n") 
        print("Room No. - ",rn) 
        print("Customer Id - ",cid) 
        roomno.append(rn) 
        custid.append(cid) 
        i=i+1
        n=int(input("0-BACK\n ->")) 
        if n==0: 
            Home() 
        else: 
            exit() 
  
def Rooms_Info(): 
    print("         ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("STANDARD NON-AC") 
    print("Room amenities include: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water.\n") 
    print("STANDARD NON-AC") 
    print("Room amenities include: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water + Window/Split AC.\n") 
    print("3-Bed NON-AC") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
    print("Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water.\n") 
    print("3-Bed AC") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ") 
    print("1 Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water + Window/Split AC.\n\n") 
    print() 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
  
def restaurant(): 
    ph=int(input("Customer Id: ")) 
    global i 
    f=0
    r=0
    for n in range(0,i): 
        if custid[n]==ph and p[n]==0: 
            f=1
            print("                           Black horse Hotel")
            print("                            Menu Card") 
            print("\n BEVARAGES                            29 Dal Fry................ 140.00") 
            print(" 1  Cold coffee............. 80.00      30 Dal Makhani............ 150.00") 
            print(" 2  Regular Tea............. 20.00      31 Dal Tadka.............. 150.00") 
            print(" 3  Masala Tea.............. 25.00") 
            print(" 4  Coffee.................. 25.00      ROTI") 
            print(" 5  Cold Drink.............. 25.00      32 Garlic Naan............. 25.00")
            print(" 6  Bread Butter............ 30.00      33 Plain Roti.............. 15.00") 
            print(" 7  Bread Jam............... 30.00      34 Butter Roti............. 15.00") 
            print(" 8  Veg. Sandwich........... 50.00      35 Tandoori Roti........... 20.00") 
            print(" 9  Veg. Toast Sandwich..... 50.00      36 Butter Naan............. 20.00") 
            print(" 10  Cheese Toast Sandwich... 70.00") 
            print(" 11 Grilled Sandwich........ 70.00      RICE")  
            print("                                        37 Fried Rice.............. 100.00")
            print(" SOUPS                                  38 Plain Rice.............. 90.00") 
            print(" 12 Mix Vegie Soup......... 110.00      39 Jeera Rice.............. 90.00") 
            print(" 13 Tomato Soup............ 110.00      40 Veg Pulao............... 110.00") 
            print(" 14 Hot & Sour............. 110.00      41 Peas Pulao.............. 110.00") 
            print(" 15 Veg. Noodle Soup....... 110.00") 
            print(" 16 Sweet Corn............. 110.00      SOUTH INDIAN") 
            print(" 17 Veg. Munchow........... 110.00      42 Fried Idli............. 80.00")
            print("                                        43 Plain Dosa............. 100.00") 
            print(" MAIN COURSE                            44 Onion Dosa............. 110.00") 
            print(" 18 Paneer Lababdar........ 110.00      45 Masala Dosa............ 130.00") 
            print(" 19 Shahi Paneer........... 110.00      46 Paneer Dosa............ 130.00") 
            print(" 20 Kadai Paneer........... 110.00      47 Rice Idli.............. 130.00") 
            print(" 21 Handi Paneer........... 120.00      48 Sambhar Vada........... 140.00") 
            print(" 22 Palak Paneer........... 120.00") 
            print(" 23 Chilli Paneer.......... 140.00      ICE CREAM") 
            print(" 24 Matar Mushroom......... 140.00      49 Chocolate............... 60.00")
            print(" 25 Mix Veg................ 140.00      50 Vanilla................. 60.00") 
            print(" 26 Jeera Aloo............. 140.00      51 Strawberry.............. 60.00") 
            print(" 27 Malai Kofta............ 140.00      52 Pineapple............... 60.00") 
            print(" 28 Aloo Matar............. 140.00      53 Butter Scotch........... 60.00") 
            print("Press 0 -to end ") 
            ch=1
            while(ch!=0): 
                  
                ch=int(input(" -> ")) 
                  
                if ch==1 or ch==31 or ch==32: 
                    rs=20
                    r=r+rs 
                elif ch<=4 and ch>=2: 
                    rs=25
                    r=r+rs 
                elif ch<=6 and ch>=5: 
                    rs=30
                    r=r+rs 
                elif ch<=8 and ch>=7: 
                    rs=50
                    r=r+rs 
                elif ch<=10 and ch>=9: 
                    rs=70
                    r=r+rs 
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                    rs=110
                    r=r+rs 
                elif ch<=19 and ch>=18: 
                    rs=120
                    r=r+rs 
                elif (ch<=26 and ch>=20) or ch==42: 
                    rs=140
                    r=r+rs 
                elif ch<=28 and ch>=27: 
                    rs=150
                    r=r+rs 
                elif ch<=30 and ch>=29: 
                    rs=15
                    r=r+rs 
                elif ch==33 or ch==34: 
                    rs=90
                    r=r+rs 
                elif ch==37: 
                    rs=100
                    r=r+rs 
                elif ch<=41 and ch>=39: 
                    rs=130
                    r=r+rs 
                elif ch<=46 and ch>=43: 
                    rs=60
                    r=r+rs 
                elif ch>=50 and ch<=53:
                    rs=60
                    r=r+rs
                elif ch==0: 
                    pass
                else: 
                    print("Wrong Choice..!!") 
            print("Total Bill: ",r) 
             
            r=r+rc.pop(n) 
            rc.append(r)     
        else: 
            pass
    if f == 0: 
        print("Invalid Customer Id") 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
       
                                 
def Payment(): 
      
    ph=str(input("Phone Number: ")) 
    global i 
    f=0
      
    for n in range(0,i): 
        if ph==phno[n] : 
              
            # checks if payment is 
            # not already done 
             if p[n]==0: 
                f=1
                print("PaymENT")
                print("MODE OF PAYMENT") 
                   
                print("1- Credit/Debit Card") 
                print("2- Paytm/PhonePe") 
                print("3- Using UPI") 
                print("4- Cash") 
                f=int(input("-> "))
                print("\n Amount: ",(price[n]*day[n])+rc[n]) 
                print("\n Pay For Black Horse") 
                print("  (y/n)") 
                ch=str(input("->")) 
                  
                if ch=='y' or ch=='Y': 
                    print("\n\n --------") 
                    print("           BLACK HORSE") 
                    print(" --------------------------------") 
                    print("              Bill") 
                    print(" --------------------------------") 
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t") 
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t") 
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t") 
                    print(" Restaurant Charges: \t",rc[n]) 
                    print(" --------------------------------") 
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t") 
                    print(" --------------------------------") 
                    print("          Thank You") 
                    print("          Visit Again :)") 
                    print(" --------------------------------\n") 
                    p.pop(n) 
                    p.insert(n,1) 
                      
                    roomno.pop(n) 
                    custid.pop(n) 
                    roomno.insert(n,0) 
                    custid.insert(n,0) 
                      
             else: 
                  
                for j in range(n+1,i): 
                    if ph==phno[j] : 
                        if p[j]==0: 
                            pass
                          
                        else: 
                            f=1
                            print("\n\tPayment has been Made :)\n\n")  
    if f==0:     
        print("Invalid Customer Id") 
          
    n = int(input("0-BACK\n ->")) 
    if n == 0: 
        Home() 
    else: 
        exit() 
       
def Record(): 
      
    if phno!=[]: 
        print("        * HOTEL RECORD *\n") 
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |") 
        print("----------------------------------------------------------------------------------------------------------------------") 
          
        for n in range(0,i): 
            print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n]) 
          
        print("----------------------------------------------------------------------------------------------------------------------") 
      
    else: 
        print("No Records Found") 
    n = int(input("0-BACK\n ->")) 
    if n == 0: 
        Home() 
          
    else: 
        exit() 
  
Home()
   



