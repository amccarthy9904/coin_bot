import csv




def filter_orig():
    """Filters original dataset to get what we need"""

    filterd_data = open('data/BTC-USD_new.csv', 'w+')

    with open('data/BTC-USD_orig.csv',newline='') as olddata:

        reader = csv.reader(olddata)
        for (d,o,h,l,c,a,v) in reader:
            if d == 'Date':
                continue
            print(d)
            filterd_data.write(f"{o},{h},{l},{c},{v},{int(float(c) > float(o))}\n")


def create_inputs():

    inputs = open('data/BTC-USD_in.csv', 'w+')
    with open('data/BTC-USD_new.csv',newline='') as filterd_data:
        reader = csv.reader(filterd_data)
        for ind, (o,h,l,c,v,l) in enumerate(reader):
            
            if ind < 50:
                continue
        # stack 50 prev rows into one row in BTC-USD_in.csv

create_inputs()