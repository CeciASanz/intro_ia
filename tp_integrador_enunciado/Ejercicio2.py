import numpy as np
import matplotlib.pyplot as plt

truth = np.array([1,1,0,1,1,1,0,0,0,1])
prediction = np.array([1,1,1,1,0,0,1,1,0,0])

#True Positive (TP): El valor verdadero es 1 y el valor predicho es 1
TP = np.count_nonzero(np.logical_and(truth,prediction))
print(f'TP: {TP}')

#True Negative (TN): El valor verdadero es 0 y el valor predicho es 0
TN = np.count_nonzero(np.logical_not(np.logical_or(truth, prediction)))
print (f'TN: {TN}')

#False Positive (FP): El valor verdadero es 0 y el valor predicho es 1
FP = np.count_nonzero(np.logical_and(np.logical_xor(truth, prediction), prediction))
print (f'FP: {FP}')

#False Negative (FN): El valor verdadero es 1 y el valor predicho es 0
FN = np.count_nonzero(np.logical_and(np.logical_xor(truth, prediction), truth))
print (f'FP: {FN}')

#Precision = TP / (TP + FP)
precision = TP / (TP + FP)
#Recall = TP / (TP + FN)
recall = TP / (TP + FN)
#Accuracy = (TP + TN) / (TP + TN + FP + FN)
accuracy = (TP + TN) / (TP + TN + FP + FN)

print(f'Precision: {precision}\n Recall: {recall}\n Accuracy: {accuracy}')