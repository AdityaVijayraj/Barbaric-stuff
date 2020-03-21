#This is a library management system with various features to make managing library easier.
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("<<<    LIBRARY MANAGEMENT SYSTEM    >>>")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print()
print()

books={}                    #stores the name and quantity of books
customers={}                #stores the names and information of current customers
customers_permanent=[]      #stores the information of all customers permanently
payment_dues={}             #stores library fine dues


while True:
    print("Actions:")
    print("1 = Book Directory")
    print("2 = Book Issuing Register")
    a=int(input("Enter the action to be performed:"))
    if a==1:
        print("Actions:")
        print("1 = Search a book")
        print("2 = Add or update a book")
        a1=int(input("Enter the action to be performed:"))
        if a1==1:
            while True:
                search=input("Enter the name of the book:")
                search=search.upper()
                search=search.strip()
                for i in books.keys():
                    if i==search:
                        print(books[search]," copies of ",search,"are available.")
                        break
                else:
                    print("The book is not available.")
                ac1=input("Continue searching? (y/n) : ")
                if ac1=="y":
                    continue
                else:
                    break
        elif a1==2:
            while True:
                name=input("Enter the book name:")
                name=name.upper()
                name=name.strip()
                num=int(input("Enter the number of copies:"))
                books1={name:num}
                books.update(books1)
                ac2=input("Continue adding/updating? (y/n) :")
                if ac2=="y":
                    continue
                else:
                    break
        else:
            print("Invalid input")
    elif a==2:
        print("Actions:")
        print("1 = New customer issuing book")
        print("2 = Old customer returning book")
        print("3 = View current customer information")
        print("4 = View customer history")
        b1=int(input("Enter the action to be performed:"))
        if b1==1:
            while True:
                new=input("Enter the name:")
                new=new.upper()
                new=new.strip()
                if new in payment_dues.keys():
                    print("Fine yet to be cleared : Rs",payment_dues[new][1])
                else:
                    info=()    
                    book=input("Book name:")
                    book=book.upper()
                    book=book.strip()
                    day_i=int(input("Date of issueing (only date):"))
                    month_i=input("Month:")
                    day_r=int(input("Date of returning (only date):"))
                    month_r=input("Month:")
                    ph_no=input("Phone number:")
                    info=info+(book,(day_i,month_i),(day_r,month_r),ph_no)
                    c={new:info}
                    c1=(new,info)
                    customers.update(c)
                    customers_permanent.append(c1)
                    books[book]-=1
                    del info
                ac3=input("Continue adding new customer? (y/n) :")
                if ac3=="y":
                    continue
                else:
                    break
        elif b1==2:
            while True:
                c_name=input("Enter the name of customer:")
                c_name=c_name.upper()
                c_name=c_name.strip()
                print(customers[c_name])
                print("Actions:")
                print("1 = Returned on time")
                print("2 = Ruturn delayed")
                b2=int(input("Enter the action to be performed:"))
                if b2==1:
                    books[customers[c_name][0]]+=1
                    del customers[c_name]
                    print("Cleared")
                elif b2==2:
                    fine=0
                    d=int(input("Enter the date (only date):"))
                    n=(d)-(day_r)
                    if n>0 and n<=7:
                        fine=n*5
                    elif n>7 and n<=14:
                        fine=35+((n-7)*10)
                    elif n>14 and n<=21:
                        fine=105+((n-14)*15)
                    elif n>21 and n<=28:
                        fine=210+((n-21)*20)
                    elif n>28:
                        cost=int(input("Enter the cost of the book:"))
                        fine=350+(cost/2) 
                    print("Library fine: Rs",fine)
                    paid=input("Is the fine paid? (y/n) :")
                    if paid=="y":
                        del customers[c_name]
                        if c_name in payment_dues.keys():
                            del payment_dues[c_name]
                        print("Cleared")
                    elif paid=="n":
                        p={c_name:(customers[c_name],fine)}
                        payment_dues.update(p)
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
                ac4=input("Continue updating old customer? (y/n) :") 
                if ac4=="y":
                    continue
                else:
                    break   
        elif b1==3:
            while True:
                view=input("Enter name of customer:")
                view=view.upper()
                view=view.strip()
                print(customers[view])
                ac5=input("Continue viewing customer information? (y/n) :")
                if ac5=="y":
                    continue
                else:
                    break
        elif b1==4:
            while True:
                history=input("Enter the name of customer:")
                history=history.upper()
                history=history.strip()
                for i in customers_permanent:
                    if history==i[0]:
                        print(i)
                ac6=input("Continue viewing customer history? (y/n) :")
                if ac6=="y":
                    continue
                else:
                    break
        else:
            print("Invalid input")
    else:
        print("Invalid input")
    action=input("Do you want to continue? (y/n) : ")
    if action=="y":
        continue
    else:
        print("Exting program. Thanks for using")
        break
