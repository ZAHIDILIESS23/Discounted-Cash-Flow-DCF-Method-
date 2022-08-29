#!/usr/bin/env python
# coding: utf-8

# In[232]:


import requests
import numpy as np
import pandas as pd


# In[270]:


company='GOOG'
IS=requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey=5440fa1b83055823728a35b8988f31eb').json()
revenue_g=(IS[0]['revenue']-IS[1]['netIncome'])/ IS[1]['revenue']# revenue growth
net_income=IS[0]['netIncome']
BS=requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?apikey=5440fa1b83055823728a35b8988f31eb').json()


# In[271]:


income_statement=pd.DataFrame.from_dict(IS[0],orient='index')
income_statement=income_statement[8:36]
income_statement.columns=['current_year']
income_statement['as_%_of_revenue']=income_statement/income_statement.iloc[0]
income_statement['next_year']=(income_statement['current_year']['revenue']*(1+revenue_g))*income_statement['as_%_of_revenue']
income_statement['next_2_year']=(income_statement['next_year']['revenue']*(1+revenue_g))*income_statement['as_%_of_revenue']
income_statement['next_3_year']=(income_statement['next_2_year']['revenue']*(1+revenue_g))*income_statement['as_%_of_revenue']
income_statement['next_4_year']=(income_statement['next_3_year']['revenue']*(1+revenue_g))*income_statement['as_%_of_revenue']
income_statement['next_5_year']=(income_statement['next_4_year']['revenue']*(1+revenue_g))*income_statement['as_%_of_revenue']


# In[272]:


balance_sheet=pd.DataFrame.from_dict(BS[0],orient='index')
balance_sheet=balance_sheet[8:52]
balance_sheet.columns=['current_year']
balance_sheet.columns=['current_year']
balance_sheet['as_%_of_revenue']=balance_sheet/income_statement['current_year'].iloc[0]
# forecasting the next 5 years balance sheet
balance_sheet['next_year']=income_statement['next_year']['revenue']*balance_sheet['as_%_of_revenue']
balance_sheet['next_2_year']=income_statement['next_2_year']['revenue']*balance_sheet['as_%_of_revenue']
balance_sheet['next_3_year']=income_statement['next_3_year']['revenue']*balance_sheet['as_%_of_revenue']
balance_sheet['next_4_year']=income_statement['next_4_year']['revenue']*balance_sheet['as_%_of_revenue']
balance_sheet['next_5_year']=income_statement['next_5_year']['revenue']*balance_sheet['as_%_of_revenue']
income_statement


# ## forecast the next 5 year

# In[273]:


CF_forecast={}
CF_forecast['next_year']={}
CF_forecast['next_year']['net_Income']=income_statement['next_year']['netIncome']
CF_forecast['next_year']['inc_depreciation']=income_statement['next_year']['depreciationAndAmortization']-income_statement['current_year']['depreciationAndAmortization']
CF_forecast['next_year']['inc_receivables']=balance_sheet['next_year']['netReceivables']-balance_sheet['current_year']['netReceivables']
CF_forecast['next_year']['inc_inventory']=balance_sheet['next_year']['inventory']-balance_sheet['current_year']['inventory']
CF_forecast['next_year']['inc_payables']=balance_sheet['next_year']['accountPayables']-balance_sheet['current_year']['accountPayables']
CF_forecast['next_year']['CF_operations']=CF_forecast['next_year']['net_Income']+CF_forecast['next_year']['inc_depreciation']+(CF_forecast['next_year']['inc_receivables']*-1)+(CF_forecast['next_year']['inc_inventory']*-1)+(CF_forecast['next_year']['inc_payables']*-1)
CF_forecast['next_year']['CAPEX']=balance_sheet['next_year']['propertyPlantEquipmentNet']-balance_sheet['current_year']['propertyPlantEquipmentNet']
CF_forecast['next_year']['FCF']=CF_forecast['next_year']['CAPEX']+CF_forecast['next_year']['CF_operations']


# In[274]:


