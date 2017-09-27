#lets write a Simple script 
#to get the 20 words and their frequency percentage 
#with highest frequency in an English Wikipedia article. 
#applications are recommender systems, chatbots and NLP, sentiment analysis,
#data visualization,
#market research

#Beautiful Soup is a Python library 
#for pulling data out of HTML and XML files.
from bs4 import BeautifulSoup
#Requests is one of the most downloaded 
#Python packages of all time, 
#pulling in over 7,000,000 downloads every month.
#HTTP library for pulling pushing and authenticating
import requests
#lets you do Regular expression operations
#special text string for describing a search pattern.
#find and replace
import re
#The operator module exports a 
#set of efficient functions 
#corresponding to the intrinsic operators of Python.
#comparison, addition, greater than less then
import operator
#parses json, formats it
import json
#The module provides just one function, 
#tabulate, which takes a list of lists or another 
#tabular data type as the first argument, 
#and outputs a nicely formatted plain-text table:
from tabulate import tabulate
#system calls, dealw with user arguments
import sys
#list of common stop words various languages like the
from stop_words import get_stop_words

def getPage(url):
	soup = BeautifulSoup(requests.get(url).text, "lxml")
	return soup.string
	

#list of accession numbers
acc_values = [["JF778997", "andorraMadriu"], ["JF779064", "austriaAchenkirch"], ["JF778998", "belgiumBryssel"], ["JF778877", "bulgariaVitosha"], ["JF779199", "englandDorset"], ["JF779239", "finlandHelsinki"], ["JF779172", "franceAzaysurcher"], ["DQ074380", "germanyBabenhausen"], ["JF779092", "italyArborio"], ["JF778996", "kyrgysstanIssykkul"], ["JF779024", "netherlandsUtrecht"], ["JF779217", "polandWarsaw"], ["JF778987", "romaniaVoslobeni"], ["JF778983", "russiaBorisovka"], ["JF778921", "swedenKrankesjon"], ["JF778997", "andorraMadiru"], ["JF779064", "austriaAchenkirch"], ["JF778993", "usaCambridge"], ["JF778892", "usaMaine"]]

#store fasta sequences
fastas = [];
#the url
genbank_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="

for i,j in acc_values:
	url = genbank_url + i + "&rettype=fasta&retmode=text"

	#try-except block. simple way to deal with exceptions 
	#great for HTTP requests
	try:
		#use requests to retrieve raw data from wiki API URL we just constructed
	    	response = str(getPage(url))
		
		#first line of fasta
		header = response.splitlines()[0]
	
		newFasta = ">" + j + " " + header[1:] + "\n" + "".join(response.splitlines()[1:])
		
		fastas.append(str(newFasta))
		
	#throw an exception in case it breaks
	except requests.exceptions.Timeout:
	    print("The server didn't respond. Please, try again later.")


#write to file
writeFile = open("hicksFastaData.txt", 'w')
for i in fastas:
	writeFile.write(i + "\n\n")

writeFile.close()


