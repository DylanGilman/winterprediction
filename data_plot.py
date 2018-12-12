# Name: Dylan Gilman, Donny McCoy
# Winter Prediction Term Project
# Artificial Intelligence
# Winter Data Prediction Plotting

def main( ):
    import pickle
    import numpy as np
    from sklearn import linear_model
    import sklearn.metrics as sm
    import matplotlib.pyplot as plt
    from sklearn import model_selection

    #------------------------------
    input_file='encodedData.txt'

    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:, :-1], data[:, -1]
    #------------------------------

##    print("X")
##    print(X)
##
##    print("y")
##    print(y)

    X_may_aug = []
    X_jun_sep = []
    X_jan_may = []
    X_jun_jul = []
    X_jun = []
    X_aug_nov = []
    X_nov = []

    X_may_aug_rain = []
    X_jun_sep_rain = []
    X_jan_may_rain = []
    X_jun_jul_rain = []
    index = 0

    while index < len(X):
        X_may_aug.append((X[index][14] + X[index][17] + X[index][20] + X[index][23])/4)
        X_jun_sep.append((X[index][17] + X[index][20] + X[index][23] + X[index][26])/4)
        X_jan_may.append((X[index][2] + X[index][5] + X[index][8] + X[index][11])/4)
        X_jun_jul.append((X[index][17] + X[index][20])/2)
        X_jun.append(X[index][17])
        X_aug_nov.append((X[index][23] + X[index][26] + X[index][29] + X[index][32])/4)
        X_nov.append(X[index][32])

        X_may_aug_rain.append((X[index][12] + X[index][15] + X[index][18] + X[index][21])/4)
        X_jun_sep_rain.append((X[index][15] + X[index][18] + X[index][21] + X[index][24])/4)
        X_jan_may_rain.append((X[index][0] + X[index][3] + X[index][6] + X[index][9])/4)
        X_jun_jul_rain.append((X[index][15] + X[index][18])/2)

        index += 1

    print("Length y: " + str(len(y)))
    print("Length jan-may: " + str(len(X_jan_may)))
    print("Length may-aug: " + str(len(X_may_aug)))
    print("Length jun-sep: " + str(len(X_jun_sep)))
    print("Length jun-jul: " + str(len(X_jun_jul)))

    print("Length jan-may rain: " + str(len(X_jan_may_rain)))
    print("Length may-aug rain: " + str(len(X_may_aug_rain)))
    print("Length jun-sep rain: " + str(len(X_jun_sep_rain)))
    print("Length jun-jul rain: " + str(len(X_jun_jul_rain)))

    #Plotting with temperature values against December snowfall
    plt.scatter(y, X_jan_may, color='green')
    plt.title('January - May: Temp')
    plt.show()
    
    plt.scatter(y, X_may_aug, color='green')
    plt.title('May - August: Temp')
    plt.show()
    
    plt.scatter(y, X_jun_sep, color='green')
    plt.title('June - September: Temp')
    plt.show()

    plt.scatter(y, X_jun_jul, color='green')
    plt.title('June - July: Temp')
    plt.show()

    plt.scatter(y, X_jun, color='green')
    plt.title('June: Temp')
    plt.show()

    plt.scatter(y, X_nov, color="green")
    plt.title("November: Temp")
    plt.show()

    #Plotting with rain values against December snowfall
    plt.scatter(y, X_jan_may_rain, color='black')
    plt.title('January - May: Rain')
    plt.show()
    
    plt.scatter(y, X_may_aug_rain, color='black')
    plt.title('May - August: Rain')
    plt.show()
    
    plt.scatter(y, X_jun_sep_rain, color='black')
    plt.title('June - September: Rain')
    plt.show()

    plt.scatter(y, X_jun_jul_rain, color='black')
    plt.title('June - July: Rain')
    plt.show()
    
main()
