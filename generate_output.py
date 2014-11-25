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
# Last modified: 11/25/2014

import pyperclip

import user_interaction

def print_summary(title, caption, extra):
    '''Prints the formatted summary information.'''
    print
    print "CAPTION: ", caption
    print "TITLE:   ", title
    print "EXTRA:   ", extra

def print_fasta(fasta):
    '''Prints the FASTA sequence.'''
    print "\nFASTA sequence:\n"
    print fasta

def ask_if_copy_to_clipboard(fasta, auto_yes):
    '''Ask the user if the FASTA sequence should be copied to the clipboard,
    if we're not told to automatically do so.'''
    if not auto_yes:
        user_interaction.ask_yes_no("Copy to clipboard", "Alright then. Bye!")
    pyperclip.copy(fasta)
    print "FASTA sequence copied to clipboard."
