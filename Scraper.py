from bs4 import BeautifulSoup
import requests,csv

def Scrap(Path,Result,tag,_class):
    with open(Path, 'r') as file:
        csvreader = csv.reader(file)
        Result=f"{Result}/Result.txt"
        Rfile = open(Result,"w",buffering=1)
        for row in csvreader:
            try:
                rq = requests.get(row[0])
                soup = BeautifulSoup(rq.content,"html.parser")
                ad = soup.find(tag,{"class":_class})
                result = ad.text
                Rfile.write(f"{result}\n")
                Rfile.flush()
                print(row) 
            except:
                result = "Not Found"
                Rfile.write(f"{result}\n")