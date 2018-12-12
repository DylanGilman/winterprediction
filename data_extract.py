# Name: Dylan Gilman
# Class: Artificial Intelligence
# Data Extraction File for Winter Snowfall Prediction Term Project
# Date: 11/25/2018

def main( ):
    import numpy as np
##    import matplotlib.pyplot as plt
##    from sklearn.naive_bayes import GaussianNB
##    from sklearn import model_selection
    import math
##    import csv

    #Set the file paths for the data files
    temperature_files = ['data/buffalo_niagara_temps.txt',
                         'data/elmira_temps.txt',
                         'data/rochester_temps.txt',
                         'data/syracuse_temps.txt',
                         'data/watertown_temps.txt',
                         'data/oswego_temps.txt',
                         'data/albany_temps.txt',
                         'data/alfred_temps.txt',
                         'data/auburn_temps.txt',
                         'data/batavia_temps.txt',
                         'data/binghamton_temps.txt',
                         'data/canton_temps.txt',
                         'data/cortland_temps.txt',
                         'data/dansville_temps.txt',
                         'data/elmira_temps.txt',
                         'data/fredonia_temps.txt',
                         'data/groton_temps.txt',
                         'data/hemlock_temps.txt',
                         'data/laguardia_temps.txt',
                         'data/port_jervis_temps.txt'
                         ]

    precipitation_files = ['data/Buffalo Niagara.csv',
                           'data/Elmira.csv',
                           'data/Rochester.csv',
                           'data/Syracuse.csv',
                           'data/Watertown.csv',
                           'data/Oswego.csv',
                           'data/Albany.csv',
                           'data/Alfred.csv',
                           'data/Auburn.csv',
                           'data/Batavia.csv',
                           'data/Binghamton.csv',
                           'data/Canton.csv',
                           'data/Cortland.csv',
                           'data/Dansville.csv',
                           'data/Elmira.csv',
                           'data/Fredonia.csv',
                           'data/Groton.csv',
                           'data/Hemlock.csv',
                           'data/LaGuardia.csv',
                           'data/Port_Jervis.csv'
                           ]


    #Data handling variables
    max_snow = 0.0
    max_rain = 0.0
    max_temp = 0.0
    
    min_snow = 100
    min_rain = 100
    min_temp = 100

    entry_count = 0
    unclassed_months = np.empty([14544, 3])
    encoded_data = []
    umIndex = 0

    #Start and end points
    fileindex = 0
    end = len(temperature_files)

    all_data = np.zeros([1,13])

    #Iterate through the files, add data to master lists
    while (fileindex < end):
        print("File: " + precipitation_files[fileindex])
        all_temps = []
        all_precip = []
        yearly_precip = []
        avg_rain = []
        avg_snow = []
        one_year_precip=[]
        yearly_precip=[]

        
        #Open temperature file
        f = open(temperature_files[fileindex])

        #Read first line
        line = f.readline()

        #Read all lines, append each as a list to all_temps
        while (line):
            all_temps.append((line.split())[0:13])
            line = f.readline()

        #Close temperature file
        f.close()

        #Open precipitation file
        f = open(precipitation_files[fileindex])

        #read in first line, skip data line
        line = f.readline()
        line = f.readline()

        #Read all lines, append each as a list to all_precip
        while (line):
            #Extract date, rain, and snow values
            line_split = ((line.split(','))[3:6])

            #Occasionally, we are missing a rain value, so we will set that to zero
            if(line_split[1] == ''):
                line_split[1]='"0.00"'

            #Not all entries have a snow value, thus we must
            #apply the value of 0, and strip off newline characters
            if (line_split[2] == '\n'):
                line_split[2] = '"0.0"'
            else:
                line_split[2]=line_split[2].rstrip('\n')

            #print(line_split)
            index=0
            #Strip off double quotes surrounding data
            while index < len(line_split):
                line_split[index] = (line_split[index])[1:-1]
                index+=1
            #print(line_split)
            all_precip.append(line_split)
            line = f.readline()
        #Close precipitation file
        f.close()
        index+=1
        
        #Convert master lists into numpy 2d arrays
        for element in all_temps:
            all_data=np.vstack([all_data, element])

        index = 0
        while(index < len(all_precip)):
            month_rain = []
            month_snow = []

            #Pull out one day
            day = (all_precip[index])
            #Extract date values for comparison
            year = (day[0])[0:4] 
            month = (day[0])[5:7]

            #Print out rain/snow
            month_rain.append(day[1])
            month_snow.append(day[2])

            index+=1
            
            if(all_precip[index]):
                day = (all_precip[index])
                new_year = (day[0])[0:4]
                new_month = (day[0])[5:7]
                
            
            while(month == new_month):
                month_rain.append(day[1])
                month_snow.append(day[2])

                index+=1

                #ensure file is not empty
                if index < len(all_precip):
                    day = (all_precip[index])
                    new_year = (day[0])[0:4]
                    new_month = (day[0])[5:7]
                else:
                    break

            if index > len(all_precip):
                break

            avg_rain_val = 0
            avg_snow_val = 0
            num_days = 0
            
            for day in month_rain:
                num_days+=1
                avg_rain_val += float(day)

            for day in month_snow:
                avg_snow_val += float(day)

            avg_rain_val /= num_days
            avg_snow_val /= num_days

            #print("Monthly Average: Rain: " + str(avg_rain_val) + " Snow: " + str(avg_snow_val))

            monthPrecip = [round(avg_rain_val,4), round(avg_snow_val,4)]
            one_year_precip.append(monthPrecip)
            

            #If we've advanced one year, push yearly data into main array
            if (year < new_year):
                #Only store the data if all 12 months are there
                #Occasionally, years seem to be calculated with 11 months
                if(len(one_year_precip) == 12):
                    yearly_precip.append(one_year_precip)
                one_year_precip = []
        
        yr=0
        mon=0

        #Now we connect the temperature values with each month
        #New format for each month: Avg Rain, Avg Snow, Avg Temp
        while yr < len(yearly_precip):
            year_precip = yearly_precip[yr]
            year_temp = all_temps[yr]
            
            while mon < len(year_precip):
                month = year_precip[mon]
                year_precip[mon] = np.append(month, year_temp[mon+1])
                mon+=1
                entry_count+=1
            yr+=1
            mon=0

        #Calculate our maximum and minumum values for each class
        for item in yearly_precip:
            for i in item:
                #print(i)
                unclassed_months[umIndex] = i
                umIndex+=1
                
                if(float(i[1]) > float(max_snow)):
                    max_snow=float(i[1])
                if(float(i[0]) > float(max_rain)):
                    max_rain=float(i[0])
                if(float(i[1]) < float(min_snow)):
                    min_snow=float(i[1])
                if(float(i[0]) < float(min_rain)):
                    min_rain=float(i[0])
                if(float(i[2]) > float(max_temp)):
                    max_temp=float(i[2])
                if(float(i[2]) < float(min_temp)):
                    min_temp=float(i[2])
        
        fileindex+=1

    #Data File Read Completed
    #Print out the High/Low and Class size for each variable
    print("\nEnd of datafiles!")
    print("\nTotal Months: " + str(entry_count))
    print("\nTotal Years of Data: " + str(int(entry_count/12)))
    print("\nSnow High: " + str(max_snow))
    print("Snow Low:  " + str(min_snow))
    print("\nRain High: " + str(max_rain))
    print("Rain Low   " + str(min_rain))
    print("\nTemp High: " + str(max_temp))
    print("Temp Low   " + str(min_temp))

    snow_class = round((math.ceil((max_snow) - (min_snow))/10), 2)
    rain_class = round((math.ceil((max_rain) - (min_rain))/10), 2)
    temp_class = round((math.ceil((max_temp) - (min_temp))/10), 2)

    #Convert the real values into class numbers
    #Each variable will be encoded individually
    #December will be encoded as monthly snow class values only
    encoded_data = encode_classes(unclassed_months, min_rain, min_snow, min_temp, max_rain, max_snow, max_temp, rain_class, snow_class, temp_class)

    max_class = 0
    output_data = []
    output_year= []
    i = 0
    j = 0

    while i < len(encoded_data):
        one_year = encoded_data[i]
        #print(one_year)
        #print("Length of One Year: " + str(len(one_year)))
        while j < len(one_year)-1:
            k=0
            while k < 3:
                value = (one_year[j])[k]
                #print("Value " + str(j*3 + k) + ": "+ str(value))
                output_year.append(value)
                k+=1
            j+=1
        #Append the winter class value to the output year
        output_year.append(one_year[11])
        output_data.append(output_year)
        #print(output_year)
        output_year=[]
        j=0
        i+=1

    raw_data = []
    
    #Calculate the largest winter class value that we have
    for i in output_data:
        if i[33] > max_class:
            max_class=i[33]

    print("Max class: " + str(max_class))
    i = 0
 
    #Output the Data to a file
    with open("encodedData.txt", 'w') as file_handler:
        for item in output_data:
            out_item = str(item)[1:-1]
            file_handler.write(out_item + "\n")

    file_handler.close()

    print("Data successfully processed!")


    
