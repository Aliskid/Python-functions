def result(a, c, t, g):
    resultA = (a*100 / (a + c + t + g))
    resultC = (c*100 / (a + c + t + g))
    resultT = (t*100 / (a + c + t + g))
    resultG = (g*100 / (a + c + t + g))
    return resultA, resultC, resultT, resultG

def counting(ADN):

    '''calculates the percentage of each nucleic acid in
     a given sequence. Return a list'''

    ADN2 = []
    counterA = counterT = counterG = counterC = 0
    for i in ADN :
        if i == 'A' :
            counterA = counterA + 1
        elif i == 'T' :
            counterT = counterT + 1
        elif i == 'C' :
            counterC = counterC + 1
        elif i == 'G' :
            counterG = counterG + 1
        else :
            print("please enter A, T, C or G")
        resA, resC, resT, resG = result(counterA, counterC, counterT, counterG)
    ADN2.extend((resA, resT, resC, resG))
    return ADN2

ADN = str(raw_input("Please enter a nucleic sequence"))
reponse = counting(ADN)
print reponse
