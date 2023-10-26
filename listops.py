#find(a, k) returns the index of the first occurrence of the element k within the list a, and -1 if the element does not
#exist in the list
#rfind(a, k) returns the index of the last occurrence of the element k within the list a, and -1 if the element does not
#exist in the list
#count(a, k) returns the number of occurrences of the element k within the list a
#contains(a, k) returns True if the list a contains the element k, and False otherwise

def find (a , k ):
    for i in range(len(a)):
        if a[i] == k:
            return i

#returns -1 if k is not found in array
    return -1

def rfind (a , k ):
    for i in range(len(a)-1,0,-1):
        if a[i] == k:
            return i
#returns -1 if k is not found
    return -1
def count (a , k ):
    count = 0
    for i in range(len(a)):
        if a[i] == k:
            count += 1
    return count
def contains (a , k ):
    for i in range(len(a)):
        if a[i] == k:
            return True

    return False

# Unit tests the library .
def _main ():
    import stdio

    a = [-10, 8, -2, 0, -2, 8, 1, 8, 3, 5, 8, 8]
    stdio.writeln(find(a,0))
    stdio.writeln(rfind(a,-2))
    stdio.writeln(count(a,8))
    stdio.writeln(contains(a,9))
    stdio.writeln(contains(a, -10))

if __name__ == "__main__":
    _main()