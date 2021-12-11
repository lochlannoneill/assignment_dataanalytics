# -*- coding: utf-8 -*-
"""
Created on a cloudy day
@author: Lochlann O Neill
@id: R00175741
@Cohort: Group A, subgroup A1
"""

#To Do:
    #tidy file more readable
    #task 4
    
    
    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

    

df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')


def Task1(): #working properly
    df['color'] = df['color'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df_bw = df[df['color'] == "Black and White"].reset_index()
    a = df_bw.groupby(['actor_1_name'])['movie_title'].count().to_frame().reset_index()
    a.columns = ['Actor', 'Count']
    actors = a[a['Count'] >= 2].reset_index(drop=True)
    print(actors)

def Task2():#working
    duration = df[df['duration'] > 150]
    df_c = duration[duration['language'] != 'English'].reset_index(drop=True)
    print(df_c['country'])

def Task3():#working
    df['gross'] = df['gross'].fillna(df['gross'].mean())
    g = df.groupby('title_year')['gross'].sum().to_frame().reset_index()
    g = g.sort_values(by='title_year')
    plt.xlabel("Year")
    plt.title("Gross Amount by Year")
    plt.ylabel("Gross Amount")
    plt.bar(x=g['title_year'], height=g['gross'])
    plt.show()

def Task4(): #--------------------------TO DO_____________________________
    df['gross'].dropna(inplace=True)
    df['budget'].dropna(inplace=True)
    df_y = df[df['title_year'] > 1989].reset_index(drop=True)
    lst = []
    for i in range(len(df_y)):
        if df_y['gross'][i] > (df_y['budget'][i] * 2):
            # print(1)
            lst.append(i)
    df_bud = df_y.iloc[lst]
    years = df_y['title_year'].value_counts().to_frame().reset_index()
    years.columns = ['year', 'count']
    years = years.sort_values(by="year").reset_index(drop=True)
    years1 = df_bud['title_year'].value_counts().to_frame().reset_index()
    years1.columns = ['year', 'count']
    
    # years =
    
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.bar(x=years['year'], color='blue')
    plt.show()

def Task5(): #working
    n = df['country'].value_counts().to_frame().reset_index()[2:]
    n.columns = ['country', 'count']
    
    n = n[n['count'] > 30] #usa and uk not considered under 30
    sum = n['count'].sum()
    n['percent'] = n['count'].apply(lambda x: round((x * 100) / sum), 2)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(n['country'], n['count'])
    for i, v in enumerate(n['percent']):
        ax.text(v + 3, i + .10, str(v), color='white', fontweight='bold')

    plt.show()


def Task6():#working
    df['duration'].dropna(inplace=True)
    df['duration'].value_counts()
    plt.hist(df['duration'])
    plt.xlabel("Duration")
    plt.grid()
    plt.show()

    #the most common movie length is 90 mins


def main():
    #Task1()
    #Task2()
    #Task3()
    Task4()
    #Task5()
    #Task6()
    
main()




