import os

code = """
magic = /*code*/
if magic == 2508766360454420426020902195377847924746:
    print("/*flag*/")
else:
    print("bye")
"""

print("Show me your magic 🪄 ")
payload = input()
if len(payload) > 20:
    print("too long")
    exit(1)

compiled = code.replace("/*code*/", payload).replace("/*flag*/", os.environ.get("FLAG", "DUMMY_FLAG"))

exec(compiled, {"__builtins__": {"print": print}}, {})
 