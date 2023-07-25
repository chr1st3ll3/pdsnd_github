import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAYS = {1: "Sunday",2: "Monday",3: "Tuesday",4: "Wednesday",5: "Thursday",6: "Friday",7: "Saturday",8: "all"}
MONTHS =  {"january":1 ,"february": 2,"march": 3,"april": 4,"may": 5,"june": 6}
MONTHS_NAMES =  {1:"January" ,2: "February", 3:"March", 4: "April",5: "May",6:"June"}
def get_filters():
    #return "chicago", "1", "3"
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city=''
        while city == '':
            city = input('Pick a city (Chicago, New York, Washington): ')
            city = city.lower()
            try:
                if (city != ""):
                    continue
                else:
                    city = ""
            except:
                print("An Error occurred")
        
        filter=""
        month=-1
        day=-1
        while filter not in ("month", "day", "both", "none"):
            filter = (input('Would you like to filter by month, day, both, or not at all? (Type "none" for no filter) ')).lower()

            if (filter == "month" or filter == "both" ):
                # get user input for month (all, january, february, ... , june)
                if filter == "month": day="all"
                while month == -1:
                    try:
                        month = input('Pick a month (January, February, March, April, May, June): ').lower()
                        if month in ["january", "february", "march", "april", "may", "june"]:
                            month = MONTHS[month]
                        else:
                            month = -1
                            print("An Error occurred: Make sure you wrote an number whithin the range")
                    except Exception as e:
                            print("Make sure to pick a number: ", e )
            
            if (filter == "day" or filter == "both" ):
                # get user input for day of week (all, monday, tuesday, ... sunday)
                if filter == "day": month="all"
                while day == -1:
                    try:
                        day = int(input('Pick a day (E.g. 1 for Sunday) : '))
                        if day in [0,1,2,3,4,5,6,7]:
                            day = day
                        else:
                            day = -1
                    except Exception as e:
                        print("Make sure to pick a number within the range" )

            if (filter == "none"):
                day = "all"
                month = "all"
        
        
        
        print('-'*40)
    except:
        print("Error")

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
    try:
        df = pd.read_csv(CITY_DATA[city])
        
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
    
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_of_week
        
        # filter by month if applicable
        if month != 'all':
            # filter by month to create the new dataframe
            df = df[df['month'] == int(month)]
    
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == int(day)]

        return df
    except:
        print("Error")
        return 
    
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    try:
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        popular_month = df['month'].mode()[0]
        df2 = df[df['month'] == popular_month]
        popular_month_count = df2['month'].count()
        # display the most common month
        print("The most common month was: ", MONTHS_NAMES[popular_month], ", Count: ", popular_month_count)

        
        popular_day_of_week = df['day_of_week'].mode()[0]
        df2 = df[df['day_of_week'] == popular_day_of_week]
        popular_day_of_week_count = df2['day_of_week'].count()
        # display the most common day of week
        print("The most common day was: ", DAYS[popular_day_of_week], ", Count: ", popular_day_of_week_count)

        popular_hour = df['hour'].mode()[0]
        df2 = df[df['hour'] == popular_hour]
        popular_hour_count = df2['hour'].count()
        # display the most common start hour
        print("The most common start hour was: ", popular_hour, ", Count: ", popular_hour_count)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print("Error")

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    try:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        start_station = df['Start Station'].mode()[0]
        df2 = df[df['Start Station'] == start_station]
        start_station_count = df2['End Station'].count()
        # display most commonly used start station
        print("The most common start station was: ", start_station, ", Count: ", start_station_count)

        end_station = df['End Station'].mode()[0]
        df2 = df[df['End Station'] == end_station]
        end_station_count = df2['End Station'].count()
        # display most commonly used end station
        print("The most common end station was: ", end_station, ", Count: ", end_station_count)

    
        full_stations = df['Start Station'] + " - " + df['End Station']
        popular_combination = full_stations.mode()[0]
        # display most frequent combination of start station and end station trip
        print("The most frequent combination of start station and end stationwas: ", popular_combination, "") 


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print("Error")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        total_time = df["Trip Duration"].sum()
        # display total travel time
        print("Total Duration: ", total_time, ", Count: ", df["Trip Duration"].count())

        avg_time = df["Trip Duration"].mean()
        # display mean travel time
        print("Average Duration: ", avg_time)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print("Error")


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
       
        user_types = df['User Type'].value_counts()
        # Display counts of user types
        print("The types of users: \n", user_types)

        if city == "chicago" or city == "new york city":
            gender = df['Gender'].value_counts()
            # Display counts of gender
            print("The gender of users: \n", gender)


            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            common_year = df['Birth Year'].mean()
            # Display earliest, most recent, and most common year of birth
            print("The erliest year of birth is: ", int(earliest))
            print("The most recent year of birth is: ",int(most_recent))
            print("The most common year of birth is: ", int(common_year))
    
    except Exception as e:
        print("Error : " , e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dislplay_data(df):
    """Raw data is displayed upon request by user"""
    opt = ""
    start_loc = 0
    try:
         while opt == "":
            opt = input("Would yoou like to view 5 rows of individual trip data? Enter yes or no: ").lower()
            if opt == "yes":
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                opt = ""
            elif opt == "no":
                break
            else:
                print("Error: pick a valid option.")
                opt=""
              
    except:
        print("Error")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dislplay_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
