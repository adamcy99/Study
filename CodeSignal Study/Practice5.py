# You've created a new programming language, and now you've decided to add hashmap support to it. 
# Actually you are quite disappointed that in common programming languages it's impossible to add 
# a number to all hashmap keys, or all its values. So you've decided to take matters into your 
# own hands and implement your own hashmap in your new language that has the following operations:

# insert x y - insert an object with key x and value y.
# get x - return the value of an object with key x.
# addToKey x - add x to all keys in map.
# addToValue y - add y to all values in map.
# To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

# Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

def solution(queryType, query):
    store = {}
    output = 0
    keyAdd = 0
    valAdd = 0
    for i in range(len(queryType)):
        if queryType[i] == 'insert':
            x, y = query[i]
            store[x-keyAdd] = y-valAdd
        elif queryType[i] == 'get':
            output += store[query[i][0]-keyAdd] + valAdd
        elif queryType[i] == 'addToKey':
            keyAdd += query[i][0]
        elif queryType[i] == 'addToValue':
            valAdd += query[i][0]
    return output