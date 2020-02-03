from sqlalchemy import Table, Column, Integer, String, DateTime, create_engine, MetaData
import datetime
import json

class db:
    def __init__(self, path_to_db):
        self.engine = create_engine(path_to_db)
        self.conn = self.engine.connect()
        self.metadata = MetaData(self.engine)

    def getTable(self):
        stocks = None
        if not self.engine.dialect.has_table(self.engine, "stocks"):
            stocks = db.Table(
               'stocks', self.metadata,
               Column('id', Integer, primary_key = True),
               Column('stock_json', String),
               Column('Date', DateTime, default=datetime.datetime.utcnow()),
            )
            self.metadata.create_all(self.engine)
            return stocks
        return Table("stocks",self.metadata, autoload = True)

    def insertIntoDB(self, json_obj, stocks_table):
        insertDict = {}
        insertDict['stock_json'] = json.dumps(json_obj)
        insertDict['Date'] = datetime.datetime.utcnow()
        inserted = self.engine.execute(stocks_table.insert().values(insertDict))

    def getLastEntry(self):
        lastEntry = self.conn.execute('select stock_json from stocks order by date desc limit 1')
        lastEntry_res = lastEntry.first()[0]
        return json.loads(lastEntry_res)
