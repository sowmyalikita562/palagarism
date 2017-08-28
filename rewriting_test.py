from synonyms import *
text=input().split()
text2=input().split()
print(text)
l2=synonyms.keys()
for word in text:
    #print(word)
    count=0
    count2=0
    if word in l2:
        #print(word)
        for word2 in text2:
            #print(word2)
            if word2 in synonyms.get(word):
                #print(synonyms.get(word))
                count+=1
                print(word,count)
            
    for k in synonyms.values():
        print(k)
        for i in k:
            print(i)
            if word in i:
                print(word)
                for word2 in text2:
                    if word2 in l2 or word2 in i:
                        print(word2)
                        print("l2",l2)
                        count+=1
                    print(word,count)
print(word,count)                        
               
"""for word2 in text2:
    #print(word)
    count2=0
    if word2 in l2:
        #print(word)
        for word1 in text:
            #print(word2)
            if word1 in synonyms.get(word2):
                #print(synonyms.get(word))
                count2+=1
                print(word2,count2)
            
    for k in synonyms.values():
        for i in k:
            if word2 in i:
                for word1 in text:
                    if word1 in l2 or word1 in i:
                        count2+=1
                    print(word2,count2)
print(word2,count2)   """



