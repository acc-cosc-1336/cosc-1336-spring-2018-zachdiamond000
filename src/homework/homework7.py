'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.

Sample Dataset
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Sample Output
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000

'''
def get_p_distance_matrix(a):
    
    ROWS = 4
    COLS = 4
    
    i = 0
    
    
    output = [[0.0,0.0,0.0,0.0],
              [0.0,0.0,0.0,0.0],
              [0.0,0.0,0.0,0.0],
              [0.0,0.0,0.0,0.0]]
  
#output loops
    for k in range(0,len(a)):
        for j in range(k, len(a)):
            count = 0.0
            for i in range(0,len(a[k])):
                print(a[k][i])
                if a[k][i] == a[j][i] or a[j][i] == a[k][i]:
                    i += 1
                else:
                    count += 0.1
            output[k][j] = count
            output[j][k] = count
    print(output)
    return output



            
