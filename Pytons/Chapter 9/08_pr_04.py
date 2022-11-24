def founder(text):
    f = open("poem.txt","r")
    Data= f.read()
    f.close() 
    # print(Data)
    # print(text in Data.lower())
    if text in Data.lower():
        Data = Data.replace(text,"####")
        f = open("Poem.txt", "w")
        f.write(Data)



founder("donkey")