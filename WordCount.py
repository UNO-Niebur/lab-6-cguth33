#WordCount.py
#Name: Carter Guthrie
#Date: 3/1/2025
#Assignment: Lab 6

def main():
    line_count = 0
    word_count = 0
    char_count = 0
    
    try:
        textFile = open("gettysburg.txt", 'r')
        
        for line in textFile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
            
        textFile.close()
        
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
        
    except FileNotFoundError:
        print("Error: gettysburg.txt not found.")

if __name__ == '__main__':
    main()