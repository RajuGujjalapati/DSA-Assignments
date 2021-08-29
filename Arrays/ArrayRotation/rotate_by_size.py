def array_rotation(array, size):
    # removing size
    rotate_elem = array[:size]
    del array[:size]
    new_array = array + rotate_elem
    return new_array

print(array_rotation([1,2,3,4,5,6,7],4))


#using juggling method

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(10,3))


