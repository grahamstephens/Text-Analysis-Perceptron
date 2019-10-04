# Text-Analysis-Perceptron
Perceptron optimized for scanning and analyzing multiple .txt documents

## How to Use
The input to the Perceptron, X and Y, can be any lists of equal length. X can contain ints or floats, and Y must be comprised of either 0 or 1. For text analysis, the imported fileFreq function can be used to automatically search a directory of text-files for a certain group  of keywords. The parameters for fileFreq(keywords, direct) will specify which text files will be searched and what keywords will be searched. keywords and direct should both be strings that specify the location of a .txt file of keywords and a directory of target .txt files, respectively. The output of fileFreq will be a list of ints that is as long as the number of keywords in the keyword file. The fileFreq output can be initialzied to the X value of the Perceptron for simple text-analysis.

## Optimal Architecture Parameters
The Perceptron was tested multiple times with different archiecture parameters on the same set of data. It is optimal to have 2-6 neurons in the 2nd layer of the neural network, with more neurons for larger datasets (>400-500) and less neurons for small datasets (50-100). After 6 neurons have been added, the output value of the Perceptron value begins to fluctuate approximately every 7th neuron on an observable pattern.

## Original Data Used
This Perceptron was originally created to search for "depressed" text by searching for absolutist words within .txt files. The original dataset used was borrowed from a 2018 study about the link between absoutist word usage and depression (Al-Mosaiwi, M. & Johstone, T. "In An Absolute State...)
