from task_1 import Stack


def check_for_match(opn_elem, cls_elem):
    if (opn_elem == '[' and cls_elem == ']' or
            opn_elem == '{' and cls_elem == '}' or
            opn_elem == '(' and cls_elem == ')'):
        return True
    return False

def check_stack(stack):

    if stack.size() % 2 != 0:
        print('Несбалансированно')
        return

    elif (stack.count('(') != stack.count(')')
          or stack.count('[') != stack.count(']')
          or stack.count('{') != stack.count('}')):
        print('Несбалансированно')
        return

    else:
        pairs_found = 0
        expected_pairs = int(stack.size()) / 2
        brackets_open = ['(', '[', '{']

        for check in range(stack.size()):
            count_open = 0
            count_close = 0
            cls_element = stack.pop()
            if cls_element in brackets_open:                            #([(())]{[]})
                continue

            for element in stack[::-1]:
                if check_for_match(element, cls_element) and count_open == count_close:
                    pairs_found += 1
                    break

                else:
                    if element in brackets_open:
                        count_open += 1

                    else:
                        count_close += 1


        if pairs_found != expected_pairs:
            print(pairs_found)
            print(expected_pairs)
            print('Несбалансированно')
        else:
            print('Сбалансировано')

if __name__ == '__main__':
    b = Stack('][][][')
    c = Stack('([(())]{[]})')
    x = Stack('(([{())]})')
    y = Stack('(]][[)')
    test = Stack('[([])((([[[]]])))]{()}')
    check_stack(test)





