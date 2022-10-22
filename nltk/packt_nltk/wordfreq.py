import sys

def wordfreq(my_string):

# Function to generate the frequency distrobution of the given text


    print(my_string)
    word_freq={}

    # tok for "token"

    for tok in my_string.split():
        if tok in word_freq:
            word_freq[tok]+=1

        else: 
            word_freq[tok]=1

        print(word_freq)

    def main():
        str="This is my first python program"
        wordfreq(str)

    if __name__== "__main__":
        main()
