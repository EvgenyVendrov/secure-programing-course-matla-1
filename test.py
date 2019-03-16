import requests
from bs4 import BeautifulSoup

print("start")

for idNum in range(2, 99999):
    page = requests.get("https://moodlearn.ariel.ac.il/course/view.php?id=" + str(idNum))
    soup = BeautifulSoup(page.content, 'html.parser')
    notRegDiv = soup.find(id="notice")
    notFountDiv = soup.find_all("div", class_="alert-danger")
    if notRegDiv is None and not notFountDiv:
        print(str(idNum)+"\n")
print("done")