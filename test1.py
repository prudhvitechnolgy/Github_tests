#Types of functions
#1.without parameters without return values
def welcome_msg():
    print("hello nice to see your!")
    print('welcome to our application')
welcome_msg()
#2.without parameters with return values
def sum_of_first_10_numbers():
    sum=0
    for i in range(1,11):
        sum=sum+i
        return sum
#3.with parameters without return values:
def welcome_user(name,gender):
    if gender=='M':
        print("welcome mr",'have a nice day!')
    else:
        print('welcome mrs','have a nice day!')
    name=input('enter your name')
    gender=input('enter your gender(M/F)')
    welcome_user(name,gender)
#4.with parameters with return values
def get_count(arr,size,target_value):
    cnt=0
    for i in range(0,size):
        if arr[i]==target_value:
            cnt=cnt+1
    return cnt
my_list=[1,2,2,3,3,3,4,5,4,4,4,6,7]
print('1 occurance:',get_count(my_list,len(my_list),1))
print('2 occurance:',get_count(my_list,len(my_list),2))
print('3 occurance:',get_count(my_list,len(my_list),3))