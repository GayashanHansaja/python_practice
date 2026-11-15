def emoji_converter(input):
    message=input.split(" ")

    moods={
        ":)" : "😊",
        ":(" : "😢",
        ":D" : "😄",
        ":P" : "😛"
    }

    greeting=""
    # for word in message:
    #     if word in moods:
    #         word=moods.get(word)
    #     greeting+=word+" "
    # print(greeting, end=" ")
        
    for word in message:
        greeting += moods.get(word, word)
    return greeting

print("hi we are going to convert your text into emojis")
text=input("> ")
print(emoji_converter(text))

# parameter -> place holder for piece of information that is passed into a function when it is called. It is used to define the input that the function expects to receive.
# argument -> actual value that is passed into a function when it is called. It is the real data that is provided to the function for processing.

# def name_function(first_name, last_name):
#     print("Hello " + first_name + " " + last_name)

# name_function(first_name="John", last_name="Doe")