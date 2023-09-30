import requests
from bs4 import BeautifulSoup
import datetime
import csv

def fetch_livescore():
    try:
        current_time = datetime.datetime.now()
        url = 'https://www.espncricinfo.com/live-cricket-score'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        status = soup.find_all(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')[0].text
        t1 = soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[0].text
        s1 = soup.find_all(class_='ds-text-typo-mid3')[0].text
        k = s1.split(',')
        overt1 = k[0]
        t2 = soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[1].text
        overt2 = soup.find_all(class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')[1].text
        matchdate = soup.find_all(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3')[1].text
        date = soup.find_all(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3')[1].text
        a = matchdate.split(',')
        date = ""
        date = date + a[2] + " " + a[3]
        livescoredata = "Fetching the live score ...\n" \
                        f" {t1} vs {t2}\n" \
                        f" {status}\n" \
                        f" {t1}:{overt1} \n "\
                        f" {t2}:{overt2}\n" \
                        f" {matchdate}\n" \
                        f" Date {date}"
        with open("liveScore1.csv", "a+") as file:
            writer = csv.writer(file)
            x = livescoredata
            x += f" ., {current_time} "
            l = []
            l.append(x)
            writer.writerow(l)

        return livescoredata

    except Exception as e:
        return f"Failed to fetch livescore/No live event right now... ({e})"

if __name__ == "__main__":
    while True:
        fetch_livescore()
