import pandas as pd 
from data_repo import DataRepo as dr
from data_repo import Enterprice
from rates import Rates

COMPEDITOR_PORTFOLIO = []


class Beta(Enterprice):

    def __init__(self, ):#TARGET):
        self.all_E = False # True if the TARGET is 100% Equity based (no debt)
        '''
        self.TARGET = TARGET
        self.D = self.TARGET.balance['D']
        self.E = self.TARGET.balance['E']
        '''
        #print(self.balance['D'], self.balance['E'])
        self.D = self.balance['D']
        self.E = self.balance['E']
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
        # IF not, then this might also be the Beta for the whole  Bi I think? regardless, its a combined beta for Bd and Be 
        #return self.TARGET.statistics['beta']
        return TARGET.statistics['beta']

    @property
    def Bi(self):
        ''' Beta for investment
            Bi = (Be * wE) + (Bg * wG)
        '''
        return (self.Be * self.wE) + (self.Bd* self.wD)

   
class WeightOf:
    def __init__(self, E, D): # r, beta): #SHOULD BE REPLACED WITH SUPER 
        #print(E,D)
        self.E = E 
        self.D = D

    @property
    #def wE(self, ):
    def equity(self, ):
        ''' weight of equity; how much % of the capital is equity'''
        return  self.E / (self.E + self.D)


    @property
    #def wD(self, ):
    def debt(self, ):
        ''' weight of debt; how much % of the capital is debt
        '''
        return  self.D / (self.E + self.D)


class CapitalCost(Beta, Rates, Enterprice):
    def __init__(self, ): # r, beta): #SHOULD BE REPLACED WITH SUPER 
        '''TARGET = enterprice to valuate'''
        self.country = TARGET.statistics['country']
        '''
            FORTSATT MULGI JEG MÅ GJØRE DET SÅNN
            self.TARGET = TARGET
            self.country = TARGET.statistics['country']
        '''
    
    @property
    def ErM(self,):
        ''' market interest rate'''
        roas = [COMPEDITOR.statistics['returnOnAssets'] for COMPEDITOR in COMPEDITOR_PORTFOLIO]
        return sum(roas)/len(roas)

    @property
    def rE(self,):
        '''Ke: cost of equity'''
        return self.Rfm + (self.Be * (self.ErM - self.Rfm))
        #return self.Rfm + Beta(self.TARGET).Be * (self.rM - self.Rfm)  #Alternative 
    
    @property
    def rD(self,):
        '''Kg: cost of debt'''
        ''' 
            Bd = Bg = DebtBeta
        or
            Kg = Interest Expenses * (1 - Tax Rate)
        '''
        '''
            - Selskapsskatt (Sb) = 0,25
            - Kreditorskatt (Sk) = 0,25
            - Investorskatt (SEd) = 0,11
            - Investorskatt (SEd) = 0,3168 regner med det er det samme som aksjegevinst skatt 
        '''
        return self.Rfm + (self.Bd * (self.ErM - self.Rfm))
        #return self.Rfm + Beta(self.TARGET).Bd * (self.rM - self.Rfm) #Alternative

    @property
    def rU(self,):
        ''' cost of company without debt'''
        # print(self.Rfm)
        # print(self.ErM )
        # print(self.Bu)

        # print((self.ErM  - self.Rfm))
        # print("==========================")
        return self.Rfm * self.Bu * (self.ErM  - self.Rfm)

    @property
    def wacc(self, ):
        w = WeightOf(self.E, self.D ) 
        return ((w.equity)*self.rE) + (w.debt)*(self.rD)*(1-self.tax)
        
        #return ((self.wE)*self.rE) + (self.wD)*(self.rD)*(1-self.tax)
 

