#Write a program to find the shortest palindrome that can be formed by adding characters to the beginning of a string
def check_palindrome(n):
    list2 = []
    list1 = []
    for i in n:
        list2.append(i)
    for j in range(len(list2)-1, -1, -1):
        list1.append(list2[j])
    if list2 == list1:
        return True
    else:
        return False

def shortest_palindrome(s):
    if check_palindrome(s):
        return s

    for i in range(len(s), 0, -1):
        if check_palindrome(s[:i]):
            return s[i:][::-1] + s
input_string = input("Enter a string: ")
result = shortest_palindrome(input_string)
print("Shortest palindrome:", result)
