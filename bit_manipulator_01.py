"""Python bit maniplation"""
# helper functions to help count outside of the  class to stop definition issues
def bitCounter(num):
	count =0

	while num:
		count += num & 1
		num >>= 1
	return count

class BitManipulation:
    '''Takes in two binary numbers and based on the output needed, will do conversions or math'''
    def __init__(self,input_1,input_2):
        self.bit_1= int(input_1,2)
        self.bit_2 = int(input_2,2)

    def __str__ (self):
        return f'{self.bit_1}, {self.bit_2}'

    def __repr__(self):
        return f'{self.bit_1}, {self.bit_2}'


    def add(self):
        """ Adds bits and spits out the binary representation"""
        return bin(self.bit_1 & self.bit_2)

    def differences(self):
        """ Uses the helper function called above to count the number of differences between off and ons(ones and zeros)"""
        return bitCounter(self.bit_1^self.bit_2)


if __name__ == "__main__":

    a = BitManipulation('00000010','10010010')

    print(a.add())
    print(a.differences())
