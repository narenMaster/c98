f=open("test.txt")
filelines=f.readlines()
for line in filelines : 
    print(line)

introString="my name is naren   i am in ch e n n a i t a m i l n a du"
words=introString.split(" ")
print(words)

def greet(name):
    print("Hello , " + name + ". how are you ??" )
    input("write ur ans : ")
greet("mecowski mambroasa")    