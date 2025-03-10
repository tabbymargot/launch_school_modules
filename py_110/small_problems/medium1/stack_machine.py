def minilang(command_string):
    stack = []
    register = 0
    command_list = command_string.split()

    # Note that instead of using try/except, I could have just added a final case block to the match statement as follows:
    # case _:
    #     register = int(string)
    
    for string in command_list:
        try:
            current_value = int(string)
            string = 'n'
        except:
            pass # If string isn't an integer, don't need to do anything here.

        match string:
            case 'PRINT':
                print(register)
            case 'n':
                register = current_value
            case 'PUSH':
                stack.append(register)
            case 'MULT':
                register = stack.pop() * register
            case 'ADD':
                register = stack.pop() + register
            case 'POP':
                register = stack.pop()
            case 'DIV':
                register = register // stack.pop()
            case 'REMAINDER':
                register = register % stack.pop()
            case 'SUB':
                register = register - stack.pop()
    
    return register



# minilang('PRINT')
# 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# (nothing is printed)