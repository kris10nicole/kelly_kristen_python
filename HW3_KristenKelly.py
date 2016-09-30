import pandas as pd   #We import pandas which allows us to use descriptive statistics when analyzing data
import numpy as np    #We use numpy as it is a module that allows the user to work with multi-set arrays and perform functions on them
import matplotlib.pyplot as py   #We import matplotlib which enables us to use plots and graphs in Python


"""I downloaded all of the csv files manually so I could see the data. I also created graphs
via excel so I could check to make sure my output in Python was correct.
I did have trouble with the zip file so I saved a copy of it as a csv file on my computer.
I focused on one data set at a time instead of doing all of them at once.
Some members from Group B helped me with this"""

#Here we use pandas to read the data and assign it to the variable diamond
diamonds = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv', skiprows=1, columnnames= ['carat', 'colour','clarity','certification', 'price'])
#We skip the first row since they have column headers in it, and we assign the string of column headers to the variable columnnames

#For the next data set, we want to read the abalone data and assign column names
abalone=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", columnnames = abalone_columns)
abalone_columns=['Sex','Length','Diameter','Height','WholeWeight','ShuckedWeight', 'VisceraWeight', 'ShellWeight','Rings']

#For the next data set, we want to read the income data and assign column names
KDDdata=pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/income.csv', skiprows=1, ['', 'value','count','mean', 'prop'])


#Now we want to extract the numerical data from the columns for the diamond data set
carats=diamonds.ix[:,0]   #This extracts the data in the carats column
price=diamonds.ix[:,4]    #his extracts the data in the price columnmn


#Now we want to extract the numerical data from the columns for the abalone data set
Length=abalone.ix[:,1]  #This extracts the data in the Length column
Diameter=abalone.ix[:,2]    #This extracts the data in the Diameter column
Height=abalone.ix[:,3]  #This extracts the data in the Height column
WholeWeight=abalone.ix[:,4] #This extracts the data in the WholeWeight column
ShuckedWeight=abalone.ix[:,5]   #This extracts the data in the ShuckedWeight column
VisceraWeight=abalone.ix[:,6]   #This extracts the data in the VisceraWeight column
ShellWeight=abalone.ix[:,7] #This extracts the data in the ShellWeight column
Rings=abalone.ix[:,8]   #This extracts the data in the Rings column


#Now we want to extract the numerical data from the columns for the income data set
value=KDDdata.ix[:,2] 
count=KDDdata.ix[:,3]
mean=KDDdata.ix[:,4]
prop=KDDdata.ix[:,4]


def optimalbinwidth(a, b, c, r):
    """The purpose of this function is to calculate the optimal bin width and return a number of the the bin width
    a=number of elements within the column, i.e. the length of the column
    b=the maximum value of the column 
    c=the minimum value of the column
    r=the interquartile range of the column
    """
    
    x=2*r*a**(-1/3)
    binrange= a-b
    binwidth=binrange/x
    return binwidth

def distribution(data):
    """The purpose of this function is to find the interquartile range of the data set and use the
    dropna function to combine the subset of lower bound outliers(I had some help with this portion of the code),
    upper bound outliers, and the distribution. the interquartile range (r) is calculated again.
    We will finally plot a histogram and a boxplot for each data set.
    I struggled with plotting the data but had some outside help with using the dropna function which was suggested
    by other members of the group. 
    """
    #Below we want to get the descriptive statistics of a generic data set
    summary=data.describe()
    q1=summary['25%'] #Here we assign the Q1 value as 25%
    q3 = summary['75%'] #Here we assign the Q3 value as 75%
    r =q3-q1 #We recalculate the interquartile range (r) as the difference between q3 and q1
    lower_bound=q1-1.5*r #We know from math/stats that the lower bound is equal to q1 minus 1.5*interquartile range
    upper_bound =q3+1.5*r #We know from math/stats that the upper bound is equal to q3 plus 1.5*interquartile range
    upperbound_outliers=data.where(data>upper_bound).dropna() #Here we want to extract any upper bound outliers
    lowerbound_outliers=data.where(data < lower_bound).dropna() #Here we want to extract any lower bound outliers
    median=data.where(data<=upper_bound).dropna()  #Here we specify wher the median is
    median=median.where(median>=lower_bound).dropna() #Here we specify wher the median is
    
    
    if lowerbound_outliers.size !=0: #If the set is empty, then we do not produce a plot
        summary2 = lowerbound_outliers.describe()
        qx1=summary2['25%']  #Here we recalculate the interquartile range, r
        qx3=summary2['75%']
        r2=qx3-qx1
        LowerBoundBins=optimalbinwidth(lowerbound_outliers.size, float(lowerbound_outliers.max()), float(lowerbound_outliers.min()), float(r2))
        plot.figure()
        lowerbound_outliers.plot.hist(bins=round(LowerBoundBins)).set_title('Lower Bound Outliers');
    if median.size!= 0:  #If the set is empty, then we do not produce a plot
        summary3=median.describe()
        qx2=summary3['25%'] #Here we recalculate the interquartile range, r
        qx4=summary3['75%']
        r3=qx4-qx2
        medianbins=optimalbinwidth(float(median.size), float(median.max()), float(median.min()), float(r3))
        plot.figure()
        median.plot.hist(bins=round(medianbins)).set_title('Central Distribution of Data')
    if upperbound_outliers.size !=0 :   #If the set is empty, then we do not produce a plot
        summary4=upperbound_outliers.describe()
        qx5=summary4['25%']  #Here we recalculate the interquartile range, r
        qx6=summary4['75%']
        r4=qx6-qx5
        UpperBoundBins=optimalbinwidth(upperbound_outliers.size, float(upperbound_outliers.max()), float(upperbound_outliers.min()), float(r4))
        plot.figure()
        upperbound_outliers.plot.hist(bins=round(UpperBoundBins)).set_title('Upper Bound Outliers')
    
    plot.figure()
    data.plot.box() #Here we plot the box plot for the data sets

""""Now we want to run the function with the three different data sets to see if it works"""
distribution(carats)
distribution(price)
distribution(Length)
distribution(value)
