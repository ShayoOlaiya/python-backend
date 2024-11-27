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
def clean_text(comment):
    clean_text = ""  # Sets clean text to a string
    for char in comment:  # Looping through the characters in comments
        if char.isalpha() or char.isspace():  # Checking if characters are letters
            clean_text += char.lower()
        else:
            clean_text += ' '# Converting the characters to lowercase, while adding clean text to characters

    return clean_text.strip()  # Strips unnecessary whitespaces
    
def make_keyword_dict(keyword_file_name):
    EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']  # Defines emotions
    emotion_dict = {}  # Initializes the first dictionary (keywords)

    try:
        with open(keyword_file_name, "r") as open_file:  # Opens file, without manually needing to close the file
            for line in open_file:
                section = line.strip().split("\t")  # Creates sections
                keyword = section[0]  # Assigning "keyword" to the first section
                emotion_val = {}  # Initializes an empty dictionary
                for i in range(len(EMOTIONS)):
                    emotion_val[EMOTIONS[i]] = int(section[i + 1])
                emotion_dict[keyword] = emotion_val  # Adds nested dictionary to the first dictionary
    except Exception as e: # Exceptions
        print(e)
    return emotion_dict # Returns function

def classify_comment_emotion(comment, keywords):
    clean_comment = clean_text(comment)  # Calling previous function to clean text
    words = clean_comment.split()  # "Cleans" words  by creating a list
    total_emotion = {  # Creating a dictionary to count its emotions
        "anger": 0,
        "joy": 0,
        "fear": 0,
        "trust": 0,
        "sadness": 0,
        "anticipation": 0
    }
    for word in words:
        if word in keywords:  # Check if the word exists in the keywords dictionary
            for emotion in keywords[word]:  # Iterate through emotions for the word
                total_emotion[emotion] += keywords[word][emotion]  # Increment by the corresponding emotion value
    return max(total_emotion, key=total_emotion.get)  # Returns the emotion with the highest score

def make_comments_list(filter_country, comments_file_name):
    comments = []  # Initializes to empty list
    with open(comments_file_name, "r") as open_file:  # Opens file securely
        for line in open_file:
            section = line.strip().split(",")  # Split the line into sections
            comment_id = int(section[0])  # Cast to integer after stripping
            username = section[1]  # Strip and convert to lowercase
            country = section[2].lower()  # Strip and convert to lowercase
            comment_text = section[3].strip()  # Strip the comment text

            comment_dict = {  # Creates a dictionary for each element
                "comment_id": comment_id,
                "username": username,
                "country": country,
                "text": comment_text
            }
            if filter_country.lower() == "all" or filter_country.lower() == country:  # Filters by country
                comments.append(comment_dict)  # Adds the comment to the list

    return comments

def make_report(comment_list, keywords, report_filename):
    # Initialize total emotion counts
    total_emotion = {
        "anger": 0,
        "joy": 0,
        "fear": 0,
        "trust": 0,
        "sadness": 0,
        "anticipation": 0
    }

    # Loop through comment_list to calculate emotions
    for comment in comment_list:
        comment_emotion = classify_comment_emotion(comment['text'], keywords)  # Add emotion to comment dictionary
        total_emotion[comment_emotion] += 1

    total_comments = sum(total_emotion.values())  # Calculate total number of comments

    # Determine the most common emotion
    order = ["anger", "joy", "fear", "trust", "sadness", "anticipation"]
    max_emotion = None
    max_count = -1

    for emotion in total_emotion:
        count = total_emotion[emotion]
        if count > max_count or (count == max_count and order.index(emotion) < order.index(max_emotion)):
            max_emotion = emotion
            max_count = count


    with open(report_filename, "w") as report_file:  # Securely open file for writing
        report_file.write(f"Most Common Emotion: {max_emotion}\n")
        report_file.write("Emotion Totals:\n")
        for emotion in order:  # Ensures the emotions are written in the correct order
            count = total_emotion[emotion]
            percentage = (count / total_comments) * 100 if total_comments > 0 else 0
            report_file.write(f"{emotion}: {count} ({percentage:.2f}%)\n") # displays emotion and the percentage rounded to 2 decimal places
     # checks if there are no comments, then raises an error
    if len(comment_list) == 0:
        raise RuntimeError("No comments in dataset!")


    return max_emotion
