import pandas as pd, datetime as dt, requests, time as t
from bs4 import BeautifulSoup

df = None
try:
    df = pd.read_csv('data.csv')
except:
    df = pd.DataFrame(columns=['ido', 'fert', 'gyogy', 'elh', 'kara', 'teszt', 'v_fert', 'v_gyogy', 'v_elh'])
try:
    while True:
        try:
            response = requests.get('https://koronavirus.gov.hu/')
            soup = BeautifulSoup(response.text, 'html.parser')
            stuff = [int(x.contents[0].replace(' ', '')) for x in soup.body.findAll('span', 'number')]
            print(stuff)
            df.loc[len(df)] = [dt.datetime.now().strftime('%Y-%m-%d %H:%M')] + stuff
            t.sleep(60*60)
        except KeyboardInterrupt:
            break
finally:
    df.to_csv('data.csv', index=False)
    print('Done!')