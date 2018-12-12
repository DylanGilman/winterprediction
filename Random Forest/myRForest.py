# Name: Dylan Gilman, Donny McCoy
# Class: Artificial Intelligence
# Assignment: Term Project - December Snow Prediction
# Date: 12/08/2018

#Random Forest Classifier for Winter Weather Prediction
def main():    
    import numpy as np
    from sklearn.metrics import classification_report
    from sklearn import model_selection
    from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
    from sklearn import model_selection
    from sklearn.metrics import classification_report

    print("Random Forest Classification: ")
    
    input_file = '../encodedData.txt'
    print("Loading Data From ", input_file)
    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:, :-1], data[:, -1]

    #20% of data for testing
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.20, random_state=5)

    #Forest size of 5000, maximum tree depth of 25, using entropy to create our trees
    params = {'n_estimators': 5000, 'max_depth': 25, 'random_state': 3, 'criterion':'entropy'}

    #Standard Random Forest Classifier
    rfclassifier = RandomForestClassifier(**params)
    rfclassifier.fit(X_train, y_train)
    y_test_pred = rfclassifier.predict(X_test)

    class_names = ['Class-0', 'Class-1', 'Class-2']
    print("\n" + "#"*40)
    print("\nRandom Forest Classifier:")
    print("\nClassifier performance on training dataset\n")
    print(classification_report(y_train, rfclassifier.predict(X_train), target_names=class_names))
    print("#"*40 + "\n")

    print("#"*40)
    print("\nClassifier performance on test dataset\n")
    print(classification_report(y_test, y_test_pred, target_names=class_names))
    print("#"*40 + "\n")

    #Extra Trees Random Forest Classifier
    etclassifier = ExtraTreesClassifier(**params)
    etclassifier.fit(X_train, y_train)
    y_test_pred = etclassifier.predict(X_test)

    class_names = ['Class-0', 'Class-1', 'Class-2']
    print("\n" + "#"*40)
    print("\nExtra Trees Classifier:")
    print("\nClassifier performance on training dataset\n")
    print(classification_report(y_train, etclassifier.predict(X_train), target_names=class_names))
    print("#"*40 + "\n")

    print("#"*40)
    print("\nClassifier performance on test dataset\n")
    print(classification_report(y_test, y_test_pred, target_names=class_names))
    print("#"*40 + "\n")

    menu_select = -1
    print("\n" + "#"*40)   
    print("\nMENU:\n")
    print("1. Input User Data")
    print("2. Rochester 2018 Example")
    print("0. Quit")
    menu_select = input("User selection: ")
    print("\n" + "#"*40)   

    while (menu_select != 0):
        #Allow users to input weather data to predict
        if menu_select == '1':
            input_test = getUserData()
            y_test_pred = etclassifier.predict(input_test)
            print("\n\nExpected total snowfall for December: ", snowfall(y_test_pred))

        #Sample Data for Rochester, NY 2018
        elif menu_select == '2':
            #[jan_rain, jan_snow, jan_temp, feb_rain, feb_snow, feb_temp ... nov_snow, nov_temp]
            input_test = [[0.1, 2.0, -3.9, 0.1, 1.0, 1.1, 0.1, 2.0, 0.0, 0.1, 0.0,
                          5.0, 0.1, 0.0, 18.3, 0.1, 0.0, 20, 0.1, 0.0, 23.9, 0.1,
                          0.0, 23.3, 0.1, 0.0, 20, 0.1, 0.0, 10.6, 0.2, 1.0, 2.8]]
            y_test_pred = etclassifier.predict(input_test)
            print("\nExpected total snowfall for December: ", snowfall(y_test_pred))
        elif menu_select == '0':
            quit()
        else:
            print("\nInvalid menu choice! Please try again")

        print("\n" + "#"*40)   
        print("\nMENU:\n")
        print("1. Input User Data")
        print("2. Rochester 2018 Example")
        print("0. Quit")

        menu_select = input("User selection: ")

        print("\n" + "#"*40)
        

        
def getUserData():
    print("\n\nUser data input:")
    print("\nJanuary:")
    jan_r = input("Avg. Rain: ")
    jan_s = input("Avg. Snow: ")
    jan_t = input("Avg. Temp: ")

    print("\n\nFebruary:")
    feb_r = input("Avg. Rain: ")
    feb_s = input("Avg. Snow: ")
    feb_t = input("Avg. Temp: ")

    print("\n\nMarch:")
    mar_r = input("Avg. Rain: ")
    mar_s = input("Avg. Snow: ")
    mar_t = input("Avg. Temp: ")

    print("\n\nApril:")
    apr_r = input("Avg. Rain: ")
    apr_s = input("Avg. Snow: ")
    apr_t = input("Avg. Temp: ")

    print("\n\nMay:")
    may_r = input("Avg. Rain: ")
    may_s = input("Avg. Snow: ")
    may_t = input("Avg. Temp: ")

    print("\n\nJune:")
    jun_r = input("Avg. Rain: ")
    jun_s = input("Avg. Snow: ")
    jun_t = input("Avg. Temp: ")

    print("\n\nJuly:")
    jul_r = input("Avg. Rain: ")
    jul_s = input("Avg. Snow: ")
    jul_t = input("Avg. Temp: ")

    print("\n\nAugust:")
    aug_r = input("Avg. Rain: ")
    aug_s = input("Avg. Snow: ")
    aug_t = input("Avg. Temp: ")

    print("\n\nSeptember:")
    sep_r = input("Avg. Rain: ")
    sep_s = input("Avg. Snow: ")
    sep_t = input("Avg. Temp: ")

    print("\n\nOctober:")
    oct_r = input("Avg. Rain: ")
    oct_s = input("Avg. Snow: ")
    oct_t = input("Avg. Temp: ")

    print("\n\nNovember:")
    nov_r = input("Avg. Rain: ")
    nov_s = input("Avg. Snow: ")
    nov_t = input("Avg. Temp: ")

    yearlyData = [[jan_r, jan_s, jan_t, feb_r, feb_s, feb_t, mar_r, mar_s, mar_t,
                  apr_r, apr_s, apr_t, may_r, may_s, may_t, jun_r, jun_s, jun_t,
                  jul_r, jul_s, jul_t, aug_r, aug_s, aug_t, sep_r, sep_s, sep_t,
                  oct_r, oct_s, oct_t, nov_r, nov_s, nov_t]]

    for year in yearlyData:
        i=0
        while(i<len(year)):
            if year[i] == '':
                year[i] = 0.0
            else:
                year[i] = float(year[i])

            i+=1

    
    return yearlyData

def snowfall(n):
    if n == 0:
        return "Up to 10 inches"
    if n == 1:
        return "Up to 20 inches"
    if n == 2:
        return "Greater than 20 inches"

main()
