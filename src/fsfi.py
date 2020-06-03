import time
file = open(r"C:\Users\Shashank\OneDrive\Desktop\cb1.txt",errors='ignore') 
Counter = 0
Content = file.read() 
CoList = Content.split("\n")   
for i in CoList: 
    if i: 
        Counter += 1          
print("Total number of lines:",Counter) 

print("INDEXING STARTED")
c=0
start=time.time()
with open(r"C:\Users\Shashank\OneDrive\Desktop\cb1.txt") as pack:
    with open(r"C:\Users\Shashank\OneDrive\Desktop\index2.txt","w") as index:
        count=0
        f=pack.read()
        s=f.replace("\n","")
        for line in s.split(" "):
            stri=line[:]
            index.write(stri+" ")
            c=str(count)
            index.write(c+"\n")
            count=len(line)+count
end=time.time()
print("Indexing Completed!! in",end-start,"sec")
 
with open(r"C:\Users\Shashank\OneDrive\Desktop\cb1.txt") as main:
    with open(r"C:\Users\Shashank\OneDrive\Desktop\index2.txt","r") as index:
        lines=main.readlines()
        search = input("Enter the word to be searched:") 
        start2 = time.time () 
        for line in index:
            if search in line:
                print("The line is here in index file"+ line)
                line1 = line.split(" ") 
                loc = line1[1].split() 
                locate = int(loc[0]) 
                x = main.seek(locate) 
                y = main.readlines(locate) 
                result= [ind for ind in y if search in ind] 
                result1= result[0].split(' ') 
                c=1
                for m1 in main.readlines():
                     l = m1.split(" ") 
                     loc1 = line1[1].split()
                locate1 = int(loc[0]) 
                x1 = main.seek(locate1) 
                y1 = main.readlines(locate1) 
                for n in y1:
                    if search in n:
                        str1=" "
                        n1=n.split(" ")
                        print(str1.join(n1)) 
if c==1:
    end1=time.time()
    print("Completed Searching in:",end1-start2,"sec")
                             
    q=input("Do you want to modify Y/N:")
    if q=='Y' or q=='y':
        f1=open(r"C:\Users\Shashank\OneDrive\Desktop\cb1.txt", errors='ignore')
        data=f1.read()
        f2=input("Enter the word to be replaced:")
        f3=input("Replace with:")
        start3=time.time()
        replaced_value=data.replace(f2,f3)
        f1=open(r"C:\Users\Shashank\OneDrive\Desktop\cb1.txt","wt")
        f1.write(replaced_value)
        end3=time.time()
        print("Replaced Successfully in",end3-start3,"sec")
        f1.close()
    else:
        print("Done!!")
else:
    print("Not Found")