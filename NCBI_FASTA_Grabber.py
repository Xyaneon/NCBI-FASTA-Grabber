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

accession_number = raw_input("Please enter your accession number: ")
while True:
    ncbi_database = raw_input("Which database should be searched (protein or nucleotide)?: ")
    if ncbi_database in ["protein", "nucleotide"]:
         break;
    else:
        print "Sorry, your input was not understood. Try again."

search_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
search_url += "esummary.fcgi?db=" + ncbi_database
search_url += "&id=" + accession_number

search_xml = urllib.urlopen(search_url).read()

print search_xml
