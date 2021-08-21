#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randint
from tabulate import tabulate
import copy
class Restaurant():
    
    def __init__(self):
        print("Welcome to Edyoda Restaurant!")
        print(' ')
        inp9 = input("Do you want to see menu? Y/N: ")
        print("  ")
        if inp9.lower() == 'y':
            self.menu1()
        else:
            print("You are free to wander!")
    
    def menu1(self):
        key = True
        while key:
            print("  ")
            print('**********************************************')
            print("  ")
            print('Press 1: Register as User')
            print('Press 2: Login')
            print("Press 3: See Menu")
            print("Press 4: Admin Panel")
            print("Press 5: User Panel")
            print("Press 6: Exit!")
            print("  ")
            inp = input("Please Enter your response: ")
            print("  ")
            if inp == '1':
                print("  ")
                print('**********************************************')
                self.signUp()
            elif inp == '2':
                print("  ")
                print('**********************************************')
                self.login()
            elif inp == '3':
                print("  ")
                print('**********************************************')
                self.display_menu()
            elif inp == '4':
                print("  ")
                print('**********************************************')
                print("  ")
                print("You are in Admin Panel") 
                print("Press 1: List all food item")
                print("Press 2: Add new food item")
                print("Press 3: Edit food item")
                print("Press 4: Delete food item")
                print("Press 5: Display all user")
                print(" ")
                input1 = input("Please enter your response: ")
                print(" ")
                if input1 == '1':
                    print("  ")
                    print('**********************************************')
                    self.display_menu()
                elif input1 == '2':
                    print("  ")
                    print('**********************************************')
                    self.addItem()
                elif input1 == '3':
                    print("  ")
                    print('**********************************************')
                    self.editFood()
                elif input1 == '4':
                    print("  ")
                    print('**********************************************')
                    self.removeItem()
                elif input1 == '5':
                    print("  ")
                    self.display_users()
            elif inp == '5':
                print("You are in User Panel")
                print('Press 1: Place New Order')
                print("Press 2: Order History")
                print("Press 3: Update Profile")
                print("  ")
                input2 = input("Please Enter your response: ")
                print("  ")
                if input2 == '1':
                    print("  ")
                    print('**********************************************')
                    self.newOrder()
                elif input2 == '2':
                    print("  ")
                    print('**********************************************')
                    self.orderhistory1()
                elif input2 == '3':
                    print("  ")
                    print('**********************************************')
                    self.updateProfile()
            elif inp == '6':
                print("Thank you!")
                key = False
