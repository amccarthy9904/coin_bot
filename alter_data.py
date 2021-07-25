import csv


updata = open('data/BTC-USD_new.csv', 'w+')

with open('data/BTC-USD_orig.csv',newline='') as olddata:

    reader = csv.reader(olddata)
    for (d,o,h,l,c,a,v) in reader:
        updata.write(f"{o},{h},{l},{c},{v},{int(float(o) > float(c))}\n")