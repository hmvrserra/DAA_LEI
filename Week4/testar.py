
import time
from random import choice

# tryItABunch: executa uma dada função um dado monte de vezes e cronometra cada execução.
#
# Input: myFn: uma função tendo por input um *integer*
# Output: duas *lists* nValues e tValues correspondendo a executar myFn com argumento nValues[i], um numTrials de vezes, que levou tValues[i] milliseconds (em média).
#
# Other optional args:
#    - startN: smallest n to test
#    - endN: largest n to test
#    - stepSize: test the several n in increments of stepSize between startN and endN
#    - numTrials: for each n tests, do numTrials tests and average them
def tryItABunch(myFn, startN=10, endN=100, stepSize=10, numTrials=20):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        # run myFn (n) several times and average
        runtime = 0
        for t in range(numTrials):
            start = time.time()
            myFn( n )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

# Em seguida pode sempre fazer:
# plot(nValues, tValues)
# ou algo no género

# Outra variação:
# Input: myFn: a function which takes as input a *list* of *integers*
# Output: lists nValues and tValues as above.
#
# Other optional args:
#    - startN: smallest n to test
#    - endN: largest n to test
#    - stepSize: test n's in increments of stepSize between startN and endN
#    - numTrials: for each n tests, do numTrials tests and average them
#    - listMax: the input lists of length n will have values drawn uniformly at random from range(listMax)

# Porque não altera estas duas funções para um única que tem a opção de inicializar a lista aleatória de inteiros ou não...

def tryItABunch2(myFn, startN=10, endN=100, stepSize=10, numTrials=20, listMax = 10):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst = [ choice(range(listMax)) for i in range(n) ] # generate a *random* list of length n
            start = time.time()
            myFn( lst )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

