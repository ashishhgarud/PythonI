# a string S and width W.
# Your task is to wrap the string into a paragraph of width.


import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
