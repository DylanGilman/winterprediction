# Name: Dylan Gilman, Donny McCoy
# Winter Prediction Term Project
# Artificial Intelligence
# Neural Network

def main():
    import numpy as np
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import preprocessing
    from sklearn.svm import LinearSVC
    from sklearn.svm import SVC
    from sklearn.multiclass import OneVsOneClassifier
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    import neurolab as nl

    input_file = '../encodedData.txt'

    X = []
    y = []
    count_class0 = 0
    count_class1 = 0
    count_class2 = 0


    with open(input_file, 'r') as f:
        for line in f.readlines():
            data = line[:-1].split(', ')
            if data[-1] == '0':
                X.append(data)
                count_class0 += 1

            if data[-1] == '1':
                X.append(data)
                count_class1 += 1

            if data[-1] == '2':
                X.append(data)
                count_class2 += 1

    print('Data Spread:- ')
    print('\tClass 0: ' + str(count_class0))
    print('\tClass 1: ' + str(count_class1))
    print('\tClass 2: ' + str(count_class2))

    #Create a numpy array out of our input data
    X = np.array(X)

    X_encoded = np.empty(X.shape)
    
    for i,item in enumerate(X[0]):
        X_encoded[:, i] = X[:, i]

    X = X_encoded[:, :-1]
    y = X_encoded[:, -1]
    
    #Calculate the min/max values for each set of data
    minmax_X = []
    X1, y1 = X.tolist(), y.tolist();
    for i,item in enumerate(X[0]):
            minmax_X.append([X[:,i].min(),X[:,i].max()])

    #If the maximum value is set to 0, we set the max to 1
    #Reason: to prevent divide by zero in the training process
    #max - min will be equal to 1, as if max is 0, min is 0
    for item in minmax_X:
        if item[1] == 0:
            item[1] = .00000000001

    #Changes list values from [1, 0, 1] to [[1], [0], [1]]
    y = [[int(y)] for y in y1]

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X1, y, test_size=0.3)    

    print('Creating neural network...')
    nn = nl.net.newff(minmax_X, [15,7,1])
    nn.trainf = nl.train.train_gd

    print('Training neural network...')
    error_progress = nn.train(X_train, y_train, goal=0.01, epochs=100, lr=.1)
    
    plt.figure()
    plt.plot(error_progress)
    plt.xlabel('Epochs')
    plt.ylabel('Error')
    plt.title('Training progress')
    plt.show()

    #Calculating the accuracy of the model
    y_test_pred = nn.sim(X_test)

    y = np.array(y)
    
    y1_pred = np.empty(y.shape);


    for t in X1:

        p = nn.sim([t])[0]

        np.append(y1_pred, p)

    y1_pred = nn.sim(X1)[0,:] 

    accuracy = 100.0 * ((y == y1_pred).sum() / y.shape[0])

    print("Accuracy of the logistic classifier =", round(accuracy,2), "%")
main()
