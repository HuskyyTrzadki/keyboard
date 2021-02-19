import self as self
from bs4 import BeautifulSoup
import requests
import lxml

if __name__ == '__main__':

    #moze jakis dekorator?
    def returnlink(x):
        return f'https://nofluffjobs.com/pl/jobs/frontend{x}'
    class JobOffers:
        def __init__(self,link,requirements=set(),salary=None,level=set()):
               self.link = link
               self.requirements = requirements
               self.salary = salary
               self.level = level
    typesOfJobs=["frontend","backend","ux","artificial-intelligence","fullstack",
                    "mobile","gaming","big-data","embedded","it-administrator","project-manager","ux","backoffice"]

    allinks=[]


    def zwrocLinkiZOfertamiZeStrony(src):
        source = requests.get(src).text
        soup = BeautifulSoup(source, 'lxml')
        for elem in soup.find_all('a'):
            link = elem.attrs['href']
            if "/pl/job" in link and link.count("-") > 3:
                yield "nofluffjobs.com"+link
    for typeOfJob in typesOfJobs:
        allinks.append(zwrocLinkiZOfertamiZeStrony(f'https://nofluffjobs.com/pl/jobs/{typeOfJob}'))
        for SiteNumber in range(1,3):
            for i in zwrocLinkiZOfertamiZeStrony(f'https://nofluffjobs.com/pl/jobs/{typeOfJob}?page={str(SiteNumber)}'):
                allinks.append(i)

    print(len(allinks))



            #generator
    #wezmy wszystkie oferty na frontend




