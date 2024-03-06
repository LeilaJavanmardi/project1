#!/usr/bin/env python
# coding: utf-8

# In[ ]:

### Import Modules
# from functions import * # Import Functions


# pandas library
import pandas as pd 

# python regex library
import re 

# numpy
import numpy as np

# import matplotlib library
from matplotlib import pyplot as plt

#import seaborn
import seaborn as sns


def general_cleaning(df: pd.DataFrame):
    df_2=df.copy()
    df_2.columns= df_2.columns.str.lower().str.replace(' ','_').str.strip()
    df_2.drop_duplicates(inplace=True)
    df_2.reset_index(drop=True,inplace=True)
    return df_2


# In[ ]:


def cleaning_job_title(job_title):
    
    '''
    cleaning the job titles colmun. column name as paramter , uses regex 
    1- casting all the value to a string, cleaning the names
    2-finding the repeated pattern and replacing the values with the dic_values
    '''
    
    #1
    job_title = str(job_title)
    job_title=job_title.strip().lower()
    job_title=job_title.replace(' ','_')

    #2
    patterns = {
    r'.*senior_data.*': 'senior_data_scientist',
    r'(?<!senior_).*data_scienti.*': 'data_scientist',
    r'.*data_analy.*': 'data_analyst',
    r'.*machine_lear.*': 'machine_learning_engineer',
    r'(?i).*data_engine.*': 'data_engineer',
    r'(?i).*manage.*':'data_science_analytics_leadership',
    r'(?i).*computational.*':'computational_scientist',
    
    #r'(?i).+Scientist.+':
    }

    others='others'
    for pattern, replacement in patterns.items():
        if re.match(pattern,job_title):
            return replacement
  
    return  others


# In[ ]:


def cleaning_industry(industry):
    
    '''
    cleaning the industry colmun. column name as paramter , uses regex 
    1- casting all the value to a string, cleaning the names
    2-finding the repeated pattern and replacing the values with the dic_values
    '''
    
    #1
    industry = str(industry)
    industry = industry.strip().lower().replace(' ','_')

    patterns = {
    r'.*IT.*':'IT_services',
    r'.*computer_hardware.*|.*game.*':'computer_hardware_software',
    r'.*Aeros.*':'aerospace_defense',
    r'.*enterprise_soft.*':'enterprise_software_network_solutions ',
    r'.*consul.*':'consulting',
    r'.* pharmace.*|.*health.*': 'healthcare_and_pharmaceuticals',
    r'.*invest.*|.*bank.*|.*capital.*|.*Financ.*':'finance_and_banking',
    r'.*manufac.*':'manufacturing',
    r'.*energy.*|.*utilit.*|.*oil.*':'energy_and_utilities',
    r'.*federal.*|.*regional.*|social_ass.*':'government_public_sector',
    r'.*ship.*|.*transpor.*|rail.*':'transportation_logistics',
    r'.*real_es.*|.*constrcu.*':'real_estate_construction',
    r'.*telecommun.*':'telecommunications_services',
    r'.*internet.*':'internet_telephone_providers',
    r'.*insuranc.*':'insurance_agencies',
    r'.*adverti.*':'advertising_marketing',
    r'.*staffin.*':'staffing_outsourcing'
    }

    conds = [ (True, pattern, replacement) if re.match(pattern, industry) else (False, "", "") for pattern, replacement in patterns.items() ] 
    conds2 = [ c[0] for c in conds ] 
    
    return conds[  conds2.index(True) ][-1] if sum(conds2) > 0 else "others"


# In[ ]:


def cleaning_salary(salary):
    '''
    cleaning the salary colmun. column name as paramter , uses regex 
    1- casting all the value to a string, cleaning the names
    2-finding the repeated pattern and replacing the values with the dic_values

    '''
    
    # Removing '$' and 'K'
    salary = str(salary).replace('$', '').replace('K', '')
    # Removing parenthesis and spaces
    salary = re.sub(r'\(.*\)', '', salary).strip()
    
    patterns = { 
        r'31-56': '30-56',
        r'56-97|66-112|69-116|71-123|79-106': '56-125',
        r'79-147|80-132|87-141|90-109|90-124|95-119|99-132|79-131|75-131|79-133': '75-145',
        r'92-155|91-150|101-165|105-167|110-163|112-116|122-146': '90-170',
        r'124-198|128-201|137-171|138-158': '120-200',
        r'141-225|145-225': '140-225',
        r'212-331': '210-335'
    }
    others = 'not_verified'
    for pattern, replacement in patterns.items():
        if re.match(pattern,salary):
            return replacement

    return  others


# In[ ]:


def cleaning_locations(location):
    location=str(location).lower().strip()
    #location=location.split(',')[0].replace(' ','_')
    return location 

def cleaning_headquarters(location):
    location=str(location).lower().strip()
    #location=location.split(',')[0].replace(' ','_')
    return location 


# In[ ]:


def cleaning_companies(company):
    company=str(company).lower().strip().split('\n')[0]
    return company 

