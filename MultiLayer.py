from FinalVectorConversion import fileFreq
from sklearn.neural_network import MLPClassifier
#this particular instance is being trained on eating disorder and depression
#and being tested on a similar set

'''
X is the training set
first parameter of fileFreq is your desired keywords, second parameter is the
directory that you want to search
'''
X = fileFreq('C:/Research/Keywords/Full.txt','C:/Research/Dataset/Train1/*.txt')

xTest = fileFreq('C:/Research/Keywords/Full.txt','C:/Research/Dataset/TestB1/*.txt')

yTrain = [1]*100 + [0]*100

yTest = [1]*20 + [0]*20

#in order to modify the number of neurons, change the first parameter of hidden_layer_sizes
clf = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, hidden_layer_sizes = (3, 2), random_state = 1)

#this fits the Perceptron on the training data
clf.fit(X, yTrain)    

#this tests the Perceptron on a different set of data from the training set
print(clf.score(xTest,yTest))