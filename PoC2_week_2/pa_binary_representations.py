'''
SOURCE: https://www.coursera.org/learn/principles-of-computing-2/supplement/p0KdU/practice-activity-binary-representations-for-numbers
PoC SOLUTION: http://www.codeskulptor.org/#poc_gray_code.py
'''

def make_binary(length):
    '''
    Returns a list containing all binary numbers of the specified length
    '''
    if length == 0:
        return ['']
    else:
        outcomes = ['0', '1']
        return [entry + outcome for outcome in outcomes for entry in make_binary(length - 1)]


def make_binary_ordered(length):
    '''
    Returns a list containing all binary numbers of the specified length (ordered)
    '''
    if length == 0:
        return ['']
    result = list()
    for sequence in make_binary_ordered(length - 1):
        result.append('0' + sequence)
    for sequence in make_binary_ordered(length - 1):
        result.append('1' + sequence)
    # print result
    return result

def bin_to_dec(bin_num):
    '''
    Computes the decimal value of the specified binary number
    '''
    if len(bin_num) == 0:
        return 0
    else:
        degree = len(bin_num) - 1
        digit = int(bin_num[0])
        return (2 ** degree * digit) + bin_to_dec(bin_num[1:])


def make_gray(length):
    '''
    Generates a list of binary strings of the specified length
    ordered such that consecutive strings differ by exactly one bit
    '''
    if length == 0:
        return ['']
    result = list()
    remaining = make_gray(length - 1)
    for sequence in remaining:
        result.append('0' + sequence)
    remaining.reverse()
    for sequence in remaining:
        result.append('1' + sequence)
    # print result
    return result


def gray_to_bin(gray_code):
    '''
    Converts a Gray code to the standard binary number with same value
    '''
    if len(gray_code) == 1:
        return gray_code
    else:
        rest = gray_to_bin(gray_code[:-1])
        current = (int(gray_code[-1]) + int(rest[-1])) % 2
        return rest + str(current)





if __name__ == '__main__':
    # print '### UNORDERED BINARIES: ###'
    # binaries = make_binary(5)
    # print len(binaries)
    # print binaries
    # converted = sorted([bin_to_dec(value) for value in binaries])
    # print converted
    # print
    # print '### ORDERED BINARIES: ###'
    # ordered_binaries = make_binary_ordered(5)
    # print len(ordered_binaries)
    # print ordered_binaries
    # print '### ORDERED GRAY CODE: ###'
    gray = make_gray(5)
    # print gray
    # print gray_to_bin('00011') # Expected: 00010
    print 'GRAY', 'BIN', 'DEC'
    for gray_code in gray:
        binary = gray_to_bin(gray_code)
        dec = bin_to_dec(binary)
        print gray_code, binary, dec
