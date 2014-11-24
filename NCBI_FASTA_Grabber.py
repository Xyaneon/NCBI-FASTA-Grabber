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
# Last modified: 11/24/2014

import argparse
import urllib
import xml.etree.ElementTree as elementtree

import generate_output
import url_construction
import user_interaction

VERSION = "v1.2.0"
DESC = "NCBI-FASTA-Grabber " + VERSION + "\nFetches FASTA sequences from NCBI."

def get_from_url(url):
    '''Gets input from a given URL to open.'''
    try:
        return urllib.urlopen(url).read()
    except IOError:
        print "Error: Could not access NCBI. Check your Internet connection."
        exit(1)

#*****************************************************************************
# Start of main program
#*****************************************************************************

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=DESC
         )
yestoall_help = """answer yes to all questions and copy FASTA sequence to the
clipboard automatically, if available"""
db_group = parser.add_mutually_exclusive_group()
parser.add_argument("-a", "--accessionnumber",
                    help="specifies the accession number", type=str)
db_group.add_argument("-p", "--protein", help="search the protein database",
                      action="store_true")
db_group.add_argument("-n", "--nucleotide",
                      help="search the nucleotide database (default)",
                      action="store_true")
parser.add_argument("-y", "--yestoall", help=yestoall_help, action="store_true")
args = parser.parse_args()

accession_number = ""
database = ""
if args.accessionnumber:
    accession_number = args.accessionnumber
if args.protein:
    database = "protein"
else:
    database = "nucleotide"

if accession_number == "":
    accession_number = raw_input("Please enter your accession number: ")
if database == "":
    database = user_interaction.ask_for_database()

search_xml = get_from_url(url_construction.construct_search_url(database, accession_number))
root = elementtree.fromstring(search_xml)

# Check if there were any matches
results_count = 0
for count in root.iter("Count"):
    results_count = int(count.text)
    break

results_id = ""
if results_count > 0:
    for id_tag in root.iter("Id"):
        results_id = id_tag.text
        break
    if results_count > 1:
        print results_count, "results found. Showing only the first."
else:
    print "No results found."
    exit(2)

# Print summary for result. Need Caption, Title, and Extra
summary_xml = get_from_url(url_construction.construct_summary_url(database, results_id))
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

generate_output.print_summary(caption, title, extra)

if not args.yestoall:
    user_interaction.ask_yes_no("\nIs this the result you were looking for", "Sorry about that.")

fasta = get_from_url(url_construction.construct_fetch_url(database, results_id))

# Final sequence output
generate_output.print_fasta(fasta)
generate_output.ask_if_copy_to_clipboard(fasta, args.yestoall)

exit(1)
