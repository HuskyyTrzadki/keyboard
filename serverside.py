import self as self
from bs4 import BeautifulSoup
import requests
import lxml
import time

if __name__ == '__main__':

    #moze jakis dekorator?
    def returnlink(x):
        return f'https://nofluffjobs.com/pl/jobs/frontend{x}'

    data={'link':'None','requirements':set(),'salary':(0,0),'city':'None','level':'None','typeOfemploymennt':'none','typeofJob':'None','companySize':0}
    typesOfJobs=["frontend","backend","ux","artificial-intelligence","fullstack",
                    "mobile","gaming","big-data","embedded","it-administrator",
                 "project-manager","ux","backoffice"]

    def returnOffersfrompage(src):
        source = requests.get(src).text
        soup = BeautifulSoup(source, 'lxml')
        for elem in soup.find_all('a'):
            link = elem.attrs['href']
            if "/pl/job" in link and link.count("-") > 3:
                yield "www.nofluffjobs.com"+link
    def returnOffersFromEveryPage(allLinks=set()):
        for typeOfJob in typesOfJobs:
            for i in returnOffersfrompage(f'https://nofluffjobs.com/pl/jobs/{typeOfJob}'):
                allLinks.add((i,typeOfJob))
                #wait

            for SiteNumber in range(2, 3):
                for i in returnOffersfrompage(f'https://nofluffjobs.com/pl/jobs/{typeOfJob}?page={str(SiteNumber)}'):
                    allLinks.add((i,typeOfJob))

        return allLinks
    #fortests
    import exampledata
    def getLink(elem):
        return elem[0]
    def getRequirements(link):
        returnList=set()
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        for i in soup.findAll("button", {"class": "btn btn-outline-success btn-sm no-cursor text-truncate"}):
            returnList.add(i.text)
        return returnList

    def getSalary(link):
        returnList = []
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        for i in soup.findAll('h4',class_='mb-0'):
            returnList.append(i.text)
        return (returnList[1].split("-")[0].strip(),returnList[1].split("-")[1].replace('PLN','').strip())
    def getCity(link):
        returnList =[]
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        try:
            return soup.find("li", class_='text-break').text.replace('(Po pandemii)', '').strip()
        except(AttributeError):
            return "REMOTE"
    print(getCity('https://nofluffjobs.com/pl/job/java-backend-developer-praca-zdalna-finture-remote-w3dcdr7u'))

    def getLevel(link):
        pass
    def getTypeOfJob(link):
        pass
    def getComapanySize(link):
        pass
    def getTypeOfEmploymennt(link):
        pass





