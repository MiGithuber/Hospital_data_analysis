"""
Hospital Data Analysis

This project explains the data of the hospitals over germany.

Author: Mihir N.Shanbhag
Institution: University of Potsdam
Date: 4/06/2023
"""
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import seaborn as sns

def ques_1(df):
    """

    Args:
        df: An update on the current situation in the health care system with the help of the data of 22 years?"
    Returns:
            A barplot Visualization
        ...
    """
    sns.barplot(x=df['Year'],y=df['Hospitals'],data=df)

    
def ques_2(df):
    """
    Args:
        df: Amount of days the patient stays on average in the hospital?
    Returns:
            A lineplot Visualization
    
    """
    plt.plot(df['Year'],df['Patients'])
    plt.show()

def ques_3(df):
    """
    Args:
        df: Health of citizens over the 22yrs?
    Returns:
            A lineplot Visualization
    """
    plt.plot(df['Year'],df['Average occupancy of hospital beds'])
    plt.show()

def ques_4(df):
    """
    Args:
        df: What is the cost over the years?
    Returns:
            A lineplot Visualization
    """
    plt.plot(df['Year'],df['Occupancy / billing days'])
    plt.show()



def main(args):
    """
    [It reads the dataset which is present in the excel format and then calls the (5 questions).]
    """

    # Open data file
    df = pd.read_excel(args.excel_file)

    ques_1()

    ques_2()

    ques_3()

    ques_4()




if __name__ == "__main__":
    USAGE="Input the dataset file"
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('excel_file', type=str, help="Input the data file")
    args = parser.parse_args()
    main(args)
