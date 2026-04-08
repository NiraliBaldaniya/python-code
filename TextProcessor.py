def remove_duplicate(text):
   result = ""
   for char in text:
       if char not in result:
           result += char
   return result 

def remove_vowels(text):      
    vowels="aeiouAEIOU"
    end = ""
    for x in text:
        if x not in vowels:
            end += x
    return end

def toggle_case(text):
    return text.swapcase()

def title_case(text):
    return text.title()

def sentence_case(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]

def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

text = input("enter text: ")
        
while True:
   
    print("--------------------------------------")
    print("1. toggle case ")
    print("2. title case ")
    print("3. sentence case ")
    print("4. remove duplicate ")
    print("5. remove vowels ")
    print("6. reverse text ")
    print("7. count word & character ")
    print("8. exit ")
    print("--------------------------------------")

    choice = int(input("enter your choice(1-8) : "))
    
    if choice == 1:
        print("toggle case: ",toggle_case(text))
    elif choice == 2:
        print("title case: ",title_case(text))
    elif choice == 3:
        print("sentence case: ",sentence_case(text))
    elif choice == 4:
        print("remove duplicate ",remove_duplicate(text))
    elif choice == 5:
        print("remove vowels: ",remove_vowels(text))
    elif choice == 6:
        print("Reversed text:", reverse_text(text))
    elif choice == 7:
        print("Word count:", word_count(text))
        print("character count: ",char_count(text))
    elif choice == 8:
        print("exit program...")
        break
    else:
        print("invalid choice")
