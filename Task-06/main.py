
import requests
from bs4 import BeautifulSoup
import json
import os
import csv
import datetime
try:

    def livescore():
        current_time=datetime.datetime.now()
        url='https://www.espncricinfo.com/live-cricket-score'



        response=requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        status=soup.find_all(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')[0].text
        t1=soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[0].text
        s1=soup.find_all(class_='ds-text-typo-mid3')[0].text
        k=s1.split(',')
        overt1=k[0]
        t2=soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[1].text
        overt2=soup.find_all(class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')[1].text
        matchdate=soup.find_all(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3')[1].text
        a=matchdate.split(',')
        date=""
        date=date+a[2]+" "+a[3]
        livescoredata=f"**Match** {t1} vs {t2}\n" \
                      f"**Main1:** {t1} : {overt1}\n" \
                      f"**Main2:** {t2} : {overt2}\n"  \
                      f"**Details:** {status}\n" \
                      f"**Date:** {date}\n" 
       
        print(livescoredata)
        print("'''''''\n")
        print(type(livescoredata))
        with open("liveScore.csv","a+") as file:
            writer=csv.writer(file)
            print(type(livescoredata))
            x=livescoredata
            x+=f" ., {current_time} "
            l=[]
            l.append(x)
            print(l)
            writer.writerow(l)
            reader=csv.reader(file)
            print(reader)
        
    #return(livescoredata)
    livescore()



    
except :
    print("Failed to fetch livescore/No live score currently!")
livescore()


