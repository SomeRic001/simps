import os
import sys
import django
import csv
import yfinance as yf
from django.db import connection
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","simps_project.settings")
django.setup()


def fetch_symbols():
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT equity_id, symbol
            FROM Global_Equities
        ''')
        return cursor.fetchall()
    
def populate_prices(initial_symbols):
    today = datetime.today().date()
    with connection.cursor() as cursor:
        for symbol in initial_symbols:
            try:
                info = yf.Ticker(symbol).info
                name = info.get('shortName') or 'Stock'
                typ = info.get('sector') or ''
                sector = info.get('sector') or ''
                price = round(float(info.get('regularMarketPrice',0)),2)
                if not price:
                    continue
                cursor.execute(""" INSERT INTO Global_Equities(symbol,equity_name,type,sector,current_price)
                                VALUES (%s,%s,%s,%s,%s)                
                               """,[symbol,name,typ,sector,price])
                
            except Exception as e:
                print(e)
            cursor.execute("SELECT equity_id, symbol FROM Global_Equities WHERE symbol IN %s", [tuple(initial_symbols)])
            equity_map = {symbol: eid for eid, symbol in cursor.fetchall()}
            
            for symbol in initial_symbols:
                try:
                    info = yf.Ticker(symbol).info
                    price = info.get('regularMarketPrice')
                    if price is None:
                        continue
                    price = round(float(price),2)
                    equity_id = equity_map[symbol]

                    cursor.execute(''' INSERT INTO Equity_Price_History (equity_id,price,date)
                                VALUES (%s,%s,%s)
                                    ''',[equity_id,price,today])
                except Exception as e:
                    print(e)


def update_prices():
    equities = fetch_symbols()
    
    if not equities:
        print("No Equities Found, populating")
        initial_symbols=[]
        csv_path = os.path.join(os.path.dirname(__file__), 'symbols.csv')
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                initial_symbols.append(row['symbol'])
        populate_prices(initial_symbols)
        return
    
    equity_map = {symbol: eid for eid, symbol in equities}    
    symbols = [symbol for _, symbol in equities]

    data = yf.download(tickers = symbols,period ="1d",interval = "1d",group_by = 'ticker',progress= False)

    today = datetime.today().date()

    with connection.cursor() as cursor:
        for symbol in symbols:
            try:
                if len(symbols)>1:
                    price = data[symbol]['Close'][-1]
                else:
                    price = data['Close'][-1]
                price = round(float(price),2)
                equity_id = equity_map[symbol]

                cursor.execute(''' UPDATE Global_Equities
                               SET current_price = %s , last_updated = NOW()
                               WHERE equity_id = %s
                ''', [price,equity_id])

                cursor.execute(''' INSERT INTO Equity_Price_History (equity_id, price, date)
                               VALUES (%s,%s,%s)
                ''',[equity_id,price,today])

                print(f"Updated {symbol}-> {price}")
            except Exception as e:
                print(e)

def main():
    update_prices()
    print("Done")

if __name__=="__main__":
    main()