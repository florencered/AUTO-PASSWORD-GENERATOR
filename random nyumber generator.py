import random 
print("Hi I am lacy,welcome to random password generator!!")
l=int(input("Enter the number of letters to be included: ")) 
d=int(input("Enter the number of digits to be included: "))
s=int(input("Enter the number of symbols to be included: ")) 
new_list=[]
mypass=[]
list_sym=[]
a=0
list_letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"
             "S","T",'U','V',"W","X","Y",'Z',"a","b","c","d","e",'f',"g","h",
             "i","j","k","l","m","n","o","p","q","r","s","t","u","v",'w',"x","y",'z']
random.shuffle(list_letter)
list_digit=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(list_digit) 
str_symbol='!@#$%^&*()'
new_symbol=str_symbol[0:s]
for i in new_symbol:
    list_sym.append(i) 
random.shuffle(list_sym)
    


new_list=list_letter[0:l]+list_digit[0:d]+list_sym

#list_symbol[0:s]  
random.shuffle(new_list) 
mypass=new_list[0:] 

print("Auto generated Password is:")
for item in mypass:
    
    print(item,end='')
    

