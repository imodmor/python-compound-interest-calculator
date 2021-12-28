principle = input("Enter Principle Amount ($): ")
rate = input("Enter Interest Rate (%): ")
time = input("Enter Time (Day): ")

Amount = int(principle) * (pow((1 + int(rate) / 100), int(time)))
CI = Amount - int(principle)

if __name__ == '__main__':
    print("Amount is: ", "${:,.2f}".format(Amount))
    print("Compound interest is: ", "${:,.2f}".format(CI))
