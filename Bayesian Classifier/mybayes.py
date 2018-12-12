# Name: Dylan Gilman, Donny McCoy
# Class: Artificial Intelligence
# Assignment: Term Project - Winter Prediction
# Date: 12/10/2018

#Given two lists, return a list including only common numbers; no duplicates
def main( ):
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.naive_bayes import GaussianNB
    from sklearn import model_selection

    #We will get warnings, as the data set does not work well for
    #NB Classification. This will supress the F1 and Precision warning
    #for not enough data points in specific classifications,
    #as we want just a clean print-out
    import warnings
    warnings.filterwarnings("ignore")

    input_file='../encodedData.txt'
    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:,:-1], data[:, -1]

##    print(X[:])
##    print(y[:])

    count0 = 0
    count1 = 0
    count2 = 0
    for item in y:
        if item == 0:
            count0 += 1
        if item == 1:
            count1 += 1
        if item == 2:
            count2 += 1

    print("Class 0 Count: " + str(count0))
    print("Class 1 Count: " + str(count1))
    print("Class 2 Count: " + str(count2))

    #Create our classifier
    classifier = GaussianNB()
    classifier.fit(X, y)
    y_pred = classifier.predict(X)

    accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
    print("\nAccuracy of Naive Bayes classifier =", round(accuracy, 2), "%")

    print("y_pred sum =", (y == y_pred).sum());
    print("above * 100 =", 100 * (y == y_pred).sum());
    print("X.shape[0] =", X.shape[0]);

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15, random_state=0)
    
    classifier_new = GaussianNB()
    classifier_new.fit(X_train, y_train)
    y_test_pred = classifier_new.predict(X_test)

    accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
    print("\nAccuracy of the new classifier =", round(accuracy, 2), "%")

    num_folds = 5
    accuracy_values = model_selection.cross_val_score(classifier,  X, y, scoring='accuracy', cv=num_folds)
    print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%")

    precision_values = model_selection.cross_val_score(classifier, X, y, scoring='precision_weighted', cv=num_folds)
    print("Precision: " + str(round(100*precision_values.mean(), 2)) + "%")

    f1_values = model_selection.cross_val_score(classifier, X, y, scoring='f1_weighted', cv=num_folds)
    print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")

main()
