# Kodutoo 2
# 12.09.2014
# Andres Liiver

def brackets(str):
    print(str + ": ", end = "")
    
    if str == "":
        print("correct")
        return

    start_brackets = ('(','[','{')
    end_brackets = (')',']','}')
    brackets_found = []
    
    for i, char in enumerate(str):
        if char not in start_brackets and char not in end_brackets:
            print("illegal symbol at", i)
            return
        
        elif brackets_found == [] and char not in start_brackets:
            print("no opening bracket at", i)
            return
        
        elif brackets_found != []:
            bracket = brackets_found[len(brackets_found)-1]
            if char != end_brackets[start_brackets.index(bracket)] and \
            char not in start_brackets:
                print("wrong closing bracket at", i)
                return
            else:
                if char in start_brackets:
                    brackets_found.append(char)
                else:
                    brackets_found.pop()
            
        elif char in start_brackets:
            brackets_found.append(char)

    if brackets_found != []:
        print("no closing bracket at", len(str))
    else:
        print("correct")

brackets("")
brackets("()")
brackets("()()")
brackets(")")
brackets("()]")
brackets("[()")
brackets("[(])")
brackets("([]a)")