def faculty_evaluation_result(nev, rar, som, oft, voft, alw):

    #input total response count

    total = nev + rar + som + oft + voft + alw

    #calc percentage 

    alw_ratio = alw / total
    
    voft_ratio = voft / total
    
    oft_ratio = oft / total
    
    som_ratio = som / total
    
    rar_ratio = rar / total
    
    nev_ratio = nev / total
    result = ''

    
    if alw_ratio + voft_ratio >= .9:
       result = 'Excellent'
    elif voft_ratio + oft_ratio + alw_ratio >= .8:# and voft_ratio + oft_ratio + alw_ratio <= .89:
        result = 'Very Good'
    elif som_ratio + voft_ratio + oft_ratio + alw_ratio >= .7:# and som_ratio + voft_ratio + oft_ratio + alw_ratio <= .79:
       result = 'Good'
    elif rar_ratio + som_ratio + voft_ratio + oft_ratio + alw_ratio >= .6:# and rar_ratio + som_ratio + voft_ratio + oft_ratio + alw_ratio <= .69:
       result = 'Needs Improvement'
    else:
        result = 'Unacceptable'


    return result
    '''
    Write code to calculate faculty evaluation rating according to asssignment instructions

    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''

def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
