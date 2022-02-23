import requests

class Game():
    def __init__(self,url):
        self.server = url
        self.browser = requests.session()
        self.browser.headers['User-Agent']='CTPy 1.0'
        
    def question(self,qnum):
        """This method accepts a question number and prints the question text."""
        url = f"{self.server}/question/{qnum}"
        resp = self.browser.get(url)
        if resp.status_code == 404:
            print('404 error. There is no question with that number. Either you completed all the challenges or entered an incorrect question number.')
            return None
        else:
            qtxt = resp.json().get("qtext")
            print(qtxt)
            return None        

    def data(self,qnum):
        """This method accepts a question number and returns the data for the question."""
        url = f"{self.server}/question/{qnum}"
        resp = self.browser.get(url)
        if resp.status_code == 404:
            print('404 error. There is no question with that number. Either you completed all the challenges or entered an incorrect question number.')
            return None
        else:
            qdata = resp.json().get("qdata")
            return qdata

    def answer(self, qnum, answer):
        """This method accepts two arguments, a question number and the calculated answer and returns a string informing whether the supplied answer was correct or incorrect."""
        url = f"{self.server}/question/{qnum}"
        ans = {'ans':str(answer).strip()}
        resp = self.browser.post(url, json=ans)
        if resp.status_code == 404:
            print('404 error. There is no question with that number. Either you completed all the challenges or entered an incorrect question number.')
            return None
        else:
            return resp.json()["check"]

game = Game('http://127.0.0.1:5000')
