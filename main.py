"""
******************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Shayo Olaiya
Student ID: oolaiya2
File created: November 2024
******************************
This file is classifying YouTube comments based on one of the following emotions anger, joy, fear, trust,
sadness, or anticipation.
"""

import os.path
from emotions import *

VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',         # List of valid countries
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']


def ask_user_for_input():

    # Ask for the keyword file and check its extension
    keyword_file = input('Input keyword file (ending in .tsv): ').strip()     
    if not keyword_file.endswith('.tsv'):
        raise ValueError("Error: Keyword file does not end in .tsv!\n")
    if not os.path.exists(keyword_file):
        raise IOError(f"Error: {keyword_file} does not exist!\n")

    # Ask for the comments file and check its extension
    comments_file = input('Input comment file (ending in .csv): ').strip()
    if not comments_file.endswith('.csv'):
        raise ValueError("Error: Comments file does not end in .csv!\n")
    if not os.path.exists(comments_file):
        raise IOError(f"Error: {comments_file} does not exist!\n")

    # Ask for the country to analyze
    country = input('Input a country to analyze (or "all" for all countries): ').strip().lower()
    if country != "all" and country not in VALID_COUNTRIES:
        raise IOError(f"Error: {country} is not a valid country to filter by!\n")

    # Ask for the report file and check its extension
    report_file = input('Input the name of the report file (ending in .txt): ').strip()
    if not report_file.endswith('.txt'):
        raise ValueError("Error: Report file does not end in .txt!\n")


    # If everything is valid, break out of the loop
    return keyword_file, comments_file, country, report_file

# Display the error and continue the loop for re-input




def main():
    try:
        # Step 1: Get inputs from the user
        keyword_file, comments_file, country, report_file = ask_user_for_input()

        # Step 2: Create a keyword dictionary from the keyword file
        keywords = make_keyword_dict(keyword_file)

        # Step 3: Filter comments based on the country
        comment_list = make_comments_list(country, comments_file)

        # Step 4: Generate the report using the filtered comments and keywords
        if not comment_list:  # Check if the comment list is empty
            raise ValueError("No comments in dataset!")
        max_emotion = make_report(comment_list, keywords, report_file)

        with open(report_file, "r") as report:
            print(report.read())  # Print the report contents

    except (IOError, ValueError, RuntimeError) as e: # List of
        print(e)



if __name__ == "__main__":
    main()

