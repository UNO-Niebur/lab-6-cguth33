#WordIndex.py
#Name: Carter Guthrie
#Date: 3/1/2025
#Assignment: Lab 6

def main():
    try:
        textFile = open("fish.txt", 'r')
        words = {} # Dictionary: word -> [line numbers]
        line_num = 0

        for line in textFile:
            line_num += 1
            # Clean punctuation and split into words
            cleaned_line = line.replace(",", "").replace(".", "").replace("!", "")
            row_words = cleaned_line.split()
            
            for word in row_words:
                word = word.lower()
                if word not in words:
                    words[word] = [line_num]
                else:
                    if line_num not in words[word]: # Avoid duplicate line numbers
                        words[word].append(line_num)
        
        textFile.close()

        # Print the index alphabetically
        for key in sorted(words.keys()):
            print(f"{key}: {words[key]}")
            
    except FileNotFoundError:
        print("Error: fish.txt not found.")

if __name__ == '__main__':
    main()