###########################################################################################################################
    
    def random4digit(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    users = [['Name','Email','Password','Contact Number','Address','Role'], 
             ['Admin', 'admin', 'admin','9999999999','Mumbai,India','Admin']]
    active_user = [['Email', 'Password', 'Role'], ['Email', 'Password', 'Role']]
    menu=[['Sr. no','FoodID','Name','Quantity','Price','Discount','Stock'],
          [1,random4digit(4),'Veg Burger','1 Piece',320,20,9],
          [2,random4digit(4),'Paneer Biryani','300gm',480,30,15],
          [3,random4digit(4),'Truffle Cake','500gm',900,120,5],
          [4,random4digit(4),'Pasta','200gm',250,51,3]]
    orderHistory = [['Email','Name','Price Paid']]
    removedItem = [['FoodID','Name','Quantity','Price','Discount','Stock']]
     
            
    def signUp(self):
        name = input("Enter your Full Name: ")
        contact = input("Enter your Contact no.: ")
        address = input("Enter your Address: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        role = 'User'
        for i in range(len(self.users)):
            if email in self.users[i]:
                print(" ")
                print("User Already Registered")
                break
        else:
            self.users.append([name,email,password,contact,address,role])
            print('User Registered Successfully')
        
    counter1 = 0
        
    def login(self):
        self.email = input("Please enter your registered email: ")
        self.password = input("Please enter your password: ")
        for i in range(len(self.users)):
            if self.email == self.users[i][1] and self.password == self.users[i][2]:
                self.counter1 = 1
                self.active_user.clear()
                self.active_user.append(['Email', 'Password', 'Role'])
                self.active_user.append([self.users[i][1], self.users[i][2], self.users[i][-1]])
                break
            else:
                self.counter1 = 0
        if self.counter1 == 1:
            print("Welcome! You are successfully logged in.")
        elif self.counter1 == 0:
            print("User not found! Please Register.")
            
    def display_menu(self):
        print(tabulate(self.menu, headers='firstrow', tablefmt='fancy_grid'))
        
    def display_users(self):
        if self.active_user[1][2] == "Admin":
            userlistindb = [['Name','Email','Password','Contact Number','Address','Role']]
            for i in range(len(self.users)):
                if self.users[i][-1] == "User":
                    userlistindb.append(self.users[i])
            print(tabulate(userlistindb, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("You need to be Admin to view this feature.")
     
    @classmethod
    def addItem(cls):
        if cls.active_user[1][2] == "Admin":
            srno = len(cls.menu) 
            foodId = cls.random4digit(4)
            foodName = input("Enter the Food Name: ")
            foodQuantity = input("Enter the Food Quantity: ")
            foodPrice= int(input("Enter Food Price: "))
            foodDiscount = int(input("Enter Discount: "))
            foodStock = input("Enter Stock Available: ")
            cls.menu.append([srno,foodId,foodName,foodQuantity,foodPrice,foodDiscount,foodStock])
            print("Food Item added successfully!")
        else:
            print("Please login first")
                
    def removeItem(self):
        if self.active_user[1][2] == "Admin":
            self.display_menu()
            inp1 = input("Enter Food ID to remove item: ")
            for j in range(len(self.menu)):
                if inp1 in self.menu[j]:
                    print(self.menu[j])
                    resp= input("Do you want to remove this item? Y/N: ")
                    if resp.lower() == 'y':
                        removed=self.menu.pop(j)
                        removedItem.append(removed)
                        print("Food Item Removed")
                    else:
                        print("No Worries!")
                    break
            else:
                print("Food Id not valid!")    
        else:
            print("Please Login First.")
            
    def editFood(self):
        if self.active_user[1][2]=='Admin':
            self.display_menu()
            inp2 = int(input("Please enter FoodId to edit: "))
            for i in range(len(self.menu)):
                if inp2 in self.menu[i]:
                    print(self.menu[i])
                    inp3=input("Do you want to edit this food item? Y/N: ")
                    if inp3.lower()=='y':
                        print("Press 1: Edit Name: ")
                        print("Press 2: Edit Quantity: ")
                        print("Press 3: Edit Food Price: ")
                        print("Press 4: Edit Discount: ")
                        print("Press 5: Edit Stock: ")
                        print(" ")
                        inp4 = input("Please enter your response: ")
                        if inp4 == '1':
                            self.menu[i][2] = input("Please enter new name: ")
                            print("Changes Applied")
                        elif inp4 == '2':
                            self.menu[i][2] = input("Please enter new quantity: ")
                            print("Changes Applied")
                        elif inp4 == '3':
                            self.menu[i][2] = int(input("Please enter new price: "))
                            print("Changes Applied")
                        elif inp4 == '4':
                            self.menu[i][2] = int(input("Please enter new discount: "))
                            print("Changes Applied")
                        elif inp4 == '5':
                            self.menu[i][2] = input("Please enter new stock: ")
                            print("Changes Applied")
                    else:
                        print("No worries")
                    break
            else:
                print("Food ID not valid")
        else:
            print("Please login first")
                 
    def newOrder(self):
        if self.active_user[1][2] == "Admin" or self.active_user[1][2] == 'User':
            self.display_menu()
            list1 = ['Name','Quantity','Price','Discount','Final Price']
            present_order = []
            resp1 = list(input("Please enter the Sr. No of food to order: "))
            for i in resp1:
                if i.isnumeric()==False:
                    resp1.remove(i)
            for j in range(0,len(resp1)):
                for i in range(0,len(self.menu)):
                    if int(resp1[j]) == self.menu[i][0]:
                        newlist1 = copy.deepcopy(self.menu[i][2:6])
                        newlist1.append(newlist1[2] - newlist1[3])
                        present_order.append(newlist1)               
            print("You are ordering : ")
            print(tabulate(present_order, headers=list1, tablefmt='fancy_grid'))
            resp2 = input("Do you want to proceed? Y/N: ")
            if resp2.lower()=="y":
                sum1 = 0
                for k in range(len(present_order)):
                    sum1 += present_order[k][-1]


# In[ ]:




