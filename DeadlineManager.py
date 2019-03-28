# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:53:52 2019

@author: Fanhong Li
"""

import os
import time
import datetime
import pandas as pd

print('Hi Daaahai, welcome to your cute deadline manager :)')

if not os.path.exists('Deadline.csv'):
    deadlines = pd.DataFrame(columns=['Task','DueDate','DayLeft','EstimateTime','DailyWorkHours'])
else:
    deadlines = pd.read_csv('Deadline.csv', index_col=0)

while True:
    add = input('Do you have more deadlines?(y/n)')
    if add == 'y':
        Task = input('What\'s the task this time?')
        duedate = input('When should it be finished?(yyyy-mm-dd HH:MM)')
        DueDate = time.strptime(duedate,'%Y-%m-%d %H:%M')
        DayLeft = (time.mktime(DueDate) - time.mktime(time.localtime()))/86400
        EstimateTime = input('How long do you think you\'ll need?(hours)')
        DailyWorkHours = int(EstimateTime)/DayLeft
        deadlines.loc[len(deadlines)]={'Task':Task,'DueDate':DueDate,'DayLeft':DayLeft,'EstimateTime':EstimateTime,'DailyWorkHours':DailyWorkHours}
    else:
        print('\nCongratulations! You only have '+str(len(deadlines))+' deadlines\nn')
        deadlines.sort_values("DayLeft",inplace=True)
        print(deadlines)
        timesum = deadlines['DailyWorkHours'].sum()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
        todayleft = (today_end_time - time.mktime(time.localtime()))/3600
        print('You should work '+'%.1f' %timesum+' hours today, but today ends in '+'%.1f' %todayleft+' hours.')
        deadlines.to_csv('Deadline.csv') #如何记录每次修改
        break