import pandas as pd 
from data_repo import DataRepo as dr
from data_repo import Enterprice
from rates import Rates

COMPEDITOR_PORTFOLIO = []

class EnterpriceValue(Rates):
    def __init__(self, company,): # r, beta): #SHOULD BE REPLACED WITH SUPER 
        '''company = enterprice to valuate'''
        self.company = company
        self.country = company.statistics['country']
        #self.country = r.country
        r = Rates(self.country)
        #self.beta = Beta()
        #self.beta = beta
    


    @property
    def rM(self,):
        roas = [compeditor.statistics['returnOnAssets'] for compeditor in COMPEDITOR_PORTFOLIO]
        return sum(roas)/len(roas)

    @property
    def rE(self,):
        '''Ke cost of equity'''
        return self.Rfm + Beta(self.company).Be * (self.rM - self.Rfm)
    
    @property
    def rE(self,):
        '''Ke cost of equity'''
        return self.Rfm + Beta(self.company).Bd * (self.rM - self.Rfm)
    
    
    def wacc(self, ):
        print(self.company.balance)
        d_e = self.d+self.e
        wacc = ((self.e/d_e)*self.rE) + (self.e/d_e)*(self.rD)*(1-self.tax)
        return 
    

class Beta(Enterprice):

    def __init__(self, company):
        self.company = company

    @property
    def Be(self):
        ''' Beta of Equity '''
        # I ASSUME THAT THIS IS THE RIGHT ONE
        return self.company.statistics['beta']

def main():
    '''
    User requirements:
        in order to use this software you will need:
            - target stock ticker 
            - compeditor stock tickers 
            - stock exchange ticker
            - Full company names or org number
            - nationality
            - 
    '''
    #NOTE: indexes cant be used as compeditor need more work  
    compeditors = {
        'auss':['AUSS','OL'],
        'salm':['SALM','OL'],
        'mowi':['MOWI','OL'],
        'gsf':['GSF','OL'],
        #'obsfx':['OBSFX','OL'],
    }

    for compeditor, val in compeditors.items():
        globals()[compeditor] = Enterprice(val[0], val[1])
        COMPEDITOR_PORTFOLIO.append(globals()[compeditor])
    
    
    lsg = Enterprice('LSG', 'OL')
    
    country = "Norway"
    r = Rates(country)
    #beta = Beta(country)
    E = EnterpriceValue(lsg,)# r, beta)
    print(E.rE)
    
if __name__ == '__main__':
    main()