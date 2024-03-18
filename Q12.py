def reverse_sen(user_input):
     if not user_input:
        return "Input sentence is empty"
     words = user_input.split()
     for i in range(len(words)): 
        words[i] = words[i][::-1] 
     reversed_sentence = ' '.join(reversed(words))
     return reversed_sentence

user_input=input("Enter a sentence to be reversed:")
output=reverse_sen(user_input)
print("Input sentence:", user_input)
print("Reversed sentence:", output)