CF_forecast['next_2_year']={}
CF_forecast['next_2_year']['net_Income']=income_statement['next_2_year']['netIncome']
CF_forecast['next_2_year']['inc_depreciation']=income_statement['next_2_year']['depreciationAndAmortization']-income_statement['next_year']['depreciationAndAmortization']
CF_forecast['next_2_year']['inc_receivables']=balance_sheet['next_2_year']['netReceivables']-balance_sheet['next_year']['netReceivables']
CF_forecast['next_2_year']['inc_inventory']=balance_sheet['next_2_year']['inventory']-balance_sheet['next_year']['inventory']
CF_forecast['next_2_year']['inc_payables']=balance_sheet['next_2_year']['accountPayables']-balance_sheet['next_year']['accountPayables']
CF_forecast['next_2_year']['CF_operations']=CF_forecast['next_2_year']['net_Income']+CF_forecast['next_2_year']['inc_depreciation']+(CF_forecast['next_2_year']['inc_receivables']*-1)+(CF_forecast['next_2_year']['inc_inventory']*-1)+(CF_forecast['next_2_year']['inc_payables']*-1)
CF_forecast['next_2_year']['CAPEX']=balance_sheet['next_2_year']['propertyPlantEquipmentNet']-balance_sheet['next_year']['propertyPlantEquipmentNet']
CF_forecast['next_2_year']['FCF']=CF_forecast['next_2_year']['CAPEX']+CF_forecast['next_2_year']['CF_operations']
CF_forecast['next_2_year']


# In[275]:


CF_forecast['next_3_year']={}
CF_forecast['next_3_year']['net_Income']=income_statement['next_3_year']['netIncome']
CF_forecast['next_3_year']['inc_depreciation']=income_statement['next_3_year']['depreciationAndAmortization']-income_statement['next_2_year']['depreciationAndAmortization']
CF_forecast['next_3_year']['inc_receivables']=balance_sheet['next_3_year']['netReceivables']-balance_sheet['next_2_year']['netReceivables']
CF_forecast['next_3_year']['inc_inventory']=balance_sheet['next_3_year']['inventory']-balance_sheet['next_2_year']['inventory']
CF_forecast['next_3_year']['inc_payables']=balance_sheet['next_3_year']['accountPayables']-balance_sheet['next_2_year']['accountPayables']
CF_forecast['next_3_year']['CF_operations']=CF_forecast['next_3_year']['net_Income']+CF_forecast['next_3_year']['inc_depreciation']+(CF_forecast['next_3_year']['inc_receivables']*-1)+(CF_forecast['next_3_year']['inc_inventory']*-1)+(CF_forecast['next_3_year']['inc_payables']*-1)
CF_forecast['next_3_year']['CAPEX']=balance_sheet['next_3_year']['propertyPlantEquipmentNet']-balance_sheet['next_2_year']['propertyPlantEquipmentNet']
CF_forecast['next_3_year']['FCF']=CF_forecast['next_3_year']['CAPEX']+CF_forecast['next_3_year']['CF_operations']


# In[276]:


CF_forecast['next_4_year']={}
CF_forecast['next_4_year']['net_Income']=income_statement['next_4_year']['netIncome']
CF_forecast['next_4_year']['inc_depreciation']=income_statement['next_4_year']['depreciationAndAmortization']-income_statement['next_3_year']['depreciationAndAmortization']
CF_forecast['next_4_year']['inc_receivables']=balance_sheet['next_4_year']['netReceivables']-balance_sheet['next_3_year']['netReceivables']
CF_forecast['next_4_year']['inc_inventory']=balance_sheet['next_4_year']['inventory']-balance_sheet['next_3_year']['inventory']
CF_forecast['next_4_year']['inc_payables']=balance_sheet['next_4_year']['accountPayables']-balance_sheet['next_3_year']['accountPayables']
CF_forecast['next_4_year']['CF_operations']=CF_forecast['next_4_year']['net_Income']+CF_forecast['next_4_year']['inc_depreciation']+(CF_forecast['next_4_year']['inc_receivables']*-1)+(CF_forecast['next_4_year']['inc_inventory']*-1)+(CF_forecast['next_4_year']['inc_payables']*-1)
CF_forecast['next_4_year']['CAPEX']=balance_sheet['next_4_year']['propertyPlantEquipmentNet']-balance_sheet['next_3_year']['propertyPlantEquipmentNet']
CF_forecast['next_4_year']['FCF']=CF_forecast['next_4_year']['CAPEX']+CF_forecast['next_4_year']['CF_operations']


