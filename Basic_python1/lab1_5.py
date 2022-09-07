from itertools import count


def f():
    k = 0
    bid = list(map(int, input ("Enter All Bid : ").split()))
    if(len(bid) > 1):
        max_bid = max(bid[0],bid[1])
        secondmax = min(bid[0], bid[1])
        if(bid.count(max_bid) > 1):
            print("error : have more than one highest bid")
        else:
            for i in range (2,len(bid)):
                if bid[i] > max_bid:
                    secondmax = max_bid
                    max_bid = bid[i]
                elif bid[i] > secondmax and \
                    max_bid != bid[i]:
                    secondmax = bid[i]
                elif max_bid == secondmax and \
                    secondmax != bid[i]:
                    secondmax = bid[i]
            print("winner bid is "+str(max_bid)+" need to pay "+str(secondmax))
    else:
        print("not enough bidder")

f()