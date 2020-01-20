import graphs.dnn.dataset.main as dt   
import matplotlib.pyplot as plt
import os 
os.getcwd()
os.listdir(os.getcwd())

def main():
    dataset = dt.DATASET() 
    ax = plt.gca()

    print(dataset.__read_csv__(path='graphs/inputs/bitcoin_price.csv'))

    print(dataset.__read_csv__(path='graphs/inputs/ethereum_price.csv'))

    df1= dataset.__read_csv__(path='graphs/inputs/bitcoin_price.csv')
    df2= dataset.__read_csv__(path='graphs/inputs/ethereum_price.csv')

    df1.plot(kind='line', x='Date', y='High', ax=ax)
    df2.plot(kind='line', x='Date', y='High', ax=ax)

    plt.show()

if __name__ == "__main__":
    main()