'''
SOURCE: https://www.coursera.org/learn/principles-of-computing-2/supplement/6cuTC/practice-activity-recursion
'''

def triangular_sum(num):
    '''
    Computes the arithmetic sum 0+1+2...+(num-1)+num
    '''
    if num == 0:
        return num
    else:
        return num + triangular_sum(num - 1)


def number_of_threes(num):
    '''
    Returns the number of times the digit 3 appears in the decimal representation
    of the non-negative integer num
    '''
    str_num = str(num)
    if len(str_num) == 0:
        return 0
    else:
        if str_num[0] == '3':
            return 1 + number_of_threes(str_num[1:])
        else:
            return number_of_threes(str_num[1:])


def is_member(my_list, elem):
    '''
    Returns True if elem is a member of my_list and False otherwise
    '''
    if len(my_list) == 0:
        return False
    else:
        if my_list[0] == elem:
            return True
        else:
            return is_member(my_list[1:], elem)


def remove_x(my_string):
    '''
    Takes the string my_string and deletes all occurrences of the character 'x' from this string
    '''
    if len(my_string) == 0:
        return ''
    else:
        if my_string[0] != 'x':
            return my_string[0] + remove_x(my_string[1:])
        else:
            return remove_x(my_string[1:])


def insert_x(my_string):
    '''
    Takes the string my_string and adds the character 'x'
    between each pair of consecutive characters in the string
    '''
    if len(my_string) == 1:
        return my_string[0]
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])


def list_reverse(my_list):
    '''
    Takes a list and returns a new list whose elements appear in reversed order
    '''
    if len(my_list) == 0:
        return []
    else:
        return list_reverse(my_list[1:]) + [my_list[0]]


def gcd(num1, num2):
    '''
    Takes two non-negative integers and computes the greatest common divisor of num1 and num2
    (Using The Euclidean Algorithm)
    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    Solution from PoC: http://www.codeskulptor.org/#poc_recursion_gcd.py
    '''
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        if num1 > num2:
            return gcd(num2, num1 % num2)
        else:
            return gcd(num1, num2 % num1)


def slice(my_list, first, last):
    '''
    Takes as input a list my_list and two non-negative integer indices first and last
    satisfying 0<=first<=last<=n where n is the length of my_list.
    slice should return the corresponding Python list slice my_list[first:last]
    PoC solution: http://www.codeskulptor.org/#poc_recursion_slice.py
    '''
    if first == 0 and last == len(my_list):
        return my_list
    else:
        # print first, last, len(my_list)
        if first > 0:
            my_list.pop(0)
            first -= 1
            last -= 1
        if last < len(my_list):
            my_list.pop(-1)
        return slice(my_list, first, last)


if __name__ == '__main__':
    # print triangular_sum(4)
    # print number_of_threes(34534)
    # print is_member(['c', 'a', 't'], 'c')
    # print is_member(['c', 'a', 't'], 'b')
    # print remove_x('catxxdogx')
    # print insert_x('catdog')
    # print list_reverse([2, 3, 1])
    # print gcd(0, 0)
    print slice(['a', 'b', 'c', 'd', 'e'], 2, 4), 'EXPECTED: ["c", "d"]'
    print slice(['a', 'b', 'c', 'd', 'e'], 0, 2), 'EXPECTED: ["a", "b"]'
    print slice(['a', 'b', 'c', 'd', 'e'], 2, 5), 'EXPECTED: ["c", "d", "e"]'
    print slice(['a', 'b', 'c', 'd', 'e'], 1, 3), 'EXPECTED: ["b", "c"]'
    print slice([], 0, 0), 'EXPECTED: []'
    print slice([1], 0, 0), 'EXPECTED: []'
    print slice([1], 0, 1), 'EXPECTED: [1]'