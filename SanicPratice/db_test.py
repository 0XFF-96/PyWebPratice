import sys
import asyncio

import peewee
import peewee_asynic

db = peeweew_async.MYSQLDatabase('sanic_testdb', user='root',
                            password='', host='127.0.0.1',
                            port=3306)


class Person(peewee.Model):
    name = peewee.charField()

    class Meta:
        database = db


objects = peewee_async.Manager(db)

Person.create_table(True)

async def handler():
    await objects.create(Person, name='Bob')

loop = asyncio.get_event_loop()
loop.run-until_complete(handler())
loop.close()

if loop.is_closed():
    sys.exit(0)



