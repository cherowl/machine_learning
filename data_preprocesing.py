# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
import re

#https://habrahabr.ru/post/202090/
#https://khashtamov.com/ru/pandas-introduction/
file = open("exN.txt", 'w+')


data = pd.read_csv('data.csv')
#print data.head()
total = data.Name.count()
#print "Total passengers:", total




# --------------------------------------------------------------------------
# ex6 : Какое самое популярное женское имя на корабле? 
data_female = data[data['Sex'] == 'female']['Name']

def get_first_name(x):
    search_parenthes = re.search('\([A-Za-z]*', x) 
    if search_parenthes is not None:
        divide1 = re.split("\(", search_parenthes.group(0))        
        return divide1[1]
    
    searched = re.search('^[A-Za-z]*\,\sMiss.\s[A-Za-z]*\s',x)
    if searched is not None:
        divide2 = re.split("\.\s", searched.group(0))
        return divide2[1]

popular_female_name = data_female.map(lambda x : get_first_name(x)).value_counts().idxmax()

print popular_female_name
file.write(popular_female_name)
# --------------------------------------------------------------------------



# # --------------------------------------------------------------------------
# # ex5 : Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? 
# # Посчитайте корреляцию Пирсона между признаками SibSp и Parch. 
# corr = data['SibSp'].corr(data['Parch'],method = 'pearson')
# file.write(str(corr)+' ')
# # --------------------------------------------------------------------------




# # --------------------------------------------------------------------------
# # ex4 : Какого возраста были пассажиры? Посчитайте среднее и медиану.
# age =  data.Age
# res = age.mean()
# file.write(str(res)+' ')
# res = age.median()
# file.write(str(res))
# # --------------------------------------------------------------------------



# # --------------------------------------------------------------------------
# # ex3 : Какую долю составляли пассажиры первого класса? (%)
# data_class =  data.Pclass.value_counts()
# class_first = data_class.at[1]
# print "Amount passengers from first class: ", class_first

# def percentage(x):
#     x = (x*100.0)/total 
#     return np.round(x, 2)

# res = percentage(class_first)
# print "Percentage: ", res
# file.write(str(res))
# # --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# # ex2 : Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров(%).
# data_survived =  data.Survived.value_counts()
# surv = data_survived.at[1] #equivalent to get_value(1)
# print "Survived: ", surv 

# def percentage(x):
#     x = (x*100.0)/total 
#     return np.round(x, 2)

# res = percentage(surv)
# print "The part of Survived:", res
# file.write(str(res))
# --------------------------------------------------------------------------


# #количество спасшихся и утонувших в зависимости в разрезе классо
# data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked =  True)
# plt.show()


# #предположение про то, что чем выше у пассажиров их социальное положение, тем выше их вероятность спасения
# fig, axes = plt.subplots(ncols=2)
# data.pivot_table('PassengerId', ['SibSp'], 'Survived', 'count').plot(ax=axes[0], title='SibSp')
# data.pivot_table('PassengerId', ['Parch'], 'Survived', 'count').plot(ax=axes[1], title='Parch')
# plt.show()


# --------------------------------------------------------------------------
# # ex1 : male & female 
# d_sex = pd.Series(d['Sex'])
# result = d_sex.value_counts()
# print "Counting male and female\n", result
# result.to_csv("ex.1", sep = ' ')
# --------------------------------------------------------------------------
file.close()