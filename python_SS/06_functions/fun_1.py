# ------positional argument---------

def sum(a,b):
    print(f"this is a sum of :- {a+b} ")
sum(12,12)
## yaha per hum multiple time sum() ko call ker skte he aur a and b ki value change kr skte he
# functions is a reusable thing........


# ------------ keyword argument ----------


def hello(name,age):
    print(f"your name is {name} and your age is {age}")
hello(age=21,name="satyam")  # but mujhe hello() ke ander pehel age dena he frr name
# yaha uper mene pehel age di frr name frr bhi wo pehle name frr age le rha he 
# ishe hi key ko point krke value dene ko keyword argument kehte he 



# --------- default argument -----------

def sum(a,b=564): # ager me is line me a ya b me se kisi ek ko value de do to ushe default value dena bolenge
    print(f"your sum is {a+b}")
sum(65) # ab yaha mujhe sirf a ki value deni he 
# output is :- 629

def sum(a,b=564): # yaha mene B ki value deke rkhi he 
    print(f"your sum is {a+b}")
sum(65) # yaha mene A ki value 65 di he ager B = 50 rkh du to kya b = 564 lega ya b = 50 
# python is a interpreter language isiliye b ki value step by step change ho jayegi.