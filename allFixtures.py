from requests_html import HTMLSession
import json

class Fixture(dict):
    HOME_LEAGUE = "Premier League"
    def __init__(self,date,home,away) -> None:
        dict.__init__(self,date=date,home=home,away=away)
        self.home = home
        self.away = away
        self.date = date
    
    def printDict(self):
        print(self.__dict__)
    

    
def main():
    session = HTMLSession()

    #define our URL
    url = 'https://www.premierleague.com/fixtures'

    #use the session to get the data
    r = session.get(url)

    #Render the page, up the number on scrolldown to page down multiple times on a page
    r.html.render(sleep=1, keep_page=True, scrolldown=10)

    #take the rendered html and find the element that we are interested in

    
    fixtureDate_match_list = r.html.find('div.fixtures__matches-list')
    result_list = []
    for fixtureDate in fixtureDate_match_list:
        atrributes_of_fixtureDate = fixtureDate.attrs
        matchList = (fixtureDate.find('ul.matchList', first = True)).find('li.matchFixtureContainer')
        for match in matchList:
            attributes_of_match = match.attrs
            result_list.append(Fixture(atrributes_of_fixtureDate["data-competition-matches-list"],attributes_of_match["data-home"] , (attributes_of_match["data-away"])))
    
    print(json.dumps(result_list))


    

if __name__ == "__main__":
    main()
