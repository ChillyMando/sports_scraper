import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import datetime

# TO-DO Simplify parsing functions


def moneyline_parse():
    for item_index, item in enumerate(parse_list):
        if item == 'Money Line':
            if parse_list[item_index + 3] != 'N/A':
                odds = []
                odds.append(parse_list[item_index + 3])
                odds.append(float(parse_list[item_index + 4]))
                odds.append(parse_list[item_index + 5])
                odds.append(float(parse_list[item_index + 6]))
                odds.append(1/odds[1] + 1/odds[3] - 1)
                if parse_list[item_index + 7] != 'N/A' and parse_list[item_index + 13] != 'N/A':
                    try:
                        odds.append(parse_list[item_index + 19])
                    except IndexError:
                        pass
                moneyline.append(odds)


def spread_parse():
    for item_index, item in enumerate(parse_list):
        if item == 'Spread':
            if parse_list[item_index + 2] == 'N/A':
                if parse_list[item_index + 4] != 'N/A':
                    odds = []
                    odds.append(parse_list[item_index + 4])
                    odds.append(float(parse_list[item_index + 5]))
                    odds.append(float(parse_list[item_index + 6]))
                    odds.append(parse_list[item_index + 7])
                    odds.append(float(parse_list[item_index + 8]))
                    odds.append(float(parse_list[item_index + 9]))
                    odds.append(1/odds[2] + 1/odds[5] - 1)
                    if parse_list[item_index + 10] != 'N/A':
                        try:
                            odds.append(parse_list[item_index + 16])
                        except IndexError:
                            pass
                    else:
                        try:
                            odds.append(parse_list[item_index + 13])
                        except IndexError:
                            pass
                    spread.append(odds)
            elif parse_list[item_index + 6] != 'N/A':
                odds = []
                odds.append(parse_list[item_index + 6])
                odds.append(float(parse_list[item_index + 7]))
                odds.append(float(parse_list[item_index + 8]))
                odds.append(parse_list[item_index + 9])
                odds.append(float(parse_list[item_index + 10]))
                odds.append(float(parse_list[item_index + 11]))
                odds.append(1/odds[2] + 1/odds[5] - 1)
                if parse_list[item_index + 12] != 'N/A':
                    try:
                        odds.append(parse_list[item_index + 18])
                    except IndexError:
                        pass
                else:
                    try:
                        odds.append(parse_list[item_index + 14])
                    except IndexError:
                        pass
                spread.append(odds)


def total_parse():
    for item_index, item in enumerate(parse_list):
        if item == 'Total':
            if parse_list[item_index + 1] == 'N/A':
                if parse_list[item_index + 3] == 'N/A':
                    if parse_list[item_index + 5] != 'N/A':
                        odds = []
                        odds.append(parse_list[item_index - 4])
                        odds.append(parse_list[item_index - 3])
                        odds.append(float(parse_list[item_index + 6]))
                        odds.append(float(parse_list[item_index + 7]))
                        odds.append(float(parse_list[item_index + 10]))
                        odds.append(1/odds[3] + 1/odds[4] - 1)
                        odds.append(parse_list[item_index + 11])
                        total.append(odds)
                elif parse_list[item_index + 9] != 'N/A':
                    odds = []
                    odds.append(parse_list[item_index - 4])
                    odds.append(parse_list[item_index - 3])
                    odds.append(float(parse_list[item_index + 10]))
                    odds.append(float(parse_list[item_index + 11]))
                    odds.append(float(parse_list[item_index + 14]))
                    odds.append(1/odds[3] + 1/odds[4] - 1)
                    odds.append(parse_list[item_index + 15])
                    total.append(odds)
            elif parse_list[item_index + 5] == 'N/A':
                if parse_list[item_index + 7] != 'N/A':
                    odds = []
                    odds.append(parse_list[item_index - 4])
                    odds.append(parse_list[item_index - 3])
                    odds.append(float(parse_list[item_index + 8]))
                    odds.append(float(parse_list[item_index + 9]))
                    odds.append(float(parse_list[item_index + 12]))
                    odds.append(1/odds[3] + 1/odds[4] - 1)
                    odds.append(parse_list[item_index + 13])
                    total.append(odds)
            elif parse_list[item_index + 11] != 'N/A':
                odds = []
                odds.append(parse_list[item_index - 4])
                odds.append(parse_list[item_index - 3])
                odds.append(float(parse_list[item_index + 12]))
                odds.append(float(parse_list[item_index + 13]))
                odds.append(float(parse_list[item_index + 16]))
                odds.append(1/odds[3] + 1/odds[4] - 1)
                odds.append(parse_list[item_index + 17])
                total.append(odds)


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

os.environ['PATH'] += r'C:/Users/colby/OneDrive/Coding/Selenium Drivers'
driver = webdriver.Chrome(options=options)

driver.get('https://www.playnow.com/mb/sports/sport/3/football/matches')

time.sleep(3)

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN*5)
show_more = driver.find_elements(
    By.XPATH, '//button[text()="Show More Events"]')
for element in show_more:
    element.send_keys(Keys.RETURN)

text = body.text.split('\n')
parse_list = []
for line in text:
    parse_list.append(line)

driver.quit()

del (parse_list[0:(parse_list.index('Money Line') - 3)])
del (parse_list[parse_list.index('Outrights and Futures')-1:])

moneyline = [['Money Line'], ['away', 'odds', 'home', 'odds', 'vig', 'date']]
moneyline_parse()

spread = [['Spread'], ['away', 'spread',
                       'odds', 'home', 'spread', 'odds', 'date']]
spread_parse()

total = [['Total'], ['away', 'home',
                     'score' 'over_odds', 'under_odds', 'vig', 'date']]
total_parse()

print('Money Line: \n', moneyline, '\n')
print('Spread: \n', spread, '\n')
print('Totals: \n', total, '\n')

current_datetime = datetime.datetime.now()
current_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

csv_file_path = f"output/{current_datetime}.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in moneyline:
        writer.writerow(row)

    for row in spread:
        writer.writerow(row)

    for row in total:
        writer.writerow(row)
