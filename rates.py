import requests
from bs4 import BeautifulSoup
import re

class Rates:
    '''
    raturns different types of public rates, e.g. taxes, risk free rate..
    '''
    def __init__(self, country) -> None:
        self.country = country

    @property
    def tax(self,):
        url = f"https://www.skatteetaten.no/satser/faktor-for-oppjustering-av-gevinsttap-eller-utbytte-pa-aksjer/"
        url = f"https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skattesatser-2023/id2929581/"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        return (float(re.sub(r'[^\x00-\x7F]+',' ', soup.find_all('tr')[3].find_all('td')[1].find('p').text).replace(" pst.","")))/100
    
    @property
    def investor_tax(self,):
        ''' Merk at det er mulig at utbytte må oppjusteres før skatteberegning'''
        return self.tax * self.investor_tax_adjustment_rate
    
    @property
    def investor_tax(self,):
        ''' apparently creditors tax are = to company tax (which do make sence since creditors are companies too)'''
        return self.tax
    

    @property
    def investor_tax_adjustment_rate(self,):
        url = f"https://www.skatteetaten.no/satser/faktor-for-oppjustering-av-gevinsttap-eller-utbytte-pa-aksjer/"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        return  float(soup.select("h2")[0].find_next("p").text.split(" ")[-1].strip(".").replace(",","."))

    @property
    def government_bond_rate(self):
        url = f"http://www.worldgovernmentbonds.com/bond-historical-data/{self.country}/10-years/"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        return (float((soup.find('div', class_="w3-cell font-open-sans").text.strip()).replace("%","")))/100

    @property
    
    def inflation_rate(self):
        url = f"https://tradingeconomics.com/{self.country}/inflation-cpi"
        payload = ""
        headers = {
            "accept": "*/*",
            "cache-control": "no-cache",
            "cookie": "ASP.NET_SessionId=xcapdmpubdkoqfeq3ucxpw5t; TEServer=TEIIS",
            "pragma": "no-cache",
            "sec-ch-ua": "^\^Not/A",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        return (float((soup.find("td", class_="datatable-item datatable-item-positive").text.strip()).replace("%","")))/100

    @property
    def Rfm(self,):
        ''' risk-free rate'''
        # should actually get the propriate bond yield from the security's origin country. (if it even matters)
        return  ((1+self.government_bond_rate)/(1+self.inflation_rate))-1
    
    @property
    def foo(self,):
        foo = ""
        return foo