def encode_classes(unclassed, mnRain, mnSnow, mnTemp, mxRain, mxSnow, mxTemp, rClass, sClass, tClass):
    import numpy as np
    
    total = len(unclassed)-1
    #Create our output array
    encoded_data = []
    raw_data = []
    encodedIndex = 0

    #Skip the 0th index, as it's junk data
    index = 0
    yearIndex = 0
    singleYear = []
    rawYear = []
    rawMonth = []

    while (index < total):
        month = unclassed[index]
        
        i = 0
        while i < 3:
            rawMonth.append(month[i])
            #print("Raw Month Value for " + str(index) + ": " + str(month[i]))
            month[i] = label(month[i], i, rClass, sClass, tClass, mnRain, mnSnow, mnTemp)
            i+=1

        #Append our classed month values to the encoded singleYear    
        singleYear.append(month)

        #We also want to rebuild the months into years with the raw data and only December classified
        rawYear.append(rawMonth)
        #print("Raw Year Value: " + str(rawYear))
        rawMonth=[]
        
        index+=1
        yearIndex+=1

        #If we've hit 12 months, we have gone through one full year
        if((yearIndex%12)==0):
            #Extract the snow class for December
            decemberSnowClass = ((singleYear[11])[1])
            

            #We strip off all data for December but the class for snowfall
            singleYear = singleYear[:-1]
            #print("Before deleting december: " + str(rawYear))
            december = rawYear[-1][1]
            #print(december)
            rawYear = rawYear[:-1]
            #print("After deleting december: " + str(rawYear))

            #Append the snow class only for December
            singleYear.append(int(decemberSnowClass))
            rawYear.append(round(december, 1))
            #rawYear.append(decemberSnowClass)
            #print("After Appending December Snow Class: " + str(rawYear))

            #Append the data to the year lists
            encoded_data.append(singleYear)
            raw_data.append(rawYear)
            
##            print("RAW DATA:")
##            print(raw_data)
##            print("ENCODED DATA:")
##            print(encoded_data)

            #Empty our local variables to reuse
            rawYear = []
            rawMonth=[]
            singleYear = []
            yearIndex=0

    #Prior to returning the encoded years, we will output our raw data to a file
    #Output the Data to a file
    output=[]

    with open("rawData.txt", 'w') as file_handler:
        for year in raw_data:
            #print("Year: "+str(year))
            for month in year:
                #print(month)
                if type(month) is list:
                    i=0
                    while i<3:
                        file_handler.write(str(month[i]) + ", ")
                        i+=1
                    
                else:
                    file_handler.write(str(month) + " \n")
                    break

                
    file_handler.close()

    #return our encoded data
    return encoded_data

def label(value, index, rClass, sClass, tClass, mnRain, mnSnow, mnTemp):
    classVal = [rClass, sClass, tClass]
    minimumVal = [mnRain, mnSnow, mnTemp]
    
    #Encode labels onto the data
    #Snow encoding - value relates to avg daily snowfall
    if index == 1:
        if value < .325:
            return 0
        if value < .645:
            return 1
        else:
            return 2

    #Round all other data to one decimal point
    else:        
        return round(value, 1)       

main()
