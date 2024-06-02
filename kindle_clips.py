import pandas as pd

def kindle_clip(clips_filepath):
    """
    Returns a random clip from the kindle clips

    Args:
        clips_filepath (str): filepath to kindle clippings file

    Returns:
        daiy email clip (str): kindle_clip

    """
    with open(clips_filepath, 'r', encoding='utf-8') as file:
        kindle_text = file.read()
    file.close()
    # Splits the text strings into a list of sections
    sections = kindle_text.split('==========\n')

    titles = []
    quotes = []

    # loops through all the sections
    for section in sections:
        # Removes any leading and trailing whitespaces
        if section.strip():
            # Splits the text strings into a list by new lines
            lines = section.split('\n')
            # Separates the title, detail and quote by taking specific elements
            title = lines[0]
            quote = lines[3]
            # Appends the elements to lists
            titles.append(title)
            quotes.append(quote)

    # Sets the name of dataframe columns
    kindle_df = pd.DataFrame({
        'Title': titles,
        'Quote': quotes
    })

    # returns a new dataframe where the data type of
    # all columns has been set to strings
    kindle_df = kindle_df.astype(str)
    # randomly picks a row from the dataframe
    kindle_clip = kindle_df.sample(n=1)

    return kindle_clip


clips_filepath = input('Filepath: ')
daily_kindle_clip = kindle_clip(clips_filepath)
