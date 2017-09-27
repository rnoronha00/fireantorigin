#Written by Roshan Noronha
#September 21, 2017

from bs4 import BeautifulSoup
import requests
import csv

#takes in a URL and uses requests to get data from genbank
def getPage(url):
	soup = BeautifulSoup(requests.get(url).text, "lxml")
	return soup.string

#import csv file, read only
f = open("", "r")
reader = csv.reader(f)

#stores every row in the csv as an array
acc_info = [];
for row in reader:
        acc_info.append([row])

#stores the accession numbers and the unique identifier + city of each fire ant sample
acc_values = [];
for data in acc_info:
        acc_values.append([data[0], data[1] + "_" + data[2].split(",")[0]])

#stores fasta sequences from Genbank
fastas = [];
#part of the url. The accession number needs to be added to this
genbank_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="

for acc_num, identifier in acc_values:
	
	#adds the accession number to the url
	url = genbank_url + acc_num + "&rettype=fasta&retmode=text"

	#tries to connect and outputs and exception if not successful
	try:
		#calls the getPage() function and stores the result
	    	response = str(getPage(url))
		
		#the first line is the header
		header = response.splitlines()[0]
	
		#header is modified to fasta format
		newFasta = ">" + identifier + " " + header[1:] + "\n" + "".join(response.splitlines()[1:])
		
		#modified fasta sequence is stored
		fastas.append(str(newFasta))
		
	#throw an exception in case it breaks
	except requests.exceptions.Timeout:
	    print("The server didn't respond. Please, try again later.")


#write saved fasta sequences to a text file
writeFile = open("hicksFastaData.txt", 'w')
for i in fastas:
	writeFile.write(i + "\n\n")

writeFile.close()


