'''
Created on Nov 18, 2018

@author: Mgmi
'''
import datetime

#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
def exercise1():
    print('Enter your name:')
    name=input()
    print('Enter your age:')
    age=int(input())
    today = datetime.date.today()
    if age <=100:
        hundredthyear = today.year + (100-age)
        message = 'Hi ' + name +  ', your 100th birthday will be on ' + str(hundredthyear) 
        print(message)
    else:
        print('Please provide the correct age (<100')

#Take a list and write a program that prints out all the elements of the list that are less than 5.
def exercise2(): 
    print('Enter the numbers separated by a single space') #[5 1 7 3 9 0 6 8]
    input_list = input().split()
    print('List::', input_list)
    temp_func = lambda x : int(x) <= 5
    new_list = list(filter(temp_func, input_list))
    print('New list with elements less than 5: ', new_list)
    
#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
def exercise3():
    print('Enter first list : numbers separated by a single space') #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    input_list1 = input().split() 
    print('Enter second list : numbers separated by a single space')#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    input_list2 = input().split()
    set1 = set(input_list1)
    set2 = set(input_list2)
    print("The elements that are common: ", set1.intersection(set2))
     
    
    
    
if __name__ == '__main__':
    #exercise1()
    #exercise2()
    exercise3()