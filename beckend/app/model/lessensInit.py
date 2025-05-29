file_path = "rec/lesson2.txt"
lessons = [[]] 
for i in range(0,19):
    lessons.append([])
    
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split()
   
        
    for i in range(len(words)):
        lessons[i % 20].append(words[i])
        
        
        
        
        
        
        
for i in range(0,len(lessons)):
    with open(f'rec/lessons/lesson{i % 20}.txt','w') as f :
        for word in lessons[i]:
            f.write(word + '\n')
            
    
        
        
        
        
        
        
        
    
        