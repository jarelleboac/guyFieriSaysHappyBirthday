# GUY FIERI SAYS HAPPY BIRTHDAY
Fun side project. This is a Twitterbot which allows for people to sign up via Google Form and wishes people happy birthday from a *fake* Guy Fieri. The goal of this bot is to put a smile on someone's face. 

![alt text](https://media2.fdncms.com/clevescene/imager/u/original/33361684/wkbvjbjywtwoqyo_800x450_nopad.5ef0d95835b98.jpg)


## Improvements
Deploy to Heroku
Function to clean csv

## Quickstart
### Running the bot

Make sure to have the Google Form responses exported to .csv.

To do a manual run, navigate to the directory and simply execute the following command:
```
python NAME_OF_PROGRAM.py
```
To do scheduled runs of your email bot, install `hickory`, which is a simple command line tool for scheduling Python scripts:
```
pip install hickory
```

Via command line, navigate to the directory and call hickory schedule with YOUR_PROGRAM_NAME.py as the script argument:
```
hickory schedule src.py --every=10th@9:00am
```
### `--every` Examples

| Repeat                                                  |                          |
| ------------------------------------------------------- | ------------------------ |
| Every ten minutes                                       | `--every=10minutes`      |
| Every day at 10:10 AM                                   | `--every=@10:10`         |
| Every Monday at 10:10 AM                                | `--every=monday@10:10am` |
| Every 10th day of the month at 10:10 AM                 | `--every=10th@10:10am`   |
| Every last day of the month at 10:10 AM                 | `--every=eom@10:10am`    |
| Every 10th and last day of the month at 10 AM and 10 PM | `--every=10,eom@10,10pm` |



### `--every` Table

| Interval         |                                               |
| ---------------- | --------------------------------------------- |
| 10 seconds       | `10`, `10s`, `10sec`, `10secs`, `10seconds`   |
| 10 minutes       | `10m`, `10min`, `10mins`, `10minutes`         |
| 10 hours         | `10h`, `10hr`, `10hrs`, `10hours`             |
| **Time**         |                                               |
| 10:00 AM         | `@10`, `@10am`                                |
| 10:00 PM         | `@22`, `@10pm`                                |
| 10:10 AM         | `@10:10`, `@10:10am`                          |
| 10:10 PM         | `@22:10`, `@10:10pm`                          |
| **Weekday**      |                                               |
| Monday           | `m@`, `mon@`, `monday@`                       |
| Tuesday          | `t@`, `tue@`, `tues@`, `tuesday@`             |
| Wednesday        | `w@`, `wed@`, `weds@`, `wednesday@`           |
| Thursday         | `th@`, `thu@`, `thur@`, `thurs@`, `thursday@` |
| Friday           | `f@`, `fri@`, `friday@`                       |
| Saturday         | `s@`, `sat@`, `saturday@`                     |
| Sunday           | `su@`, `sun@`, `sunday@`                      |
| **Calendar Day** |                                               |
| 1st              | `1@`, `1st@`                                  |
| 2nd              | `2@`, `2nd@`                                  |
| 3rd              | `3@`, `3rd@`                                  |
| 4th              | `4@`, `4th@`                                  |
| 15th             | `15@`, `15th@`                                |
| 31st             | `31@`, `31st@`                                |
| **Other Day**    |                                               |
| Every Day        | `day@`                                        |
| Every Weekday    | `weekday@`                                    |
| End of Month     | `eom@`                                        |

## Helpful Links
https://realpython.com/twitter-bot-python-tweepy/
