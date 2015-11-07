#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle
import sys
import re
import math
sys.path.append("../final_project")
from poi_email_addresses import poiEmails
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

len(enron_data)
enron_data.keys()
data1 = enron_data['BIBI PHILIPPE A']
data1.keys()
len(data1)
m=0
for k,v in enron_data.iteritems():
    #print k    
    if v['poi'] == True:
        m = m + 1
print m
emails = poiEmails()
len(emails)
enron_data["PRENTICE JAMES"]["total_stock_value"]
enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
m = 0
for k,v in enron_data.iteritems():
    #print k  
    if math.isnan(float(v['total_payments'])):
        m = m + 1
print m
m=0
for k,v in enron_data.iteritems():
    if v['poi'] and math.isnan(float(v['total_payments'])):
        m = m + 1
print m