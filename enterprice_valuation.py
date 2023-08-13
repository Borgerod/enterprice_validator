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
        self.E = self.company.balance['E']
        self.D = self.company.balance['D']
        self.Beta = Beta(self.company)
    


    @property
    def rM(self,):
        roas = [compeditor.statistics['returnOnAssets'] for compeditor in COMPEDITOR_PORTFOLIO]
        return sum(roas)/len(roas)

    @property
    def rE(self,):
        '''Ke cost of equity'''
        return self.Rfm + self.Beta.Be * (self.rM - self.Rfm)
        #return self.Rfm + Beta(self.company).Be * (self.rM - self.Rfm)  #Alternative 
    
    @property
    def rD(self,):
        '''Kg cost of debt'''
        ''' Bd = Bg = DebtBeta '''
        return self.Rfm + self.Beta.Bd * (self.rM - self.Rfm)
        #return self.Rfm + Beta(self.company).Bd * (self.rM - self.Rfm) #Alternative

    @property
    def wE(self, ):
        ''' weight of equity; how much % of the capital is equity'''
        return  self.E / (self.E+self.D)


    @property
    def wD(self, ):
        ''' weight of debt; how much % of the capital is debt'''
        return  self.D / (self.E+self.D)

    @property
    def wacc(self, ):
        return ((self.wE)*self.rE) + (self.wD)*(self.rD)*(1-self.tax)
    
    @property
    def Vm(self, ):
        ''' Value of company '''
        return
    
    @property
    def Vu(self, ):
        ''' Value of company '''
        return


    @property
    def Vx(self, ):
        ''' Value of company '''
        return


class Beta(Enterprice):

    def __init__(self, company):
        self.all_E = False # True if the company is 100% Equity based (no debt)
        self.company = company
        self.D = self.company.balance['D']
        self.E = self.company.balance['E']
        self.wD = self.D / (self.E+self.D)
        self.wE = self.E / (self.E+self.D)
    

    @property
    def Bu(self,):
        ''' Beta for selskap uten Gjeld 
        '''
        #self.Bu = self.Be # når det ikke finnes gjeld, så er Be hele Beta for hele selskapet
        return self.Be

    @property
    def Bd(self,):
        ''' Debt Beta
            Be = Bu + ( (G/E) * (Bu+Bg) )
            ==> self.Bd = self.Bu + ( (self.Bu - self.Be) / (self.D/self.E)  )
        '''
        return self.Bu + ( (self.Bu - self.Be) / (self.D/self.E)  )
   
    @property
    def Bg(self,):
        '''bare så det ikke blir forvirring og engelsk og norsk kan forveksles
        '''
        return self.Bd
    
    @property
    def Be(self):
        ''' Beta of Equity 
            self.Be = self.Bu + ((self.D/self.E)*(self.Bu+self.Bg))
        '''
        # I ASSUME THAT THIS IS THE RIGHT ONE
        # IF not, then this might also be the Beta for the whole company, Bi I think? regardless, its a combined beta for Bd and Be 
        return self.company.statistics['beta']

    @property
    def Bi(self):
        ''' Beta for investment
            Bi = (Be * wE) + (Bg * wG)
        '''
        return (self.Be * self.wE) + (self.Bd* self.wD)













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

    print(E.wacc)
    
if __name__ == '__main__':
    main()


'''


return ((self.E/self.d_e)*self.rE) + (self.D/self.d_e)*(self.rD)*(1-self.tax)
return self.Rfm + self.Beta.Bd * (self.rM - self.Rfm)
return self.Bd
Bu = self.Be
return self.company.statistics['beta']
stat = self.company.info
return self.get_info()

'''