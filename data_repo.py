import pandas as pd 
import yfinance as yf
from extractor import Extractor
from exchange_name_chart import Exchanges as ex

class DataRepo:

    def __init__(self) -> None:
        self.target = None #stands for target company
        self.compeditors = [] #other similar companies
        self.exchange = None
        self.target_w_exchange = None
        self.compeditors_w_exchange = None
        self.portfolio_w_exchange = None


    @property
    def portfolio(self):
        return [self.target] + self.compeditors
    
    def get_historical_data_for(self, arg, exchange=None, simple=True):
        arg = self.check_exchange(arg, exchange)
        if simple:
            return yf.download(arg)['Adj Close']
        else:
            #arg: yf.download(arg) for ticker in arg
            [[arg] if not isinstance(arg, list) else arg]
            print({ticker: yf.download(ticker) for ticker in arg})
            '''
            return { arg: yf.download(arg) for ticker in arg 
            }
            '''
    
    def check_exchange(self, arg, exchange):
        self.exchange = exchange
        if self.exchange:
            if isinstance(arg, list):
                arg = [f"{ticker}.{self.exchange}" for ticker in arg if '.' not in ticker]
            else:
                arg = f"{arg}.{self.exchange}"
        return arg 


    def add_exchange_to_tickers(self) -> None:
        new_tickers = [f"{ticker}.{self.exchange}" for ticker in ([self.target] + self.compeditors) if '.' not in ticker]
        self.target_w_exchange, self.compeditors_w_exchange, self.portfolio_w_exchange = new_tickers[0], new_tickers[1:], new_tickers


    def get_FKS(self, ):
        pass
        

    def get_balance(self):
        pass


class Enterprice:
    def __init__(self, ticker, country=None, exchange=None, exchange_ticker=None,) -> None:
        '''
        yahoo finance uses EOD_codes to differentiate between exchanges, so stocks need identification for that exchange in order to work. 
        '''
        if (ticker, exchange, exchange_ticker,) == None:
            raise ValueError("You need atleast two parameters for this object to work: 1 (the stock ticker), and 2 (either the name of the exchange, or origin country, or the exchange's ticker symbol) ")
        self.exchange_ticker = exchange_ticker
        self.exchange = exchange
        self.country = country
        self.ticker = ex().convert_to_propriate_ticker(ticker=ticker, _input=[i for i in [self.exchange_ticker,self.exchange,self.country] if i][0])
       
        self.iniate_all_properties()
    
    @property
    def statistics(self,):
        stat = self.company.info
        return {
            'ebitda': float(stat['ebitda']),
            'beta': float(stat['beta']),
            'earningsGrowth' : float(stat['earningsGrowth']),
            'debtToEquity' : float(stat['debtToEquity']),
            'dividendRate' : float(stat['dividendRate']),
            'dividendYield' : float(stat['dividendYield']),
            'ebitdaMargins' : float(stat['ebitdaMargins']),
            'enterpriseToEbitda' : float(stat['enterpriseToEbitda']),
            'enterpriseValue' : float(stat['enterpriseValue']),
            'marketCap' : float(stat['marketCap']),
            'operatingCashflow' : float(stat['operatingCashflow']),
            'returnOnAssets' : float(stat['returnOnAssets']),
            'returnOnEquity' : float(stat['returnOnEquity']),
            'revenueGrowth' : float(stat['revenueGrowth']),
            'totalCash' : float(stat['totalCash']),
            'totalDebt' : float(stat['totalDebt']),
            'totalRevenue' : float(stat['totalRevenue']),
            'country' : stat['country'],
            'fks': stat['freeCashflow'],
        }
    @property
    def balance (self, ):
        return {
            'A' : float(self.company.balance_sheet.loc['Total Assets'][0]),
            'E' : float(self.company.balance_sheet.loc['Total Equity Gross Minority Interest'][0]),
            'D' : float(self.company.balance_sheet.loc['Total Liabilities Net Minority Interest'][0]),
            'net_debt': float(self.company.balance_sheet.loc['Net Debt'][0]),
        }
    
    @property
    def analysis (self, ):
        pass
        '''return {
            '' : float(self.company._analysis.loc[''][0]),
            '' : float(self.company._analysis.loc[''][0]),
            '' : float(self.company._analysis.loc[''][0]),
        }'''

    @property
    def income_statement (self, ):
        #orint(self.company.income_stmt)
        return {
            'interest_expence' : float(self.company.income_stmt.loc['Interest Expense'][0]),
            'ebit' : float(self.company.income_stmt.loc['EBIT'][0]),
        }


    @property
    def cash_flow (self, ):
        #return self.company.cashflow
        return {
            'fks' : float(self.company.cashflow.loc['Free Cash Flow'][0]),
        }

    def iniate_all_properties(self):
        self.company = yf.Ticker(self.ticker)
        self.statistics
        self.balance
        self.analysis
        
    def check_exchange(self, arg, exchange):
        # DEPRICATED
        self.exchange = exchange
        
        if self.exchange:
            if isinstance(arg, list):
                arg = [f"{ticker}.{self.exchange}" for ticker in arg if '.' not in ticker]
            else:
                arg = f"{arg}.{self.exchange}"
        return arg 
    

    def set_statistics(self):
        self.statistics['EBIDTA'] = 69









def temp_main():
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
    dr = DataRepo()
    lsg = yf.Ticker("LSG.OL")
    #pprint(lsg.info)
    Lsg = Enterprice('Lerøy Seafood Group ASA', '975350940', 'LSG', 'Oslo', 'OL')
    #Lsg = Enterprice("LSG.OL")
    print(Lsg.statistics['EBITDA'])



    #print(lsg.info['ebitda'])
    '''
    dr.compeditors = ['AUSS', 'NVMI', 'SALM', 'MOWI', 'GSF', 'OBSFX']
    dr.target = 'LSG'
    target = Enterprice('Lerøy Seafood Group ASA', '975350940', 'LSG', 'Oslo', 'OL')
    compeditors = {
        'AUSS' : Enterprice('Austevol', '975350940', 'AUSS', 'Oslo', 'OL'),
        'NVMI' : Enterprice('Lerøy Seafood Group ASA', '975350940', 'NVMI', 'Oslo', 'OL'),
        'SALM' : Enterprice('Lerøy Seafood Group ASA', '975350940', 'SALM', 'Oslo', 'OL'),
        'MOWI' : Enterprice('Lerøy Seafood Group ASA', '975350940', 'MOWI', 'Oslo', 'OL'),
        'GSF' : Enterprice('Lerøy Seafood Group ASA', '975350940', 'GSF', 'Oslo', 'OL'),
        'OBSFX' : Enterprice('Lerøy Seafood Group ASA', '975350940', 'OBSFX', 'Oslo', 'OL'),
    }
    #print(dr.get_historical_data_for(dr.portfolio, 'OL', simple=False))

    ticker = "GSF.OL"
    yahoo = Extractor('yfinance')
    name = yahoo.get_legal_name(ticker, )
    print(name)
    '''

if __name__ == '__main__':
    temp_main()
