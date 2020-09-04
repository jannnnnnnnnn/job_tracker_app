from bs4 import BeautifulSoup
import requests


page = requests.get(
    "https://ca.indeed.com/jobs?q=Junior+Developer&l=Toronto%2C+ON")
soup = BeautifulSoup(page.content, 'html5lib')
allp = soup.find_all("h2", class_="title")
print(allp)
return render(request, 'search.html', context)
# print(soup.find(id="resultsCol")
