def count_words(string):
    number_of_words = string.split()
    return len(number_of_words)

def count_characters(string):
    lower_string = string.lower()

    alphabet_dict = {'a' : 0, 'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,'g' : 0,
    'h' : 0,'i' : 0,'j' : 0,'k' : 0,'l' : 0,'m' : 0,'n' : 0,'o' : 0,
    'p' : 0,'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,'v' : 0,'w' : 0,
    'x' : 0,'y' : 0,'z' : 0}

    for i in range(0, len(string)):
        if lower_string[i] in alphabet_dict:
            alphabet_dict[lower_string[i]] += 1
            
    return alphabet_dict

#def sort_on(dict):
    #return dict[num]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    alphabet_dict = {}
    number_of_words = count_words(file_contents)
    alphabet_dict.update(count_characters(file_contents))
    #sorted_dict = [alphabet_dict]
    #sorted_dict.sort(reverse=True, key=sort_on)


    print("--- Begin report of frakenstein.txt ---")
    print(f"There are {number_of_words} words in the book.")

    for item in alphabet_dict:
        print(f"{item} appears a total number of {alphabet_dict[item]} times.")

    print("--- end report ---")


main()