# In[277]:


CF_forecast['next_5_year']={}
CF_forecast['next_5_year']['net_Income']=income_statement['next_5_year']['netIncome']
CF_forecast['next_5_year']['inc_depreciation']=income_statement['next_5_year']['depreciationAndAmortization']-income_statement['next_4_year']['depreciationAndAmortization']
CF_forecast['next_5_year']['inc_receivables']=balance_sheet['next_5_year']['netReceivables']-balance_sheet['next_4_year']['netReceivables']
CF_forecast['next_5_year']['inc_inventory']=balance_sheet['next_5_year']['inventory']-balance_sheet['next_4_year']['inventory']
CF_forecast['next_5_year']['inc_payables']=balance_sheet['next_5_year']['accountPayables']-balance_sheet['next_4_year']['accountPayables']
CF_forecast['next_5_year']['CF_operations']=CF_forecast['next_5_year']['net_Income']+CF_forecast['next_5_year']['inc_depreciation']+(CF_forecast['next_5_year']['inc_receivables']*-1)+(CF_forecast['next_5_year']['inc_inventory']*-1)+(CF_forecast['next_5_year']['inc_payables']*-1)
CF_forecast['next_5_year']['CAPEX']=balance_sheet['next_5_year']['propertyPlantEquipmentNet']-balance_sheet['next_4_year']['propertyPlantEquipmentNet']
CF_forecast['next_5_year']['FCF']=CF_forecast['next_5_year']['CAPEX']+CF_forecast['next_5_year']['CF_operations']


# ## Convert to pandas

# In[278]:


CF_forecast=pd.DataFrame.from_dict(CF_forecast,orient='columns')

pd.options.display.float_format='{:.0f}'.format
CF_forecast


# ## Discount the FCF

# In[279]:


import pandas_datareader.data as web
import datetime
import requests
def interest_coverage_and_RF(company):
    IS=requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey=5440fa1b83055823728a35b8988f31eb').json()
    EBIT=IS[0]['ebitda']-IS[0]['depreciationAndAmortization']
    interest_expense=IS[0]['interestExpense']
    interest_coverage_ratio=EBIT/interest_expense
    # RF
    start=datetime.datetime(2020,7,10)
    end=datetime.datetime.today()
    Treasury=web.DataReader(['TB1YR'],'fred',start,end)
    RF=float(Treasury.iloc[-1])
    RF=RF/100
    print(RF,interest_coverage_ratio)
    return [RF,interest_coverage_ratio]
interest=interest_coverage_and_RF(company)
RF=interest[0]
interest_coverage_ratio=interest[1]
def cost_of_debt(company,RF,interest_coverage_ratio):
    if interest_coverage_ratio>8.5:
        # Rating AAA
        credit_spread=0.0063
    if(interest_coverage_ratio>6.5)&(interest_coverage_ratio<=8.5):
        # Rating AA
        credit_spread=0.0078
    if(interest_coverage_ratio>5.5)&(interest_coverage_ratio<=6.5):
        # Rating A+
        credit_spread=0.0098
    if(interest_coverage_ratio>4.25)&(interest_coverage_ratio<=5.49):
        # Rating A
        credit_spread=0.0108
    if(interest_coverage_ratio>3)&(interest_coverage_ratio<=4.25):
        # Rating $A-
        credit_spread=0.0122
    if(interest_coverage_ratio>2.5)&(interest_coverage_ratio<=3):
        # Rating BBB
        credit_spread=0.0156
    if(interest_coverage_ratio>2.25)&(interest_coverage_ratio<=2.5):
        # Rating BB+
        credit_spread=0.02
    if(interest_coverage_ratio>2)&(interest_coverage_ratio<=2.25):
        # Rating BB
        credit_spread=0.0240
    if(interest_coverage_ratio>1.75)&(interest_coverage_ratio<=2):
        # Rating B+
        credit_spread=0.0351
    if(interest_coverage_ratio>1.5)&(interest_coverage_ratio<=1.75):
        # Rating B
        credit_spread=0.0421
    if(interest_coverage_ratio>1.25)&(interest_coverage_ratio<=1.5):
        # Rating B-
        credit_spread=0.0515
    if(interest_coverage_ratio>0.8)&(interest_coverage_ratio<=1.25):
        # Rating CCC
        credit_spread=0.0820
    if(interest_coverage_ratio>0.65)&(interest_coverage_ratio<=0.8):
        # Rating CC
        credit_spread=0.0864
    if(interest_coverage_ratio>0.2)&(interest_coverage_ratio<=0.65):
        # Rating C
        credit_spread=0.1134
    if(interest_coverage_ratio<=0.2):
        # Rating D
        credit_spread=0.1512
    cost_of_debt=RF+credit_spread
    print(cost_of_debt)
    return cost_of_debt
