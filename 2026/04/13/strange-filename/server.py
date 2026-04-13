import subprocess

# list files
print("$ ls", flush=True)
subprocess.run(["ls"])

# cat a file, taking only one argument, without shell redirections
subprocess.run(["cat", input("$ cat ")])
