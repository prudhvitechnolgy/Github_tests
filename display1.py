import requests
from bs4 import BeautifulSoup
import csv

try:
    source=requests.get("https://books.google.co.in/books/about/It_Starts_with_Us.html?id=okVdEAAAQBAJ&printsec=frontcover&source=kp_read_button&hl=en&newbks=1&newbks_redir=0&gboemv=1&redir_esc=y#v=onepage&q&f=false")
    soup=BeautifulSoup(source.text,'html.parser')
    print(soup)
except Exception as e:
    print(e)

images = soup.find_all('img')
image_urls = [img['src'] for img in images]

# Download each image and save it to disk
for url in image_urls:
    response = requests.get('https://books.google.co.in/books/about/It_Starts_with_Us.html?id=okVdEAAAQBAJ&printsec=frontcover&source=kp_read_button&hl=en&newbks=1&newbks_redir=0&gboemv=1&redir_esc=y#v=onepage&q&f=false')
    with open(url.split('/')[-1], 'wb') as f:
        f.write(response.content)
        print(images)

print('Images downloaded successfully!')
print(images)
#using csv  we have to store the data
with open('il.csv','w') as csvfile:
    write=csv.writer(csvfile)
    write.writerow(images)



