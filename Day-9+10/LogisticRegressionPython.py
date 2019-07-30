import csv
import math
import copy, random

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def str_to_float(dataset):
    for row in range(len(dataset)):
        for col in range(len(dataset[row])):
            dataset[row][col] = float(dataset[row][col])

def minMax(dataset):
    minMaxData = []
    for i in range(len(dataset[0])):
        col = [row[i] for row in dataset]
        minValue = min(col)
        maxValue = max(col)
        minMaxData.append([minValue, maxValue])
    return minMaxData

def normalization(dataset, minMaxData):
    for row in dataset:
        for i in range(len(row)):
            numer = row[i] - minMaxData[i][0]
            denom = minMaxData[i][1] - minMaxData[i][0]
            row[i] = numer / denom

def crossValidation(dataset,k=5):
    dataset_copy = copy.deepcopy(dataset)
    fold_size = len(dataset) // k
    folds = []
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def predict(coef, row):
    y_pred = coef[0]
    for i in range(len(row) - 1):
        y_pred += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-y_pred))

def accuracyScore(actual, predicted):
    score = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            score += 1
    return score / len(actual) * 100

def evaluateAlgorithm(dataset,epochs,learning_rate):
    scores = []
    folds = crossValidation(dataset)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])
        test = []
        for row in fold:
            rowCopy = list(row)
            rowCopy[-1] = None
            test.append(rowCopy)
        pred = logisticRegression(train,test,epochs,learning_rate)
        actual = [row[-1] for row in fold]
        score = accuracyScore(actual, pred)
        scores.append(score)
    return scores

def stochasticGradient(dataset,epochs,learning_rate):
    coef = [0] * len(dataset[0])
    for i in range(epochs):
        for row in dataset:
            y_pred = predict(coef, row)
            loss = y_pred - row[-1]
            coef[0] = coef[0] - learning_rate * loss
            for j in range(len(row) - 1):
                coef[j+1] = coef[j+1] - learning_rate * loss * row[j]
    return coef

def logisticRegression(train,test,epochs,learning_rate):
    predictions = []
    coef = stochasticGradient(train,epochs,learning_rate)
    for row in test:
        y_pred = predict(coef,row)
        predictions.append(round(y_pred))
    return predictions


filename = 'pima-indians-diabetes.data.csv'
dataset = read_csv(filename)
str_to_float(dataset)
minMaxData = minMax(dataset)
normalization(dataset, minMaxData)

epochs = 1000
learning_rate = 0.001
e = evaluateAlgorithm(dataset,epochs, learning_rate)
print("All Accuracies :",e)
print("Final Accuracy :",sum(e) / len(e))





