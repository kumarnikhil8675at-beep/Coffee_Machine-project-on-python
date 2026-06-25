MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources ={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0,
}


def check_amout(menu_item,sum_amount):
    if(MENU[menu_item]["cost"]<=sum_amount):
        return True
    else:
        return False

def user_coin():
       
       Penny=int(input("How many penny?:"))*0.01
       Dime=int(input("How many dime?:"))*0.10
       Nickel=int(input("How many nickel?:"))*0.05
       Quarter=int(input("How many quarters?:"))*0.25
       
       sum_amount=Penny+Dime+Nickel+Quarter
       return sum_amount


def resource_check(menu):
    for item in menu:
        if menu[item]>resources[item]:
            print(f"Sorry there is not engough {item}. Money refunded.")
            return False
    return True

 
def exchange_coin(user_sum,iteam_name):
    a=user_sum-MENU[iteam_name]["cost"]
    if(a!=0):
        return print("here is $",f"{a:.2f}",f"*{round(a,2)}*", "in change.")
    else:
        return print("you total coin is exact value or you coffe")
    

def resource_update(a):
    resources["coffee"]=resources["coffee"]-MENU[a]["ingredients"]["coffee"]
    resources["milk"]=resources["milk"]-MENU[a]["ingredients"]["milk"]
    resources["water"]=resources["water"]-MENU[a]["ingredients"]["water"]
    resources["money"]=resources["money"]+MENU[a]["cost"]
       
        
code=True
while code:
    user=input("What would you like? (espresso/latte/cappuccino):")
    
    if (user=="report"):
        print("Resouces")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources["money"]}")
        
    elif(user=="off"):
        code=False
        
    else:
        try:
            if(resource_check(MENU[user]["ingredients"])):
                user_sum=user_coin()
                if(check_amout(user,user_sum)):
                    exchange_coin(user_sum,user)   
                    print(f"Here is your {user}. Enjou!")
                    resource_update(user)
                else:
                    print("you coin is less for",user)
            else:
                print("resource is less for ", user)
        
        except KeyError:
            print("this type of coffee is not available") 