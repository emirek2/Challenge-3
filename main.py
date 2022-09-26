# fork this challenge to your own repl
#share this challenge with another person in the room.

#Day 3 Python Challenge

# The task is as follows: You are going to create a program that first asks the user to enter text. It can be any text, an entire article, a paragraph, a sentence, a poem, whatever you want. Then the program will ask the user to enter three random letters. From that moment on, our code is going to process that information and result in five different types of analysis:

# 1. How many times each of those letters they have chosen appears. To achieve this, I advise you to store those letters in a list, and then use a method of strings that allows you to count how many times a substring appears within the string. One thing to keep in mind is that when searching for letters, there can be upper and lower case and this will affect the result. So, to make sure that absolutely all letters are counted, you should pass both the original text and the letters to be searched to lowercase.

# 2. How many words are in the whole text? To achieve this part, remember that there is a string method that allows us to transform it into a list. And then there is a function that allows us to find out the length of a list.

# 3. What are the first and last letters of the text? Here, we will clearly use indexing.

# 4. The system will show us how the text would look like if we inverted the order of the words. Is there any method that allows us to invert the order of a list? And another one that allows us to join these elements with spaces in between?

# 5. The system will tell us if the word “python” is inside the text. This part can be a bit complicated to imagine, but I'll give you a hint: you can use Booleans to make your enquiry and a dictionary to find ways to express your answer.

# make 
ask_user=input("Input text:")
letter10=input("Select a letter:")
letter20=input("Select a letter:")
letter30=input("Select a letter:")



letter1=letter10.lower()
letter2=letter20.lower()
letter3=letter30.lower()
#step 1
list1=[str(letter1), str(letter2), str(letter3)]

text=str(ask_user)
list2=text.split()



# print(list1)
# print(list2)

text2=text.lower()

print("Letter 1 appears " +str(text2.count(letter1))+ " times.")
print("Letter 2 appears " +str(text2.count(letter2))+ " times.")
print("Letter 3 appears " +str(text2.count(letter3))+ " times.")


# Step 2
print('The length of the text is '+ str(len(list2)) + ' words.')


# Step 3
last_char = text2[-1]
print('Last character : ', last_char)
first_char = text2[0]
print('First character : ', first_char)

# Step 4
list2.reverse()
print(' '.join(list2))



# Step5
word = 'python'

if word in text2:
    print('Word found.')

if word not in text2:
  print("Word not found.")