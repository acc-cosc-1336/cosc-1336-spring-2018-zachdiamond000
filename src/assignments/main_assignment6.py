from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file

'''
Using function get_count_A_C_G_and_T_in_string create a main function and...
Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
Sample Output:

DNA String:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A 20, C 12, G 17, T 21


Call the main function in Python Shell or in this file.
'''
def main():
    print('DNA String: ')
    dna_string = str('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    val1,val2,val3,val4 =get_count_A_C_G_and_T_in_string(dna_string)
    
    print('A', val1, ',', 'C', val2, ',', 'G', val3, ',', 'T', val4)
        
main()
