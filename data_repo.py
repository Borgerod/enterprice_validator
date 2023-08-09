import pandas as pd 
import yfinance as yf
from extractor import Extractor

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
    def __init__(self, name, org_num, ticker, exchange, exchange_ticker,) -> None:
        self.name = None #Full legal company name 
        self.org_num = None #organisation number
        self.ticker = None
        self.exchange = None
        self.exchange_ticker = None #e.g. OL for Oslo stock exchange completed ticker will look like e.g. LSG.OL  
        


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
    

if __name__ == '__main__':
    temp_main()
