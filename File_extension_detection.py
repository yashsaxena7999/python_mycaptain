x=input("Enter a file to check whether the file entered is a Python File, C++ file or a C file : ")
def check_valid(x):
    if x.endswith(".py"):
        return "python file"
    elif x.endswith(".cpp") or x.endswith(".c++"):
        return "C++ file"
    elif x.endswith(".c"):
        return "C file"
    else:
        return "Invalid String"

res=check_valid(x)
print(res)