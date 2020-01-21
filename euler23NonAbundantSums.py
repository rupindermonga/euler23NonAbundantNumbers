#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def SumProperDivisor(n):
    sum = 0
    for i in range(1, int(n ** 0.5) +1):
        if n % i == 0:
            sum += i + (n //i)
    if n**0.5 - int(n**0.5) == 0:
        sum -= n**0.5
    return sum - n

def IsAbundant(n):
    return n < SumProperDivisor(n)

def IsSumof2Abundant(n):
    result = False
    for number in range(1, int(n//2)+1,1):
        if IsAbundant(number) and IsAbundant(n - number):
            result = True
            break
    return result

def SumNonAbundant(n):
    sum = 0
    for number in range(1, n, 1):
        if IsSumof2Abundant(number):
            sum += number
    

    return n*(n-1)*0.5 - sum



#final = SumProperDivisor(4)
final = SumNonAbundant(28123)
print(final)