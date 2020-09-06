from les6DB import Publisher, Book, Stock, Shop, Sale, Session, engine
import json

with open("fixtures.json", encoding='utf-8') as f:
    json_data = json.load(f)

if __name__ == '__main__':
    session = Session()
    # for item in json_data:
        # if item['model'] == 'publisher':
        #     session.add_all([Publisher(id = item['pk'], name = item['fields']['name'])])
        # if item['model'] == 'book':
        #     session.add_all([Book(id = item['pk'], title = item['fields']['title'],
        #                           id_publisher = item['fields']['publisher'])])
        # elif item['model'] == 'shop':
        #     session.add_all([Shop(id = item['pk'], name = item['fields']['name'])])
        # if item['model'] == 'stock':
        #     session.add_all([Stock(id = item['pk'], id_book = item['fields']['book'],
        #                            id_shop = item['fields']['shop'],
        #                            count = item['fields']['count'])])
    #     if item['model'] == 'sale':
    #         session.add_all([Sale(id = item['pk'], price = item['fields']['price'],
    #                               date_sale = item['fields']['date_sale'],
    #                               id_stock = item['fields']['stock'],
    #                               count = item['fields']['count'])])
    # session.commit()

    connection = engine.connect()
    sel = connection.execute("""SELECT name FROM publisher;
    """).fetchall()
    print(sel)
    print('Издателя скопируйте из списка выше')
    current_publisher = input('Введите имя издателя: ')
    for shop in session.query(Shop).join(
        Stock, Shop.id == Stock.id_shop).join(
        Book, Stock.id_book == Book.id).join(
        Publisher, Book.id_publisher == Publisher.id).filter(
        Publisher.name.ilike(f'%%{current_publisher}%%')).all():
        print(shop)
