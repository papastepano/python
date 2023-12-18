# Write your solution here
def prepare_words(filename: str):
    words = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            words.append(line)
    return words

def find_words(search_term: str):
    search_results = []
    words = prepare_words("words.txt")
    if "." in search_term:
        for word in words:
            if len(word) != len(search_term):
                continue
            match = True
            for i in range(len(word)):
                if word[i] != search_term[i] and search_term[i] != ".":
                    match = False
                    break
            if match:
                search_results.append(word)
    elif "*" in search_term:
        if search_term.startswith("*"):
            for word in words:
                if word.endswith(search_term.replace("*", "")):
                    search_results.append(word)
        elif search_term.endswith("*"):
            for word in words:
                if word.startswith(search_term.replace("*", "")):
                    search_results.append(word)
    else:
        for word in words:
            if word == search_term:
                search_results.append(word)
                
    return search_results
    
if __name__ == "__main__":
    print(find_words("*vokes"))

