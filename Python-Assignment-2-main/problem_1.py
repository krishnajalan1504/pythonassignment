#1.	Reverse the contents of the f1.txt
with open("f1.txt", "r+") as f:
    str = f.read()
    str1 = str.split(",") 
    ans = str1[::-1]       
    an1 = ",".join(ans)

with open("f1.txt","w+") as of:
    of.write(an1)