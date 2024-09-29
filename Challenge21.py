def insert_bottom(stk, val):
    if len(stk) == 0:
        stk.append(val)
    else:
        top_item = stk.pop()
        insert_bottom(stk, val)
        stk.append(top_item)
def reverse_stack(stk):
    if len(stk) > 0:
        top_item = stk.pop()
        reverse_stack(stk)
        insert_bottom(stk, top_item)
stk = [3, 1, 4, 2]
reverse_stack(stk)
print("Reversed stack:", stk)
