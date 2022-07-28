import sqlite3

# import constants


class Database:
    def __init__(self, db_name):
        with sqlite3.connect(db_name) as self.connect:
            self.curs = self.connect.cursor()

    def create_table(self, table_name):
        querry = f"CREATE TABLE IF NOT EXISTS {table_name} (" \
                 f"id INTEGER PRIMARY KEY AUTOINCREMENT," \
                 f"mark varchar(100) not null," \
                 f"model varchar(100) not null," \
                 f"make_year integer(10) not null," \
                 f"price integer(100) not null," \
                 f"link varchar(100) not null)"
        self.curs.execute(querry)
        cars_table = self.connect.commit()
        return cars_table

    def drop_table(self, table_name):
        querry = f"DROP TABLE {table_name};"
        self.curs.execute(querry)
        self.connect.commit()

    def insert_values(self, table_name, mark, model, make_year, price,  link):
        querry = f"INSERT INTO {table_name} ('mark', 'model','make_year', 'price', 'link')" \
                 f"VALUES ('{mark}', '{model}','{make_year}', '{price}',  '{link}')"
        self.curs.execute(querry)
        self.connect.commit()

    def select_row(self, table_name = "cars_table"):
        querry = f"SELECT * FROM {table_name}"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result


    def select_all_mark(self, mark = "mark", table_name = "cars_table"):
        querry = f"SELECT {mark} FROM {table_name}"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result

    def min_and_max_price(self, min_price, max_price, table_name = 'cars_table'):
        querry = f"SELECT * FROM {table_name} WHERE price > {min_price} AND price < {max_price}"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result


    def search_by_mark(self,text, table_name = "cars_table"):
        querry = f"SELECT * FROM {table_name} WHERE mark LIKE '{text}%'"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result

    def search_by_model(self, text, table_name="cars_table"):
        querry = f"SELECT * FROM {table_name} WHERE model LIKE '{text}%'"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result

    def search_by_data(self, start_data, end_data, table_name):
        querry = f"SELECT * FROM {table_name} WHERE make_year > {start_data} AND make_year < {end_data}"
        self.curs.execute(querry)
        self.connect.commit()
        result = self.curs.fetchall()
        return result


d = Database('cars_db')
d.create_table('cars_table')
# print(d.select_row('cars_table'))
# print(d.select_all_mark('mark', 'cars_table'))
# print(d.min_and_max_price(1000, 10000))
# print(d.search_by_data(start_data=2010, end_data=2020, table_name='cars_table'))
# d.search_by_mark(text='Mer',table_name='cars_table')
# print(d.search_by_model(text ='x6'))