kd=cost_of_debt(company,RF,interest_coverage_ratio)
def cost_of_equity(company):
    # RF
    start=datetime.datetime(2020,7,10)
    end=datetime.datetime.today()
    Treasury=web.DataReader(['TB1YR'],'fred',start,end)
    RF=float(Treasury.iloc[-1])
    RF=RF/100
    # BETA
    beta=requests.get(f'https://financialmodelingprep.com/api/v3/company/profile/{company}?apikey=5440fa1b83055823728a35b8988f31eb')
    beta=beta.json()
    beta=float(beta['profile']['beta'])
    # market return
    start=datetime.datetime(2020,7,10)
    end=datetime.datetime.today()
    SP500=web.DataReader(['SP500'],'fred',start,end)
    SP500yearlyreturn=(SP500['SP500'].iloc[-1]/SP500['SP500'].iloc[-252])-1
    cost_of_equity=RF+(beta*(SP500yearlyreturn-RF))
    print(cost_of_equity)
    return cost_of_equity
ke=cost_of_equity(company)
def wacc(company):
    FR=requests.get(f'https://financialmodelingprep.com/api/v3/ratios//{company}?apikey=5440fa1b83055823728a35b8988f31eb').json()
    ETR=FR[0]['effectiveTaxRate']
    
    # capital structure
    BS=requests.get(f'https://fmpcloud.io/api/v3/balance-sheet-statement/{company}?limit=120&apikey=03143675d8f041d214b19231424e0527').json()
    debt_to=BS[0]['totalDebt']/(BS[0]['totalDebt']+BS[0]['totalStockholdersEquity'])
    equity_to=BS[0]['totalStockholdersEquity']/(BS[0]['totalDebt']+BS[0]['totalStockholdersEquity'])
    # WACC
    WACC=((kd*(1-ETR)*debt_to)+(ke*equity_to))*-1
    print(WACC,equity_to,debt_to)
    return WACC
WACC=wacc(company)
print('WACC  of   ' + company +' is   '+str(WACC*100)+'%')


# In[280]:


FCF_List=CF_forecast.iloc[-1].values.tolist()
import numpy_financial as npf
npv=npf.npv(WACC,FCF_List)
npv


# In[281]:


LTgrowth=0.002
Terminal_values=(CF_forecast['next_5_year']['FCF']*(1+LTgrowth))/(WACC-LTgrowth)
Terminal_values_discounted=Terminal_values/(1+WACC)**4
Terminal_values_discounted


# In[282]:


target_equity_value=Terminal_values_discounted+npv
debt=balance_sheet['current_year']['totalDebt']
target_value=target_equity_value-debt
number_of_shares=requests.get(f'https://financialmodelingprep.com/api/v3/enterprise-values/{company}?apikey=5440fa1b83055823728a35b8988f31eb').json()
number_of_shares=number_of_shares[0]['numberOfShares']
target_price_per_share=target_value/number_of_shares
target_price_per_share


# In[283]:


print(number_of_shares)


# In[ ]:




