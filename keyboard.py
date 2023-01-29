from time import time
from random import randrange
import pandas as pd
import csv
import os
def acc(sentence, text,score = 0):
    '''check accurate'''
    if len(text) > len(sentence):#ลบตามตัวที่เกิน
        score = len(sentence)-len(text)
    for var in range(len(sentence)):
        if var+1 >len(text):
            break
        if sentence[var] == text[var]:
            score +=1
    acc = score*100/len(sentence)
    return acc

def difficulty():
    '''select diffuclty'''
    lsword = []
    mode = input("SELECT SENTENSE LEVEL :\n[1] SHORT\n[2] MEDIUM\n[3] LONG\nPRESS NUMBER : ")
    if mode == '1':
        mode = 'short'
    elif mode == '2':
        mode = 'normal'
    elif mode == '3':
        mode = 'long'
    else:
        print('\nPlease select again')
        return difficulty()
    with open(mode+'_sen.txt', mode = 'r') as df:
        for var in df:
            lsword.append(var.strip())
    return lsword,mode
'''ต้องแก้'''
def game(username):
    '''main'''
    lsword,mode = difficulty()# list ประโยค ตาม level
    num = randrange(0,len(lsword))#0-19999
    sentence = lsword[num]
    tic = time()
    print('------------------------------------------------------------------------------------------------------')
    print('Test your speed :',sentence)
    text = input('Answer : ')
    toc = time()
    acc2 = acc(sentence, text)
    total = toc - tic#time
    wide = text.split(' ')
    if len(wide) == 1:
        print('Please Try Again')
        quit()
    elif len(text)/len(sentence) < 0.7:
        print('Please Input Full Sentense')
        return
    else:
        wpm = len(wide)*60/total
    x = '%'
    print("Time : %.2f second"%total)
    print("WPM : %.2f"%wpm)
    print("Accurate : %.2f"%acc2 + x)
    stat = (total,acc2,wpm)
    save(username,mode,stat)
    while True:
            print('------------------------------------------------------------------------------------------------------')
            decide = input('WANT TO EXIT ? (Y/N) : ')
            if decide.upper() == 'Y':
                quit()
            elif decide.upper() == 'N':
                break
            else:
                print('PLEASE TRY AGAIN')
            print('------------------------------------------------------------------------------------------------------')

def save(username,mode,stat):
    edited = False
    ls = []
    source = open(mode+' record.csv', mode ='r', newline = '\n')
    edit = open('new.csv', mode ='w', newline = '\n',encoding='UTF8')
    with source, edit:
        f = csv.reader(source)
        edit = csv.writer(edit)
        for var in f:
            if var == ['None','0','0','0','0']:
                edited = True
                text = str('{:.2f} ({:.2f} sec)'.format(stat[2],stat[0]))
                ls = [username,text,text,str(stat[1]),'1']
                edit.writerow()
                ''''''
            elif var[0] == username:
                edited = True
                ls.append(username)
                var1 = var[1].replace(' sec)','').split(' (')
                if float(var1[0])<stat[2] and float(var[3])<stat[1]:
                    high_wpm = '{:.2f} ({:.2f} sec)'.format(stat[2],stat[0])
                    ls.append(high_wpm)
                else:
                    ls.append(var[1])
                total_WPMall = var[2].replace(' sec)','').split(' (')
                avg_WPM = (float(total_WPMall[0])*int(var[4]) + stat[2])/(int(var[4])+1)
                avg_time = (float(total_WPMall[1])*int(var[4])+stat[0])/(int(var[4])+1)
                ans2 = '{:.2f} ({:.2f} sec)'.format(avg_WPM,avg_time)
                avg_acc = (float(var[3])*int(var[4])+stat[1])/(int(var[4])+1)
                ls.append(ans2)
                ls.append('{:.2f}'.format(avg_acc))
                ls.append(str(int(var[4])+1))
                edit.writerow(ls)
                ''''''
            else:#New_data
                edit.writerow(var)
        if edited == False:
            text = str('{:.2f} ({:.2f} sec)'.format(stat[2],stat[0]))
            ls = [username,text,text,str(stat[1]),'1']
            edit.writerow(ls)
        source.close()
    os.remove(mode+' record.csv')
    os.rename('new.csv',mode+' record.csv')

def see(username):
    mode = input("SELECT SENTENSE LEVEL :\n[1] SHORT\n[2] MEDIUM\n[3] LONG\nPRESS NUMBER : ")
    print('------------------------------------------------------------------------------------------------------')
    if mode == '1':
        mode = 'short'
    elif mode == '2':
        mode = 'normal'
    elif mode == '3':
        mode = 'long'
    else:
        print('Please select again')
        print('------------------------------------------------------------------------------------------------------')
        return see(username)
    source = open(mode+' record.csv', mode ='r', newline = '\n')
    with source:
        f = csv.reader(source)
        count = 0
        check = False
        for var in f:
            if count == 0:
                head = list(var)
            if var[0] == username:
                info = list(var)
                check = True
            count += 1
        if check == True:
            for var in range(len(head)):
                print(head[var]+' : '+info[var])
        else:
            print("YOU DIDN'T PLAY THIS MODE BEFORE")
        while True:
            print('------------------------------------------------------------------------------------------------------')
            decide = input('WANT TO EXIT ? (Y/N) : ')
            if decide.upper() == 'Y':
                quit()
            elif decide.upper() == 'N':
                break
            else:
                print('PLEASE TRY AGAIN')
            print('------------------------------------------------------------------------------------------------------')
def start():
    username = input('INPUT USERNAME: ')
    while True:
        print('------------------------------------------------------------------------------------------------------')
        select = input('SELECT MODE : \n[1] PLAY\n[2] STAT\n[3] LOGOUT\n[4] EXIT\nPRESS NUMBER : ')
        print('------------------------------------------------------------------------------------------------------')
        if select == '2':
            see(username)
        elif select == '1':
            game(username)
        elif select == '3':
            start()
            pass
        elif select == '4':
            quit()
        else:
            print("Error : You didn't select")

print('------------------------------------------------------------------------------------------------------')
start()
