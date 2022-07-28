from bs4 import BeautifulSoup
import requests
from constants import PARSER_TYPE, HREF, URL, table_name, db_name
from sql_auto import Database
from datetime import datetime
import multiprocessing


class Parser:
    def __init__(self, url, parser_type=PARSER_TYPE):
        response = requests.get(url)
        content = response.content
        self.soap = BeautifulSoup(content, parser_type)


    def parse_html(self):
        date = self.soap.find('h1', class_='bold').find_all('a')[1:]
        price = self.soap.find('span', class_="fnum").get_text()
        try:
            city = self.soap.find('span', class_ = 'grey-text').findNext('span')
        except AttributeError:
            city = 'not city'

        result = {
            'date':date[0].text,
            'mark':date[1].get_text(strip=True).replace(' ', ''),
            'model':date[2].get_text(strip=True).replace(' ', ''),
            'price':price.replace(' ', ''),
            # 'city':city.text,
            'link':'https://auto.am/offer/' + str(i)
        }


        return result




# time1 = datetime.now()
# for i in range(HREF, HREF + 100):
#     Car_list = []
#     try:
#         url = URL + str(i)
#         pars = Parser(url=url, parser_type=PARSER_TYPE)
#         Car_list.append(pars.parse_html())
#         data = Database(db_name)
#         for i in Car_list:
#             data.insert_values(table_name, i['mark'], i['model'],
#                                i['date'], i['price'],  i['link'])
#         print(Car_list)
#     except AttributeError as e:
#         pass
# time2 = datetime.now()
# print(time2 - time1)

time1 = datetime.now()
def get_url(url):
    car_list = []
    a = Parser(url=url)
    try:
        car_list.append(a.parse_html())
        data = Database(db_name)
        for i in car_list:
            data.insert_values(table_name, i['mark'], i['model'],
                               i['date'], i['price'],  i['link'])
    except AttributeError as e:
        pass
    return car_list

links_list = []
for i in range(HREF, HREF+1000):
    links_list.append(URL + str(i))
if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        print(p.map(get_url, links_list))
time2 = datetime.now()
print(time2 - time1)