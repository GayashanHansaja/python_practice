text=input("> ")

message=text.split(" ")

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
    greeting = moods.get(word, word)
    print(greeting, end=" ")