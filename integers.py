
# Write a Python function that takes two arguments (a and b) and returns their sum.
def two_args(a,b):
 
    return a+b
a=2
b=5
sum=a+b
print("The sum is :" ,two_args)


# Write a Python function that takes a string as input and returns the string reversed.
def reverse(str):   
    string = "".join(reversed(str))
    return string   
str="read"
print(reverse)


# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def  integers_sum(integers):
    sum_integers=0
    for i in sum_integers:
        sum_integers+=i
        return sum_integers
    integers=[1,2,3,4,5,6]
    print(f"the sum of the list{integers} is {sum(sum_integers)}")


# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even(integers):
    integers=[1,2,3,4,5,6,7,8,9,10]
    for i in integers:
        if i%2==0:
            integers.remove(i)
        print(integers)



# Write a Python function that takes a list of integers as input and returns the highest value in the list.
def highest_value(integers):
    integers=[1,2,3,4,5,6,7,8,9,10]
    length=len(integers)
    value=0
    for i in range(length):
        if(integers[i]>value):
            value=integers[i]
            return value
        print(highest_value)




# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def capitalized(list):
    list=["hello world"]
    for i in list:
        list.capitalize()
        return list
    print(list)




