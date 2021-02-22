import self as self
from bs4 import BeautifulSoup
import requests
import lxml
import time
import re

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
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        return [x.replace('Wymagania obowiązkowe','').strip() for x in (soup.find(class_="d-block pb-2").text).split('  ')]
    def getSalary(link):
        x={}
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        if len (soup.findAll('h4', class_='mb-0'))>1:
            x['B2B'] =([x.replace('PLN', '').strip() for x in (soup.findAll('h4', class_='mb-0')[0].text).split("-")])
            x['ContrOfEmplyment'] =([x.replace('PLN', '').strip() for x in (soup.findAll('h4', class_='mb-0')[1].text).split("-")])
            print(soup.findAll('h4', class_='mb-0'))
        else:
            if'B2B' in soup.find('p', class_='type').text:
                x['B2B']=([x.replace('PLN', '').strip() for x in (soup.find('h4', class_='mb-0').text).split("-")])

            else:
                print(soup.find('h4', class_='type'))
                x['ContrOfEmplyment']=([x.replace('PLN', '').strip() for x in (soup.find('h4', class_='mb-0').text).split("-")])
        return x
    #B2B:[1000,200q0]
    print(getSalary('https://nofluffjobs.com/pl/job/remote-ios-developer-vlogit-3w0j4dr9'))
    def getCity(link):
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        try:
            return soup.findAll("li", class_='text-break').text.replace('(Po pandemii)', '').strip()
        except(AttributeError):
            return "REMOTE"

    def getLevel(link):
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        return [i.text for i in soup.findAll("div", class_='col star-section text-center active')]

    def getTypeOfJob(elem):
        return elem[1]
    def getCompanySize(link):
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        try:
            return [i.text for i in soup.findAll('dd',class_='mb-0')][1].replace('+','').split('-')[1]
        except IndexError:
            return [i.text for i in soup.findAll('dd', class_='mb-0')][1].replace('+', '')
    def getCompanyName(link):
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        return soup.find("dd").text


    print(getCompanySize('https://nofluffjobs.com/pl/job/devops-engineer-aws-azure-link-group-remote-xwuagl0j'))
        #return soup.find("dl").text





