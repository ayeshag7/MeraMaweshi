def wrapper(array):
    checker=0
    if((array[0][6] == 1)):
        disease = 'Babesiosis'
        checker=checker+1
    if((array[0][84] == 1) and(array[0][7] == 1)):
        disease = 'Anthrax'
        checker=checker+1
    if((array[0][87] == 1)):
        disease = 'Arthritis'
        checker=checker+1
    if((array[0][38] == 1)):
        disease = 'Impaction/Constipation'
        checker=checker+1
    if((array[0][31] == 1) and (array[0][56] == 1) ):
        disease = 'Drenching Pneumonia'
        checker=checker+1
    if((array[0][14] == 1) and (array[0][46] == 1) ):
        disease = 'Black Quarter'
        checker=checker+1
    if(((array[0][79] == 1) and(array[0][80] == 1)) or ((array[0][79] == 1) and(array[0][8] == 1)) or ((array[0][80] == 1) and(array[0][8] == 1))):
        disease = 'Lumpy Jaw'
        checker=checker+1
    if(((array[0][33] == 1) and(array[0][54] == 1)) or ((array[0][33] == 1) and(array[0][75] == 1)) or ((array[0][54] == 1) and(array[0][75] == 1))):
        disease = 'Foot and Mouth Disease (FMD)'
        checker=checker+1
    if((array[0][1] == 1) and(array[0][53] == 1)):
        disease = 'Tympany/ Bloat'
        checker=checker+1
    if(((array[0][95] == 1) and(array[0][96] == 1)) or ((array[0][95] == 1) and(array[0][76] == 1)) or ((array[0][96] == 1) and(array[0][76] == 1))):
        disease = 'Tick Infestation'
        checker=checker+1
    if((array[0][32] == 1) or(array[0][69] == 1)):
        disease = 'Foot Rot'
        checker=checker+1
    if((array[0][23] == 1)):
        disease = 'Rabies and Injury'
        checker=checker+1
    if(((array[0][101] == 1) and(array[0][102] == 1)) or (array[0][50] == 1) or (array[0][51] == 1) or (array[0][10] == 1)):
        disease = 'Mastitis'
        checker=checker+1
    if((array[0][25] == 1) or(array[0][64] == 1)):
        disease = 'Vitamins and Minerals Deficiency'
        checker=checker+1
    if((array[0][77] == 1) and(array[0][78] == 1)):
        disease = 'Lumpy Skin Disease'
        checker=checker+1
    return (disease,checker)
