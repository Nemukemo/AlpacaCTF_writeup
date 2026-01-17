# flag is in ./flag.txt
s = input("> ")
assert s == s[::-1], "Not a palindrome!"
eval(s)
