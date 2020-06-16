import requests                         #importing requests module which allows to send HTTP requests.
from bs4 import BeautifulSoup           #importing Beautiful Soup which is a Python library for pulling data out of HTML and XML files.

class WebScrapper():                    #creating class
   wikiDoc = requests.get("https://en.wikipedia.org/wiki/Main_Page") #The get() method sends a GET request to the specified url and returns a requests.Response object.
   parsedDoc = BeautifulSoup(wikiDoc.content, "html.parser")  # parsing the wikiDoc content # calling beatifulsoup to parse html 

   def getTitle(self):                      #creating a method which returns title string 
     title = self.parsedDoc.title.string
     return title

   def getWikiLinks(self):                   #creating a method which returns title string of parsedoc
       list =[]
       for link in self.parsedDoc.find_all('a'):  #looping to find all a tags
           list.append(link.get('href'))       #appending all links to list
       return list

webs = WebScrapper()                        #creating obj
print(webs.getTitle())                      #printing out of title by calling gettitle method
print(webs.getWikiLinks())                  #printing out of links by calling getwikilinks method
f = open("output.txt", "w")                 #opeing file in write mode
f.write(webs.getTitle())                    #writing title into file 
f.write(str(webs.getWikiLinks()))           #writing links into file
f.close()
