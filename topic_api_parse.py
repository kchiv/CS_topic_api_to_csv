import csv
import json
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

f = csv.writer(open("topicAPI2.csv", "wb+"))
f.writerow(["active", "name", "popularity", "description", "pic", "subject_id", "subject_category", "date_created", "searchablename", "isbn13", "publisherID", "ID"])

x = 1

while x < 280:
	uri = 'api URL' % x
	x = x + 1
	response = requests.get(uri)
	if response.status_code == 200:
		data = response.json()
		for topics in data:
			f.writerow([topics["active"],
						topics["name"],
						topics["popularity"],
						topics["description"],
						topics["pic"],
						topics["subjectId"],
						topics["subjectCategory"],
						topics["dateCreated"],
						topics["searchableName"],
						topics["isbn13"],
						topics["publisherId"],
						topics["id"]])
			print([topics["active"],
						topics["name"],
						topics["popularity"],
						topics["description"],
						topics["pic"],
						topics["subjectId"],
						topics["subjectCategory"],
						topics["dateCreated"],
						topics["searchableName"],
						topics["isbn13"],
						topics["publisherId"],
						topics["id"]])
	else:
		print "none " + uri