import os
#Rachel Gordon Project 1 
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv
import datetime

def getData(file):
	infile = open(file, "r")
	Data = csv.reader(infile)
	li_of_dicts = []
	counter = 0
	for row in Data:
		if counter == 0:
		    first = row[0]
		    last = row[1]
		    email = row[2]
		    year = row[3]
		    dob = row[4]
		else:
		    d = {}
		    d[first] = row[0]
		    d[last] = row[1]
		    d[email] = row[2]
		    d[year] = row[3]
		    d[dob] = row[4]
		    li_of_dicts.append(d)
		counter += 1
	infile.close()

	return li_of_dicts

def mySort(data,col):
	first_dic = sorted(data, key = lambda x: x[col])[0]
	full_name = first_dic['First'] + ' ' + first_dic["Last"]
	return full_name


def classSizes(data):
    class_dict = {}
    for d in data:
        class_stand = d["Class"]
        if class_stand in class_dict:
            class_dict[class_stand] += 1
        else:
            class_dict[class_stand] = 1
    sorted_classes = sorted(class_dict.items(), key = lambda x: x[1], reverse = True)
    return sorted_classes


def findMonth(a):
    month_dict = {}
    for d in a:
        birth_month = d['DOB'].split('/')[0]
        if birth_month in month_dict:
            month_dict[birth_month] += 1
        else:
            month_dict[birth_month] = 1
    sorted_months = sorted(month_dict, key = lambda x: month_dict[x], reverse = True)
    return int(sorted_months[0])


def mySortPrint(a,col,fileName):
	fi_list = []
	first_dic = sorted(a, key = lambda x: x[col])
	for i in first_dic:
		fi_list.append(i["First"] + ',' + i["Last"] + ',' + i["Email"] + '\n')
	outFile = open(fileName, "w")
	for x in fi_list:
		outFile.write(x)

def findAge(a):
	age_list = []
	count = 0
	year_today = (datetime.datetime.today().strftime('%m/%d/%Y'))
	for d in a:
		year = d["DOB"]
		date_today = year_today.split('/')
		birthday = year.split('/')
		age = int(date_today[2]) - int(birthday[2])
		if int(birthday[0]) >= int(date_today[0]):
			age = int(date_today[2]) - int(birthday[2]) - 1
		if int(birthday[0]) == int(date_today[0]) and int(birthday[1]) > int(date_today[1]):
			age = int(date_today[2]) - int(birthday[2]) - 1
		age_list.append(age)
	    
	total = 0
	for i in age_list:
		total += i
    
	avg = float(total / len(age_list))
	return round(avg)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
