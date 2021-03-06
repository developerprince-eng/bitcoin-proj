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

    df1 = df1.iloc[::-1]
    df2 = df2.iloc[::-1]

    df1.plot(kind='line', x='Date', y='High', ax=ax, label='BitCoin-High')
    df2.plot(kind='line', x='Date', y='High', ax=ax, label='Ethereum-High')
    df2.plot(kind='line', x='Date', y='Close', ax=ax, label='Ethereum-Close')
    df1.plot(kind='line', x='Date', y='Close', ax=ax, label='BitCoin-Close')
    df1.plot(kind='line', x='Date', y='Open', ax=ax, label='BitCoin-Open')
    df2.plot(kind='line', x='Date', y='Open', ax=ax, label='Ethereum-Open')

    plt.show()

if __name__ == "__main__":
    main()