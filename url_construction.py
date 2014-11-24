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

eutils_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

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
