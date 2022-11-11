import sys
from rawConversion import dateConverter
from blockConversion import blockNumberETH, blockNumberARB, blockNumberBSC, blockNumberPOL
from transactionAddressETH import getWalletETH
from transactionAddressARB import getWalletARB
from transactionAddressBSC import getWalletBSC
from transactionAddressPOL import getWalletPOL


def main():
    start = dateConverter(sys.argv[2], "before")
    end = dateConverter(sys.argv[3], "after")
    if sys.argv[1] == "eth":
        first = int(blockNumberETH(start, "before"))
        next = first + 5000
        last = int(blockNumberETH(end, "after"))
        getWalletETH(sys.argv[4], first, next, last)
    elif sys.argv[1] == "arb":
        first = int(blockNumberARB(start, "before"))
        next = first + 5000
        last = int(blockNumberARB(end, "after"))
        getWalletARB(sys.argv[4], first, next, last)
    elif sys.argv[1] == "poly":
        first = int(blockNumberPOL(start, "before"))
        next = first + 5000
        last = int(blockNumberPOL(end, "after"))
        getWalletPOL(sys.argv[4], first, next, last)
    else:
        first = int(blockNumberBSC(start, "before"))
        next = first + 5000
        last = int(blockNumberBSC(end, "after"))
        getWalletBSC(sys.argv[4], first, next, last)

        
if __name__ == "__main__":
    main()
