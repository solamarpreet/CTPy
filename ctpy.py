import requests

class Game(object):
    def __init__(self,url):
        self.server = url
        self.browser = requests.session()
        self.browser.headers['User-Agent']='CTPy 1.0'
        
    def question(self,qnum):
        """This method accepts a question number and returns the question text."""
        url = f"{self.server}/question/{qnum}"
        resp = self.browser.get(url).json()
        qtxt = resp.get("qtext")
        print(qtxt)
        return None        

    def data(self,qnum):
        """This method accepts a question number and returns the data for the question."""
        url = f"{self.server}/question/{qnum}"
        resp = self.browser.get(url).json()
        qdata = resp.get("qdata")
        return qdata  

    def answer(self, qnum, answer):
        """This method accepts two arguments, a question number and the calculated answer."""
        url = f"{self.server}/question/{qnum}"
        ans = {'ans':str(answer).strip()}
        resp = self.browser.post(url, json=ans)
        return resp.json()["check"]
