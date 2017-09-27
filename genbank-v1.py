#Written by Roshan Noronha
#May 21, 2017

from bs4 import BeautifulSoup
import requests

#takes in a URL and uses requests to get data from genbank
def getPage(url):
	soup = BeautifulSoup(requests.get(url).text, "lxml")
	return soup.string
	

#array of accession numbers
acc_values = [["JF778997", "andorraMadriu"], ["JF779064", "austriaAchenkirch"], ["JF778998", "belgiumBryssel"], ["JF778877", "bulgariaVitosha"], ["JF779199", "englandDorset"], ["JF779239", "finlandHelsinki"], ["JF779172", "franceAzaysurcher"], ["DQ074380", "germanyBabenhausen"], ["JF779092", "italyArborio"], ["JF778996", "kyrgysstanIssykkul"], ["JF779024", "netherlandsUtrecht"], ["JF779217", "polandWarsaw"], ["JF778987", "romaniaVoslobeni"], ["JF778983", "russiaBorisovka"], ["JF778921", "swedenKrankesjon"], ["JF778997", "andorraMadiru"], ["JF779064", "austriaAchenkirch"], ["JF778993", "usaCambridge"], ["JF778892", "usaMaine"]]

#stores fasta sequences
fastas = [];

#part of the url. The accession number needs to be added to this
genbank_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="

for i,j in acc_values:
	
	#adds the accession number to the url
	url = genbank_url + i + "&rettype=fasta&retmode=text"

	#tries to connect and outputs and exception if not successful
	try:
		#calls the getPage() function and stores the result
	    	response = str(getPage(url))
		
		#the first line is the header
		header = response.splitlines()[0]
		
		#header is modified to fasta format
		newFasta = ">" + j + " " + header[1:] + "\n" + "".join(response.splitlines()[1:])
		
		#modified fasta sequence is stored
		fastas.append(str(newFasta))
		
	#throw an exception in case connection to genbank is unsuccessful
	except requests.exceptions.Timeout:
	    print("The server didn't respond. Please, try again later.")


#write saved fasta sequences to a text file
writeFile = open("hicksFastaData.txt", 'w')
for i in fastas:
	writeFile.write(i + "\n\n")

writeFile.close()


