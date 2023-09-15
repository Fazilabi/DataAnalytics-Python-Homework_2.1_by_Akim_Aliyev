#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Question 1
Write a calculator function for two numbers based on the list of elements and 
mathematical operations provided. The function must accept three lists as input: 
a list of first elements, a list of second elements, and a list of operations 
(eg "plus", "minus", "multiply", "divide", "power"). The function should return 
another list with the results of the calculations. Example: \
num_list1 = [10, 5, 8, 2]\
num_list2 = [2, 3, 1, 5]\
operations_list = ["plus", "multiply", "minus", "power"]-->[12, 15, 7, 32]
'''
def calculator():
    while True:    
        try:
            result_list = []
            list1 = []
            operator = input("please select any operator in list + - * / or ** or press 'q' for quit ")
            if operator=="q":
                print("Calculator stopped")
                break
            if operator not in "+ - * / or ** q :":
                print("please select any operator in list + - * / or ** or press 'q' for quit ")
                break:
# burada break əvəzinə  nə yaza bilərəm ki, yenidən operator seçiminə qayıdıb soruşsun, aşağıdakı list_lenə getməsin? 
            list_len = int(input("enter positive number for lists len : "))
            for i in range(list_len):
                x = int(input(f"enter {i}. elements of first list : "))
                list1.append(x)
            print("list1 :", list1)
            print("-------------------------")
            list2 = []
            for k in range(list_len):
                y = int(input(f"enter {k}. elements of second list : "))
                list2.append(y)
            print("list2 :", list2)
            print("-------------------------")
            if operator=="+":
                for j in range(list_len):
                    result_list.append(list1[j]+list2[j])
            elif operator=="-":
                for j in range(list_len):
                    result_list.append(list1[j]-list2[j])
            elif operator=="*":
                for j in range(list_len):
                    result_list.append(list1[j]*list2[j])
            elif operator=="/":
                for j in range(list_len):
                    result_list.append(list1[j]/list2[j])
            elif operator=="**":
                for j in range(list_len):
                    result_list.append(list1[j]**list2[j])
            elif operator=="q":
                break
            else:print("enter valid operator in list : ")
            print(result_list)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.") 

calculator()


#===========================================================================================================

'''
Question 2
Write a function that takes a string and converts every odd (odd) letter in each word to uppercase. 
Example: func("some sentence for testing")--->SoMe SeNtEnCe FoR TeStInG.
'''
def convert_word_camelcase():
    string1 = input("Enter any string : ")
    for i in range(len(string1)):
        result = ''
        if i%2==0:
            result = string1[i].upper()
            print(result, end="")        
        if i%2==1:
            result = string1[i].lower()
            print(result, end="")
convert_word_camelcase()

#===========================================================================================================
'''
Question 3
Write a function that takes a 2-dimensional square (3x3, 4x4, etc.) array (list of lists) and 
displays the elements below the diagonal and the diagonal itself. Others should be replaced by 0. Example: \
matrix = \
[[1, 2, 3],\
         [4, 5, 6],\
         [7, 8, 9]]\
     -->\
1 0 0 \
4 5 0 \
7 8 9
HINT: pay attention to list indexing.

'''
#===========================================================================================================
'''
Question 4
Write a function that will take a list, multiply all even numbers by 2, divide all odd numbers by 2, 
and find the sum at the end. This function should have 1 line of code. Here you need to use advanced 
Python functions (but there is another option). Example: [1, 2, 3, 4]-->1/2 + 2\*2 + 3/2 + 4\*2=14

'''
def multiply_and_sum_lists_elements():
    while True:
        try:
            list_len = int(input("enter list len : "))
            list1 = []
            odd_list= []
            even_list = []
            for i in range(list_len):
                element = int(input(f"enter {i} list element : "))
                list1.append(element)
            print(list1)    

            result = 0
            for i in list1: 
                if i%2==0:
                    even_list.append(i)
                if i%2==1:  
                    odd_list.append(i)

            for a in range(len(even_list)):
                        result +=even_list[a]*2  
            for b in range(len(odd_list)):
                        result +=odd_list[b]/2
            print(result)
        except:
            print("please enter only number")
multiply_and_sum_lists_elements()

#===========================================================================================================
'''
Question 6
Write a function that will take a date in String format (for example, "May 22, 2023") 
and find the difference between the given date and the current date in year-month-day format.
Example: \ date_str="22 May 2023"\
func(date_str)-->'Difference between 2023-05-22 and today: 0 years, 2 months, 17 days'

'''

from datetime import datetime
from dateutil import relativedelta
def find_diff_between_dates(any_time):
    # get two dates
    today = datetime.now()
    d1 = today.strftime('%d/%m/%Y')
    print(d1)
    d2 = any_time

    # convert string to date object
    start_date = datetime.strptime(d2, "%d/%m/%Y")
    end_date = datetime.strptime(d1, "%d/%m/%Y")

    # Get the relativedelta between two dates
    delta = relativedelta.relativedelta(end_date, start_date)
    print(delta)
    print('Years, Months, Days between two dates is')
    print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')

find_diff_between_dates("19/10/2019")








# In[3]:


a  = range(5)
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




