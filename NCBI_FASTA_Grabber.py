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
# Last modified: 9/16/2014

import urllib
import xml.etree.ElementTree as elementtree

accession_number = raw_input("Please enter your accession number: ")
while True:
    ncbi_database = raw_input("Which database should be searched (protein or nucleotide)?: ")
    if ncbi_database in ["protein", "nucleotide"]:
         break
    else:
        print "Sorry, your input was not understood. Try again."

eutils_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

search_url = eutils_url + "esearch.fcgi?db=" + ncbi_database
search_url += "&term=" + accession_number + "[accn]"

search_xml = urllib.urlopen(search_url).read()
root = elementtree.fromstring(search_xml)

# Check if there were any matches
results_count = 0
for count in root.iter("Count"):
    results_count = int(count.text)

results_id = ""
if results_count > 0:
    for id_tag in root.iter("Id"):
        results_id = id_tag.text
        #print results_id
        break
else:
    print "No results found."
    exit()

# Print summary for result. Need Caption, Title, and Extra
summary_url = eutils_url + "esummary.fcgi?db=" + ncbi_database
summary_url += "&id=" + results_id

summary_xml = urllib.urlopen(summary_url).read()
#print summary_xml
root = elementtree.fromstring(summary_xml)

caption_text = ""
title_text = ""
extra_text = ""

for item in root.iter("Item"):
    if item.attrib["Name"] == "Caption":
        caption_text = item.text
    if item.attrib["Name"] == "Title":
        title_text = item.text
    if item.attrib["Name"] == "Extra":
        extra_text = item.text

print
print "CAPTION: ", caption_text
print "TITLE: ", title_text
print "EXTRA: ", extra_text

while True:
    confirmation = raw_input("\nIs this the result you were looking for (yes or no)?: ")
    if confirmation in ["yes", "no"]:
        if confirmation == "yes":
            print "TODO: get FASTA sequence"
        else:
            print "Sorry about that."
            exit()
        break

exit()
