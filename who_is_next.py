'''Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles!
The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can,
drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Write a program that will return the name of the person who will drink the n-th cola.

Input
The input data consist of an array which contains at least 1 name, and
single integer n which may go as high as the biggest number your language of choice supports (if there's such limit, of course).

Output / Examples
Return the single line 97 the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.

who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"'''


def whoIsNext(names, r):
    len_names = len(names)
    
    if r <= len_names:
        return names[r-1]

    i = 0
    k = 1
    while r > k:
        k += len_names * (2**i)
        i += 1
    k =  k-(len_names * 2**(i-1))
    i -= 1
    
    num1 = (r-k)//(2**(i))
    q = 1
    while num1 > (len_names-1):
        num1 = (r-k)//(2**(i+q))
        q += 1
    if q > 1:
        num1 -= (r-k)//(2**(i+q-1))

    return names[num1]


if __name__ == '__main__':
    names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
    if whoIsNext(names, 52) == "Penny":
        print "PASS"
    else:
        print "FAIL"
