import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key("UvrNAo166XJ5IlEBV3IP87Y4ySeGaHKsHRRqPfMNVfs")
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response
