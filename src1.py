import pandas as pd
import tweepy
from datetime import datetime, date
import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler("AUTH KEY", "AUTH KEY SECRET")
auth.set_access_token("ACCESS TOKEN", "ACCESS TOKEN SECRET")

# Create API object
api = tweepy.API(auth)

#read csv
data0=pd.read_csv('s.csv')
data0['Birthday'] =  pd.to_datetime(data0['Birthday'], format='%Y-%m-%d') #convert to date
data0['Birthday'] = data0.Birthday.dt.strftime('%m-%d') #remove the year
df_list=data0.values.tolist() #converts dataframe to list
today = date.today() #retrieve today's date

#formatting the days so that it is consistent with csv
days_under_10 = [1,2,3,4,5,6,7,8,9] 
if today.day in days_under_10:
    day = "0" + str(today.day)
    today_formatted = str(today.month) + "-" + day
else:
    today_formatted= str(today.month) + "-" + str(today.day) #formatting current month-day

#list of months
Months=["Placeholder", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for row in range(len(df_list)):
    #check date of the person's birthday and the date of today
    if str(df_list[row][2]) == today_formatted: #if their birthday is today
        this_month= str(Months[today.month]) #retrieve the Month based on month number
        this_day= str(today.day) #convert the day to a string
        #Publish Tweet
        api.update_status("It's " + this_month + " " + this_day + ", you know what that means! Happy Birthday "+ str(df_list[row][0]) + "," + str(df_list[row][1]) + "! Hope it's Flavortown-tastic.")


