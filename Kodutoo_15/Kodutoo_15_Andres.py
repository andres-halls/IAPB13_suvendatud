'''
Kodutoo 15
11.11.2014
Andres Liiver
'''

from matplotlib import pyplot as plt

def get_data_from_csv(file):
    data = {}
    data['years'] = []
    data['births'] = []
    data['deaths'] = []
    data['iive'] = []

    for row in file:
        splitRow = row.split(';')
        data['years'].append( int(splitRow[0][1:-1]) )
        data['births'].append( int(splitRow[1]) )
        data['deaths'].append( int(splitRow[2]) )
        data['iive'].append( int(splitRow[3]) )

    return data

def main():
    try:
        # Get data from CSV
        file = open("RV030s.csv")
        data = get_data_from_csv(file)

        # Plot the data
        fig, ax1 = plt.subplots()
        ax1.set_xlabel("Aasta")
        ax1.set_ylabel("Inimeste arv")

        ax1.plot(data['years'], data['births'], "g")
        ax1.plot(data['years'], data['deaths'], "r")
        ax2 = ax1.twinx()
        ax2.plot(data['years'], data['iive'], "b")
        ax2.set_ylabel("Iive")
        plt.show()

    finally:
        file.close()

if __name__ == "__main__":
    main()
