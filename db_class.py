from sqlalchemy import Table, Column, Integer, String, DateTime, create_engine, MetaData
import datetime
import json

class db:
    '''A class to get and retrieve stocks from the sqlite database using sqlalchemy library'''
    def __init__(self, path_to_db):
        self.engine = create_engine(path_to_db)
        self.conn = self.engine.connect()
        self.metadata = MetaData(self.engine)

    def getTable(self):
        '''
        Gets the instance of the stocks table or creates one if not already made.

        Returns
            stocks: instance of the stocks table.
        '''
        stocks = None
        # Check if stocks table is present in the database
        if not self.engine.dialect.has_table(self.engine, "stocks"):
            # Create and return stocks table
            stocks = db.Table(
               'stocks', self.metadata,
               Column('id', Integer, primary_key = True),
               Column('stock_json', String),
               Column('Date', DateTime, default=datetime.datetime.utcnow()),
            )
            self.metadata.create_all(self.engine)
            return stocks
        # Call instance of already made stocks table
        return Table("stocks",self.metadata, autoload = True)

    def insertIntoDB(self, json_obj, stocks_table):
        '''
        Inserts stocks into the database

        Args
            json_obj: the json containing the stock values
            stocks_table: database reference of the stocks table
        '''
        # Creates a dict of objects to be inserted
        insertDict = {}
        insertDict['stock_json'] = json.dumps(json_obj)
        insertDict['Date'] = datetime.datetime.utcnow()
        # Database call to insert into database
        inserted = self.engine.execute(stocks_table.insert().values(insertDict))

    def getLastEntry(self):
        '''
        Gets the last entry inserted into the database

        Returns
            parsed_json: json containing the stocks
        '''
        # SQL query to get the last entry
        lastEntry = self.conn.execute('select stock_json from stocks order by date desc limit 1')
        # parse and return the last entry as a json
        lastEntry_res = lastEntry.first()[0]
        parsed_json = json.loads(lastEntry_res)
        return parsed_json
