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
    """
        Groups data into rows that will be used as input
        each row represents the previous 50 days
        the last datapoint in each row is the label for today
    """
    inputs = open('data/BTC-USD_in.csv', 'w+')
    prev_50 = []

    with open('data/BTC-USD_new.csv',newline='') as filterd_data:
        reader = csv.reader(filterd_data)

        for ind, (o,h,l,c,v,label) in enumerate(reader):

            if ind > 50:
                input_row = ""
                for day in prev_50:
                    input_row += day
                input_row += label
                inputs.write(f"{input_row}\n")

            prev_50.append(f"{o},{h},{l},{c},{v},")
            if ind < 50:
                continue
            prev_50.pop(0)

def create_col_labeled_inputs():
    """
        Groups data into rows that will be used as input
        each row represents the previous 50 days
        the last datapoint in each row is the label(Green/Red) for today
        Adds labels for columns as well to help later
    """

    inputs = open('data/BTC-USD_in.csv', 'w+')

    col_labels = ""
    for ind in range(250):
        col_labels += f"{str(ind)},"
    col_labels += "Label\n"

    print("here")
    print(col_labels)

    inputs.write(col_labels)
    prev_50 = []

    with open('data/BTC-USD_new.csv',newline='') as filterd_data:
        reader = csv.reader(filterd_data)

        for ind, (o,h,l,c,v,label) in enumerate(reader):

            if ind > 50:
                input_row = ""
                for day in prev_50:
                    input_row += day
                input_row += label
                inputs.write(f"{input_row}\n")

            prev_50.append(f"{o},{h},{l},{c},{v},")
            if ind < 50:
                continue
            prev_50.pop(0)


# create_inputs()
create_col_labeled_inputs()