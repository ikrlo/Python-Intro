#!/usr/bin/env python
# coding: utf-8

# In[18]:


from typing import NamedTuple, List, Optional
from enum import Enum
import csv

Statistic = NamedTuple('Statistic', [('country', str),
                                     ('year', int),
                                     ('expec', float),
                                     ('pop', int),
                                     ('GDP_per_Cap', float)])

s1 = Statistic('Canada', 1952, 68.75, 14785584, 11367.16)

def fn_for_statistic(s: Statistic) -> ...:
    return ...(s.country,
               s.year,
               s.expec,
               s.pop,
               s.GDP_per_Cap)

# List[Statistic]
# interpret a list of statistics

LOS0 = []
LOS1 = [s1]

def fn_for_los(los: List[Statistic]) -> ...:
    # description of the acc
    acc = ... # type: ...
    for s in los:
        acc = ...(fn_for_statistic(s), acc)
    return ...(acc)

def read(filename: str) -> List[Statistic]:
    """    
    reads information from the specified file and returns a list of statistics
    """
#   los contains the result so far
    los = []

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            s = Statistic(row[0], parse_int(row[1]), round(parse_float(row[2]), 2),
                          parse_int(row[3]), round(parse_float(row[4]), 2))
            los.append(s)
    
    return los


# In[19]:


import numpy as np
    
def average_year(los: List[Statistic]) -> float:
    """
    calculates the average year of all statistics
    """
    # total_year stores the sum of the years seen so far
    total_year = 0
    for s in los:
        total_year = total_year + s.year
    
    if len(los) == 0:
        return 0
    else:
        return round(total_year/len(los), 0)
    
def average_expec(los: List[Statistic]) -> float:
    """
    calculates the average life expectancy of all statistics
    """
    # total_expec stores the sum of the expectancies seen so far
    total_expec = 0
    for s in los:
        total_expec = total_expec + s.expec
    
    if len(los) == 0:
        return 0
    else:
        return round(total_expec/len(los), 2)
    
def average_pop(los: List[Statistic]) -> float:
    """
    calculates the average population of all statistics
    """
    # total_expec stores the sum of the populations seen so far
    total_pop = 0
    for s in los:
        total_pop = total_pop + s.pop
    
    if len(los) == 0:
        return 0
    else:
        return round(total_pop/len(los), 0)

def average_GDP(los: List[Statistic]) -> float:
    """
    calculates the average GDP per capita of all statistics
    """
    # total_GDP stores the sum of the GDPs seen so far
    total_GDP = 0
    for s in los:
        total_GDP = total_GDP + s.GDP_per_Cap
    
    if len(los) == 0:
        return 0
    else:
        return round(total_GDP/len(los), 2)


# In[20]:


def variance_year(los: List[Statistic]) -> float:
    """
    calculates the year variance of all statistics
    """
    # total_year_v stores the sum of the year variances seen so far
    total_year_v = 0
    for s in los:
        total_year_v = total_year_v + get_year_difference(sm)
    
    if len(los) == 0:
        return 0
    else:
        return round(total_year_v/len(los), 0)
    
def get_year_difference(s: Statistic) -> float:
    """
    return the difference between the year and the mean
    """
    return (s.year - average_year(los))**2
    
def variance_expec(los: List[Statistic]) -> float:
    """
    calculates the life expectancy variance of all statistics
    """
    # total_expec_v stores the sum of the variance of life expectancies seen so far
    total_expec_v = 0
    for s in los:
        total_expec_v = total_expec_v + get_expec_difference(sm)
    
    if len(los) == 0:
        return 0
    else:
        return round(total_expec_v/len(los), 0)
    
def get_expec_difference(s: Statistic) -> float:
    """
    return the difference between the life expectancy and the mean
    """
    return (s.expec - average_expec(los))**2

def variance_pop(los: List[Statistic]) -> float:
    """
    calculates the population variance of all statistics
    """
    # total_pop_v stores the sum of the variance of populations seen so far
    total_pop_v = 0
    for s in los:
        total_pop_v = total_pop_v + get_pop_difference(sm)
    
    if len(los) == 0:
        return 0
    else:
        return round(total_pop_v/len(los), 0)
    
def get_pop_difference(s: Statistic) -> float:
    """
    return the difference between the populations and the mean
    """
    return (s.pop - average_pop(los))**2

def variance_GDP(los: List[Statistic]) -> float:
    """
    calculates the GDP variance of all statistics
    """
    # total_GDP_v stores the sum of the variance of GDPs seen so far
    total_GDP_v = 0
    for s in los:
        total_GDP_v = total_GDP_v + get_GDP_difference(sm)
    
    if len(los) == 0:
        return 0
    else:
        return round(total_GDP_v/len(los), 0)
    
def get_GDP_difference(s: Statistic) -> float:
    """
    return the difference between the GDP and the mean
    """
    return (s.GDP_per_Cap - average_GDP(los))**2


# In[25]:


def main(filename: str) -> None:
    """
    Reads the file from given filename, produces average and variance for year, life expectancy, 
    population and GDP per capita
    """
    return average_year(los) and average_expec(los) and average_pop(los) and average_GDP(los)
    return variance_year(los) and variance_expec(los) and variance_pop(los) and variance_GDP(los)


# In[24]:


main("gapminder_Canada.csv")


# In[ ]:




