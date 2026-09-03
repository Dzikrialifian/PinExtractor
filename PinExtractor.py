# Extract secret codes from poems based on the length of words in each line
def pin_extractor(poems):
    # Initialize an empty list to store the secret codes
    secret_codes = []

    # Iterate through each poem in the list of poems
    for poem in poems:
        secret_code = ""

        # Split the poem into lines
        lines = poem.split("\n")

        # Iterate through each line and its index
        for line_index, line in enumerate(lines):
            # Split the line into words and check if the line has enough words to extract the length of the word at the current index
            words = line.split()
            if len (words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        
        # Append the constructed secret code for the current poem to the list of secret codes
        secret_codes.append(secret_code)
    return secret_codes

poem = """Lorem Ipsum is simply dummy text
of the printing and 
typesetting industry."""
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))