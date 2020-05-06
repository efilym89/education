from sys import argv

script_name, awr, ast, apr = argv
a, b, c = int(awr), int(ast), int(apr)

print("script name: ", script_name)
print(a * b + c)

