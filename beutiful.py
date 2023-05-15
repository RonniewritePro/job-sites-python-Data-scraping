import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


url = "https://www.myjobmag.co.ke/page/3"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find(id="jobs-sec")

job_title = results.find_all("li", class_="mag-b")

table = PrettyTable()
table.field_names = ["job-title"]

for job in job_title:
    table.add_row([job.text.strip()])

print(table)