#class EnterpriceValue(CapitalCost):
class EnterpriceValue(CapitalCost, Enterprice):
    def __init__(self,): #SHOULD BE REPLACED WITH SUPER 
        '''TARGET = enterprice to valuate'''
        ''' FORTSATT MULGI JEG MÅ GJØRE DET SÅNN
        self.TARGET = TARGET
        self.country = TARGET.statistics['country']
        '''
        self.E, self.D = TARGET.balance['E'], TARGET.balance['D']
        self.country = TARGET.statistics['country']
        
    @property
    def Vm(self, ):
        ''' Value of TARGET '''
        '''
            Vm = Vu + Vx 
            or
            Vm =E(FKS) / ((1+Kwacc)**t)
            or 
            Vm = Vu + PG * N*           [nb: N* = N-stjere]
        '''
        return self.Vu + (self.PG * self.N_star)
    
    @property
    def Vu(self, ):
        ''' Value of TARGET '''
        ''' 
            Vu = SUM : E(FKS) / ((1+Ku)**t)
            or
            (E(OFRS)*(1-Sb)) / Ku      ofrs = ebit
        '''
        ebit = TARGET.income_statement['ebit']
        #return last_fks /((1+self.rU))
        # print(self.rU)
        # print(self.tax, " ", 1-self.tax)
        # print(ebit)
        # print("_________________________")
        #return (ebit*(1-self.tax)) / self.rU
        fks = TARGET.cash_flow['fks']
        return (fks ) / ((1+self.rU)) 

    @property
    def N_star(self,) -> float:
        ''' 
            represents N*, and means "the tax value factor"/"skatteverdifaktoren"
            formula: N* =  1-(1-Sb)*(1-Se)] / (1-Sk) 
            Sb = bedriftskatt? aka vanlig fra regnskapet 
            Se = eierskatt / investorskatt
            Sk = kreditorskatt
        '''
        Sb = self.tax
        Se = self.investor_tax
        Sk = self.tax
        return (1-(1-Sb)*(1-Se)) / (1-Sk) 
    
    @property
    def rX(self, ):
        ''' Kx cost of Renteskattegevinst '''
        '''
            Vx = SUM : E(s*Rt) / (1+Kx)
        '''
        '''kapitalkostnad av: Renteskattegevinst '''
        '''
        = (r * PG * s)/r  = PG*s
        
        '''
        
        #print(TARGET.cash_flow)
        return

    def check_arbitrage_opportunity(self):
        '''
        if left side and right side is NOT equal: then there is a opportunity 

        (Vu/Vm)*Ku + (Vx/Vm)*kx = (E/Vm)*Ke + (G/Vm)*Kg
        '''

    @property
    def Vx(self, ):
        '''kapitalkostnad av: Renteskattegevinst '''
        '''
        = (r * PG * s)/r  = PG*s
        
        '''
        self.tax
        self.i = TARGET.income_statement['interest_expence']

        self.r = self.i/self.D
        print("(",self.r, "*", self.PG,"*", self.tax,")","/",self.r)
        return (self.r*self.PG*self.tax)/self.r #formelen sier self.r men det virker som self.i gir mer mening 


    @property
    def PG(self, ):
        '''
            PG = pålydende gjeld =AKA=> dagens gjeldssum 
        '''
        return TARGET.balance['net_debt'] # kan også være  current debt og logn term debt 














def main():
    '''
    User requirements:
        in order to use this software you will need:
            - target stock ticker 
            - COMPEDITOR stock tickers 
            - stock exchange ticker
            - Full TARGET names or org number
            - nationality
            - 
    '''
    #NOTE: indexes cant be used as COMPEDITOR need more work  

    #ISSUE NOTE: SOLUTION --> I solved the inheritence issue by making the Objects into global variables: TARGET and *COMPEDITORS 

    COMPEDITORs = {
        'auss':['AUSS','OL'],
        'salm':['SALM','OL'],
        'mowi':['MOWI','OL'],
        'gsf':['GSF','OL'],
        #'obsfx':['OBSFX','OL'],
    }

    for COMPEDITOR, val in COMPEDITORs.items():
        globals()[COMPEDITOR] = Enterprice(val[0], val[1])
        COMPEDITOR_PORTFOLIO.append(globals()[COMPEDITOR])
    
    
    global TARGET
    TARGET = Enterprice('lsg', 'OL')
    
    country = "Norway"
    r = Rates(country)
    E = EnterpriceValue()# r, beta)
    print(E.Vu)
    print(E.Vm)

    ##### NOTE NOT CORRECT
    


    #print(E.wacc)
    
if __name__ == '__main__':
    main()


'''


return ((self.E/self.d_e)*self.rE) + (self.D/self.d_e)*(self.rD)*(1-self.tax)
return self.Rfm + self.Beta.Bd * (self.rM - self.Rfm)
return self.Bd
Bu = self.Be
return self.TARGET.statistics['beta']
stat = self.TARGET.info
return self.get_info()

'''