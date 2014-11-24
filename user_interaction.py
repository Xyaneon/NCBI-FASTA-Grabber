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

def answer(question):
    '''Returns an answer to a question.'''
    return raw_input(question).lower()

def show_invalid_input_message():
    '''Print an error message for invalid input.'''
    print "Sorry, your input was not understood. Try again."

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
