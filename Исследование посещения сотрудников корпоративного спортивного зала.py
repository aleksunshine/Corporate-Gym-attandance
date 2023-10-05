#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('/Users/cirionstark/Downloads/Массив. Посещение тренажерного зала.xlsx - Worksheet.csv')


# Подсчет общего числа сотрудников

# In[4]:


total_employees = data['ФИО'].nunique()
print(total_employees)


# In[15]:


attendance_counts_by_employee = data[data['Присутcтвовал'] == 'да'].groupby('ФИО').size().reset_index(name='Количество присутствий')
display(attendance_counts_by_employee)


# In[16]:


# Рассчитаем процент посещения для каждого сотрудника
attendance_counts_by_employee['Процент посещения'] = (attendance_counts_by_employee['Количество присутствий'] / total_employees) * 100

# Выведем результат
display(attendance_counts_by_employee)


# In[17]:


# Отсортируйте DataFrame по столбцу "Процент посещения" в убывающем порядке
sorted_attendance = attendance_counts_by_employee.sort_values(by='Процент посещения', ascending=False)

# Выберите первую запись (с наивысшим процентом посещения)
employee_with_highest_attendance = sorted_attendance.iloc[0]

# Выведите информацию о сотруднике с наивысшим процентом посещения
print(employee_with_highest_attendance)


# In[21]:


# Получите имя частопосещаемого зала
most_frequent_gym_name = most_frequent_gym

# Подсчитайте количество раз, которое зал был посещен
count_visits_most_frequent_gym = len(data[(data['Присутcтвовал'] == 'да') & (data['Подразделение уровень 2'] == most_frequent_gym_name)])

# Выведите результат
print("Частопосещаемый зал:", most_frequent_gym_name)
print("Количество посещений:", count_visits_most_frequent_gym)


# In[20]:


# Создайте фильтр для строк, соответствующих частопосещаемому залу
frequent_gym_attendance = data[(data['Присутcтвовал'] == 'да') & (data['Подразделение уровень 2'] == most_frequent_gym_name)]

# Получите список уникальных сотрудников, которые посещали частопосещаемый зал
employees_at_frequent_gym = frequent_gym_attendance['ФИО'].unique()

# Выведите список сотрудников
print("Сотрудники, посещавшие частопосещаемый зал:")
for employee in employees_at_frequent_gym:
    print(employee)

