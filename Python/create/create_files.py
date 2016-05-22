name = ["identifiers","variables","datatypes","io","operator"]
fileName = ["Description","Syntax","Example","Output"]

for i in range(0,5):
    for j in range(0,4):
        name1=name[i]
        name2=fileName[j]
        name3 = name1+name2+'.txt' 
        print(name3)
        open(name3,'w')
        
        

