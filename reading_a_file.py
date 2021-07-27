text_file = open('welcome.txt')
text_data = text_file.read()
print(text_data)
text_file.close()

#or

with open('welcome.txt') as welcome:
    lines = welcome.readlines()
    print(lines)
    
    
#or iterating through lines

with open('welcome.txt') as welcome:
    for line in welcome.readlines():
        print(line)
        
        
        