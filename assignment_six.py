# Owen Feng'''
'''1/19/2023'''
'''this program is about to guess a birthday between 1-365'''

import random

def intro():
    '''
    it's a introduction, how many time to run a function
    :return: the number of time to run the simmulation
    '''
    numberoftimes = input("how many time takes to run")
    return numberoftimes



def getbirthday():
    '''
    the purpose of this function is create 23 list of number represent the number of birthdays
    :return:  the list of 23 numbers.
    '''
    list = []
    for x in range(23):
        list.append(random.randint(1, 366))
        #print(list)
        return(list)



def is_duplicates(list):
    '''
    it can receive a list and teel us if there is duplicates in the lsit
    :param list: it can receive a list
    :return: if it's find a a duplicates, it returns a ture.
    '''
    x = 0
    for num in list:
        x = x + 1
        for days in list {x:23}
            if num == days:
                return True



        print("birthdaylist")
    '''
    counter = 0
    for x in range(0,22)

'''

def main():
    numberoftimes = intro()
    for x in range(numberoftimes)
        list = getbirthday()
        if  is_duplicates(list) == True:
            counter + = 1



main()
