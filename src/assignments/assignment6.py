def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    for ch_a in dna_string:
        if ch_a == 'A' or ch_a == 'a':
            count_a +=1
    print('A: ', count_a)

    for ch_c in dna_string:
        if ch_c == 'C' or ch_c == 'c':
            count_c +=1
    print('C: ', count_c)

    for ch_g in dna_string:
        if ch_g == 'G' or ch_g == 'g':
            count_g +=1
    print('G: ', count_g)

    for ch_t in dna_string:
        if ch_t == 'T' or ch_t == 't':
            count_t +=1
    print('T: ', count_t)

    return count_a, count_c, count_g, count_t

