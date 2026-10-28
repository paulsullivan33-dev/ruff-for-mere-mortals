def greet( name , greeting = "hello" ):
    message = greeting +   ", " + name+"!"
    return message


def total(prices):
        total = 0
        for price in prices: total += price
        return total

print( greet("world") )
print(total([1,2,3]))
