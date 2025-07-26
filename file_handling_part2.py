#open file in read mode
file_read = open('codingal.txt','r')
print("file in read mode -")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open('codingal.txt', 'w')
#write in the file
file_write.write("file in write mode ....")
file_write.write("HI1 I am Penguin. I am 1 yr. old")
file_write.close()

#open the file in append mode
file_append = open('codingal.txt', 'a')
#append in the file
file_append.write("/n file in append mode")
file_append.write("hi! I m penguin. I am 1 yr old")
