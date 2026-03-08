import os

def open_files():
    file_names = os.listdir("data/raw")
    documents = []

    for file in file_names:
        file_path = os.path.join("data/raw" , file) 
        with open(file_path , "r") as f: # r = read mode
            text= f.read() 
        doc = {
            "source" : file,
            "text" : text
    }
        documents.append(doc)
    return documents


        

