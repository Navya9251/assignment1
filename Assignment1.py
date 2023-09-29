# Write a Python program to get the Fibonacci series between 0 to 50

n1,n2 = 0,1
print(n1)
while n2<50:
    print(n2)
    n1,n2 = n2, n1+n2
    
    
   
#Write a Python program that accepts a word from the user and reverse it.

word = input("Enter a word to reverse: ")
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")
    print("\n")


#Write a Python program to count the number of even and odd numbers from a series of numbers.

list1 = [0,1,2,3,4,5,6,7,8,9,16,25,48,50]
even_count=0
odd_count=0
for num in list1:
    if num % 2==0:
        even_count += 1
    else :
        odd_count += 1
print("even  numbers in the list: ", even_count)
print("odd numbers in the list : ",odd_count)