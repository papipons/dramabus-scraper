class Drama(object):
    title = ''
    releaseDate = ''
    status = ''
    
    def __init__(self, data):
        self.title = data[0].h2.a.text
        self.releaseDate = data[1].small.text
        self.status = self.getStatus(data)

    def getStatus(self, data):
        if not data[3].div.strong: 
            return data[3].div.text

        status = data[3].div.strong.text + data[3].div.a.text
        if data[3].div.span.text != '()':
            status += data[3].div.span.text

        return status

    @classmethod
    def parse(cls, soup):
        return [Drama(drama.findAll('div', attrs = {'class': 'col-md-3'})) 
            for drama in soup.select('div#list-drama .media')]