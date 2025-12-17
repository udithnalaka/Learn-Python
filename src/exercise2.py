# write a method to find the most frequent character in a given sentence.

def most_frequent_char(s):
    print("Input string:", s)
    formatted_str = s.strip().replace(" ", "").lower()
    print("All charaters in the sentence:", formatted_str)

    char_dict = {}
    for char in formatted_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    print("Characters with occurences:", char_dict)

    # option 1
    max_char_count = max(char_dict, key=char_dict.get)
    print("OPTION 1:The most frequent character is:", max_char_count)

    # option 2
    result = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    print("OPTION 2: The most frequent character is:", result[0])


sentence = "This is a common interview question."
sentence_1 = "UDITHHHHHhhhhhhhhhhh"
sentence_2 = "My name is Udith Snageeth Nonis bro. I am from Sri Lanka. I love programming. Programming is fun."

most_frequent_char(sentence_2)
