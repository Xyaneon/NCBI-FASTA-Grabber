# This file is part of NCBI-FASTA-Grabber.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# NCBI-FASTA-Grabber is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# NCBI-FASTA-Grabber is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with NCBI-FASTA-Grabber. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 9/17/2014

import urllib
import xml.etree.ElementTree as elementtree
import pyperclip

eutils_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def answer(question):
    '''Returns an answer to a question.'''
    return raw_input(question).lower()

def show_invalid_input_message():
    '''Print an error message for invalid input.'''
    print "Sorry, your input was not understood. Try again."

def get_from_url(url):
    '''Gets input from a given URL to open.'''
    try:
        return urllib.urlopen(url).read()
    except IOError:
        print "Error: Could not access NCBI. Check your Internet connection."
        exit(1)

def construct_search_url(database, accession_number):
    '''Creates the search URL string.'''
    url = eutils_url + "esearch.fcgi?db=" + database
    url += "&term=" + accession_number + "[accn]"
    return url

def construct_summary_url(database, results_id):
    '''Creates the summary URL string.'''
    url = eutils_url + "esummary.fcgi?db=" + database
    url += "&id=" + results_id
    return url

def construct_fetch_url(database, results_id):
    '''Creates the fetch URL string.'''
    url = eutils_url + "efetch.fcgi?db=" + database
    url += "&id=" + results_id
    url += "&rettype=fasta&retmode=text"
    return url

def print_summary(title, caption, extra):
    '''Prints the formatted summary information.'''
    print
    print "CAPTION: ", caption
    print "TITLE:   ", title
    print "EXTRA:   ", extra

def ask_for_database():
    '''Ask the user which database they want to use and return it.'''
    while True:
        question = "Which database should be searched (p/protein or n/nucleotide)?: "
        database = answer(question)
        if database in ["protein", "nucleotide", "p", "n"]:
            if database == "p":
                database = "protein"
            if database == "n":
                database = "nucleotide"
            break
        else:
            show_invalid_input_message()
    return database

def ask_yes_no(question, no_string):
    '''Exit this function only when the user answers yes to a yes/no
    question. Also, show a string and quit the program if the answer is no.'''
    while True:
        confirmation = answer(question + " (Y/n)?: ")
        if confirmation in ["yes", "no", "y", "n", ""]:
            if confirmation in ["yes", "y", ""]:
                return
            elif confirmation in ["no", "n"]:
                print no_string
                exit(0)
        else:
            show_invalid_input_message()


# Start of program


accession_number = raw_input("Please enter your accession number: ")
database = ask_for_database()

search_xml = get_from_url(construct_search_url(database, accession_number))
root = elementtree.fromstring(search_xml)

# Check if there were any matches
results_count = 0
for count in root.iter("Count"):
    results_count = int(count.text)

results_id = ""
if results_count > 0:
    for id_tag in root.iter("Id"):
        results_id = id_tag.text
        break
    if results_count != 1:
        print results_count + " results found. Showing only the first."
else:
    print "No results found."
    exit(2)

# Print summary for result. Need Caption, Title, and Extra
summary_xml = get_from_url(construct_summary_url(database, results_id))
root = elementtree.fromstring(summary_xml)

caption = "n/a"
title = "n/a"
extra = "n/a"

for item in root.iter("Item"):
    if item.attrib["Name"] == "Caption":
        caption = item.text
    if item.attrib["Name"] == "Title":
        title = item.text
    if item.attrib["Name"] == "Extra":
        extra = item.text

print_summary(caption, title, extra)

ask_yes_no("\nIs this the result you were looking for", "Sorry about that.")

fasta = get_from_url(construct_fetch_url(database, results_id))
print "\nFASTA sequence:\n"
print fasta

ask_yes_no("Copy to clipboard", "Alright then. Bye!")
pyperclip.copy(fasta)
print "FASTA sequence copied to clipboard."

exit()

# Sample output:
#
#christopher@ArcticThunder:~/NCBI-FASTA-Grabber$ python NCBI_FASTA_Grabber.py
#Gtk-Message: Failed to load module "canberra-gtk-module"
#Please enter your accession number: NM_000518
#Which database should be searched (protein or nucleotide)?: nucleotide
#
#CAPTION:  Homo sapiens hemoglobin, beta (HBB), mRNA
#TITLE:    NM_000518
#EXTRA:    gi|28302128|ref|NM_000518.4|[28302128]
#
#Is this the result you were looking for (yes or no)?: yes
#
#FASTA sequence:
#
#>gi|28302128|ref|NM_000518.4| Homo sapiens hemoglobin, beta (HBB), mRNA
#ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA
#GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC
#AGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG
#CTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC
#TCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT
#CCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA
#CCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA
#CTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT
#GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC
#
#
#Copy to clipboard (yes or no)?: yes
#FASTA sequence copied to clipboard.
