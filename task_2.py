from task_1 import Stack

# def is_even(short_list, first_ind, second_ind):
#     cut_list = short_list[first_ind:second_ind]
#     # print(cut_list)

# def check_stack(stack):
#     if stack.size() % 2:
#         print('Несбалансированно')
#
#     else:
#         pairs = 0
#         # try:
#             # for first_ind, frst_element in enumerate(stack):
#             #     short_list = stack[first_ind + 1:]
#             #
#             #     for second_ind, snd_element in enumerate(short_list):
#             #         if (frst_element == '[' and snd_element == ']'
#             #                 or frst_element == '(' and snd_element == ')'
#             #                 or frst_element == '{' and snd_element == '}'):
#             #             is_even(short_list,first_ind,second_ind)
#         try:
#             for index, element in enumerate(stack):
#                 if (element == '[' and stack[index + 1] == ']' or
#                     element == '(' and stack[index + 1] == ')' or
#                     element == '{' and stack[index + 1] == '}'):
#                     pairs += 1
#
#                     for sym_count in range(index):
#
#
#
#         except:
#             pass

def check_for_match(opn_elem, cls_elem):
    if (opn_elem == '[' and cls_elem or
            opn_elem == '{' and cls_elem == '}' or
            opn_elem == '(' and cls_elem == ')'):
        return True
    return False

def check_stack(stack):
    brackets_open = ['(','[','{']
    if stack.size() % 2:
        print('Несбалансированно')
        return

    elif (stack.count('(') != stack.count(')')
          or stack.count('[') != stack.count(']')
          or stack.count('{') != stack.count('}')):
        print('Несбалансированно')
        return

    else:
        for checks in range(stack.size() - 1):
            first_out = stack.pop()
            count = stack.count(first_out)
            if first_out in brackets_open:
                print('Несбалансированно')
                return

            else:
                for index, element in enumerate(stack):
                    if check_for_match(element, first_out):
                        if count > 1:
                            count -= 1
                            continue
                        else:






a = Stack('[][][]')
b = Stack('][][][')


x = Stack('((()))')
y = Stack('}{}')
# check_stack(x)


