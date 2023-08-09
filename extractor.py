import requests
from bs4 import BeautifulSoup as bs

class Extractor:

    def __init__(self, source) -> None:
        self.ticker = 'appl' #default
        self.url = None
        self.querystring = None
        self.payload = None
        self.headers = None

        self.source = source
        match self.source:
            case 'yfinance':
                self.set_yfinance
            case 'brrg':
                self.set_brreg
            case 'sec':
                self.set_sec
    '''  
    @property
    def source(self):
        match self.source:
            case 'yfinance':
                self.set_yfinance
            case 'brrg':
                self.set_brreg
            case 'sec':
                self.set_brreg
    '''
    @property
    def set_sec(self):
        ''' STAND IN '''
        self.url = f"I AM URL {self.ticker}/"
        self.querystring = {"I AM QUERYSTRING"}
        self.payload = ""
        self.headers = {
            "I AM HEADER"
        }

    @property
    def set_brreg(self):
        ''' STAND IN '''
        self.url = f"https://finance.yahoo.com/quote/{self.ticker}/"
        self.querystring = {"uuid":"47c7bfa6-ec66-3948-8ce3-ca07f3216390,8bbb25f4-59aa-3b64-aa46-2d6636a3f088","appid":"article2_csn","bucket":"HPMODALMAST100,FPSATE101,FPDOGFOOD202,fd-qsp-no-stickyfooter","device":"desktop","features":"enableAdFeedbackV2,enableInArticleAd,enableSlideShowKV,enableVideoDocking,ncp,oathPlayer,outStream,enableXrayTickerEntities,enableXrayNcp,enableXrayHyperloopCards,enableXrayCardsFollowButton,enableAdLiteUpSellFeedback,enableAdSlotsOneSlot,enableSingleSlotting,exposeYctIds,showCommentsIconInShareSec,enableBodySlots,enableContentMeta,enableUpsellFirstArticleOnly,enableStockChart,enableStockChartWatchlist","lang":"en-US","region":"US","site":"finance"}
        self.payload = ""
        self.headers = {
            "authority": "finance.yahoo.com",
            "accept": "*/*",
            "accept-language": "en-NO,en;q=0.9,nb-NO;q=0.8,nb;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "cookie": "A1=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk; EuConsent=CPwPGYAPwPGYAAOACMNBDRCgAAAAAAAAACiQAAAAAABhoAMAAQTFEQAYAAgmKKgAwABBMUA; GUC=AQABCAFk1M1k_0IfaARN&s=AQAAAGfyA8_f&g=ZNOBIA; A3=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk; A1S=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk&j=GDPR; maex=^%^7B^%^22v2^%^22^%^3A^%^7B^%^7D^%^7D; thamba=2; cmp=t=1691587057&j=1&u=1---&v=91; PRF=t^%^3DOBSFX.OL^%^252BGSF.OL^%^252BMOWI.OL^%^252BSALM.OL^%^252BAUSS.OL^%^252BLSG.OL^%^26newChartbetateaser^%^3D0^%^252C1692792357206",
            "pragma": "no-cache",
            "referer": f"https://finance.yahoo.com/quote/{self.ticker}/",
            "sec-ch-ua": "^\^Not/A",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    @property
    def set_yfinance(self):
        self.url = f"https://finance.yahoo.com/quote/{self.ticker}/"
        self.querystring = {"uuid":"47c7bfa6-ec66-3948-8ce3-ca07f3216390,8bbb25f4-59aa-3b64-aa46-2d6636a3f088","appid":"article2_csn","bucket":"HPMODALMAST100,FPSATE101,FPDOGFOOD202,fd-qsp-no-stickyfooter","device":"desktop","features":"enableAdFeedbackV2,enableInArticleAd,enableSlideShowKV,enableVideoDocking,ncp,oathPlayer,outStream,enableXrayTickerEntities,enableXrayNcp,enableXrayHyperloopCards,enableXrayCardsFollowButton,enableAdLiteUpSellFeedback,enableAdSlotsOneSlot,enableSingleSlotting,exposeYctIds,showCommentsIconInShareSec,enableBodySlots,enableContentMeta,enableUpsellFirstArticleOnly,enableStockChart,enableStockChartWatchlist","lang":"en-US","region":"US","site":"finance"}
        self.payload = ""
        self.headers = {
            "authority": "finance.yahoo.com",
            "accept": "*/*",
            "accept-language": "en-NO,en;q=0.9,nb-NO;q=0.8,nb;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "cookie": "A1=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk; EuConsent=CPwPGYAPwPGYAAOACMNBDRCgAAAAAAAAACiQAAAAAABhoAMAAQTFEQAYAAgmKKgAwABBMUA; GUC=AQABCAFk1M1k_0IfaARN&s=AQAAAGfyA8_f&g=ZNOBIA; A3=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk; A1S=d=AQABBHXj1mMCENIj-mcIXtFT35MBTZT5-iIFEgABCAHN1GT_ZPmOb2UBAiAAAAcI1xYhYjCcOsY&S=AQAAAhybOUwfv-7GedLyi6pnnsk&j=GDPR; maex=^%^7B^%^22v2^%^22^%^3A^%^7B^%^7D^%^7D; thamba=2; cmp=t=1691587057&j=1&u=1---&v=91; PRF=t^%^3DOBSFX.OL^%^252BGSF.OL^%^252BMOWI.OL^%^252BSALM.OL^%^252BAUSS.OL^%^252BLSG.OL^%^26newChartbetateaser^%^3D0^%^252C1692792357206",
            "pragma": "no-cache",
            "referer": f"https://finance.yahoo.com/quote/{self.ticker}/",
            "sec-ch-ua": "^\^Not/A",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    def get_req(self,):
        return requests.request("GET", self.url, data=self.payload, headers=self.headers, params=self.querystring)

    def get_legal_name(self, ticker):
        self.ticker = ticker
        self.set_yfinance
        soup = bs(self.get_req().content, 'html.parser')
        element = soup.find_all("h1", {"class": "D(ib) Fz(18px)"})
        start, end =  ">", "("
        return (str(element).split(start))[1].split(end)[0].replace("'","").strip()



