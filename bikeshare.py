import time
import pandas as pd
import numpy as np
days = ["all","sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
monthes = ["all","january","February","march","april","may","june"] 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=""
    month=""
    day=""
    while(CITY_DATA.get(city)==None):
        city  = input("Enter name of the city chicago,new york city or washington: ").lower()
        if CITY_DATA.get(city)==None:
            print("Please eter valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while(month not in monthes):
        month  = input("Enter name of the month all, january, february, ... , june: ").lower()
        if month not in monthes:
            print("Please enter valid month name")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(day not in days):
        day  = input("Enter name of day of the week all, monday, tuesday, ... sunday: ").lower()
        if day not in days:
            print("Please enter vaild day in vaild format")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    month= monthes.index(month)+1
    if day == "all" and month != "all":
        df =df[df['month']==month]
    elif month=="all" and day !="all":
        df =df[df['day']==day.title()]
    elif month !="all" and day !="all":
        df=df[df['day']==day.title()]
        df=df[df["month"]==month]
    else:
        return df
        
    
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month {} ".format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of week {} ".format(df["day"].mode()[0]))

    # TO DO: display the most common start hour
    
    print("The most common start hour {} ".format(df["hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station {} ".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station {} ".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station tri
    
    
    print("The most frequent combination of start station and end station {} ".format(df[["Start Station","End Station"]].mode().values))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["End Time"]=pd.to_datetime(df["End Time"])
    df["Travel Time"] = df["End Time"]-df["Start Time"]
    print("total traval time = {} ".format(df["Travel Time"].sum()))
    # TO DO: display mean travel time
    print("mean traval time = {} ".format(df["Travel Time"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc =0
    end_loc = 5
    while(view_data =="yes"):
        print(df.iloc[start_loc:end_loc])
        start_loc+=5
        end_loc+=5
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year: {} the most recent year: {} and most common year {}".format(int(df["Birth Year"].min()),int(df["Birth Year"].max()),int(df["Birth Year"].mode()[0])))
    except:
        print("year and gender data is not provided for this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
