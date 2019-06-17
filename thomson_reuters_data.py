# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:33:34 2019

@author: eunji bang
"""

import pandas as pd
import os
import numpy as np
import eikon as ek
from time import sleep
start_='2015-12-31'
#start_econo='2015-12-25'
start_update='2016-12-14'
end_='2019-04-05'
ek.set_app_key('Plese put your generating API key here')

save_path='C:/Users/User/Desktop/data/'


snp_stock_list=['MSFT.O','AAPL.O','AMZN.O','BRKb','FB.O','JNJ','GOOG.O','XOM','UNH','JPM']
SNP_list=['MICROSOFT','APPLE','AMAZON','BEKSHIRE HATHAWAY','FACEBOOK','JOHNSON & JOHNSON','GOOGLE','EXXON MOBIL','UNITEDHEALTH GROUP','JPMORGAN CHASE']

commodity_list=['CLc1','LCOc1','NGc1','Cc1','KCc1','CCc1','GCc1','SIc1','HGc1','1ZEc1']
commodity_list_name=['WTI','BRENT','NATURAL GAS','CORN','COFFEE','COCOA','GOLD','SILVER','COPPER','ethanol']

others=['KRW=','.STOXX50E','.SPX','.KS11','JPY=','EUR=','CNY=','CAD=']
others_name=['KRW','EURO50','SNP500','KOSPI','JPY','EUR','CNY','CAD']

economic=['CNGDP=ECI','CNPMIB=ECI','CNTRD=ECI','aCNUNRQ','KRGDPA=ECI','JPGDA=ECI','DEGDP=ECI','ITGDR=ECI']
economic_name=['china_gdp','china_pmi','china_tb','china_unem','kr_gdp','jp_gdp','germany_gdp','italy_gdp']
#chnia gdp, pmi, trade balance, unemployment, korea gdp, japan gdp,

stock_list = [snp_stock_list,commodity_list]
stock_list_name = [SNP_list,commodity_list_name]

other_list=[others]
other_list_name=[others_name]


economic_list=[economic]
economic_list_name=[economic_name]

j=0
for i in range(0,len(stock_list)):
    sl = stock_list[i]
    sln = stock_list_name[i]  
    try:

        for j in range(0,len(sln)):
            save=ek.get_timeseries(sl[j],fields=['CLOSE','HIGH', 'LOW', 'OPEN','VOLUME'],start_date=start_, end_date=end_) #STOCK
            save.to_csv(os.path.join(save_path,sln[j]+'.csv'))
            print(sl[j],sln[j])
            sleep(0.1)

            save=ek.get_timeseries(sl[j],fields=['CLOSE','HIGH', 'LOW', 'OPEN','VOLUME'],start_date=start_update, end_date=end_) #STOCK
            save.to_csv(os.path.join(save_path,sln[j]+'_for_update.csv'))

        
        ##############################################################################################################################

    except Exception as e:
        print('Next! My Exception: ',e)
        
j=0
#while True:
for i in range(0,len(other_list)):
    sl = other_list[i]
    sln = other_list_name[i]  
    try:
        
        for j in range(0,len(sln)):
            save=ek.get_timeseries(sl[j],fields=['CLOSE','HIGH', 'LOW', 'OPEN'],start_date=start_, end_date=end_) #STOCK
            save.to_csv(os.path.join(save_path,sln[j]+'.csv'))
            print(sl[j],sln[j])
            sleep(0.1)

            save=ek.get_timeseries(sl[j],fields=['CLOSE','HIGH', 'LOW', 'OPEN'],start_date=start_update, end_date=end_) #STOCK
            save.to_csv(os.path.join(save_path,sln[j]+'_for_update.csv'))
        
        ##############################################################################################################################

    except Exception as e:
        print('Next! My Exception: ',e)

        
j=0
for i in range(0,len(economic_list)):
    sl = economic_list[i]
    sln = economic_list_name[i]

    try:

        for j in range(0,len(sln)):
            print(sl[j],sln[j])
            save=ek.get_timeseries(sl[j],interval='quarterly',start_date=start_, end_date=end_) #STOCK
            save.to_csv(os.path.join(save_path,sln[j]+'.csv'))
            sleep(0.1)
        
        ##############################################################################################################################

    except Exception as e:
        print('Next! My Exception: ',e)
