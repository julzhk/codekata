import dbm

with dbm.open('my_store', 'c') as db:
    db['key'] = 'value'
    print(db.keys())  # ['key']
    print(db['key'])  # 'value'
    print('key' in db)  # True
