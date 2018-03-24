#write import statement for homework 7 file
from src.homework.homework7 import get_p_distance_matrix
'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''
def main():
    infile = open('p_distance.dat', 'r')
    print('\n')
    
    s1 = infile.readline()
    s2 = infile.readline()
    s3 = infile.readline()
    s4 = infile.readline()

    s1 = s1.rstrip('\n')
    s2 = s2.rstrip('\n')
    s3 = s3.rstrip('\n')
    s4 = s4.rstrip('\n')
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    s3 = s3.replace(" ", "")
    s4 = s4.replace(" ", "")

    a = [s1,s2,s3,s4]
    infile.close()
    get_p_distance_matrix(a)
    print(a)
main()
