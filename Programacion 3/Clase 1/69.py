def mySqrt(x):
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        else mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # El cuadrado de right es el más grande menor o igual a x


print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
