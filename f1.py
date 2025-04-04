#write a python code for the following statements
#1)write the text""PROGRAMMING IN PYTHON" in to a file of name code.txt
#2)then reads the text again and prints it to the screen.
f=open("code.txt","w")
f.write("PROGRAMMING IN PYTHON")
f.close()
f=open("code.txt","r")
text=f.read()
print(text)
f.close()