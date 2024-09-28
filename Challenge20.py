
def ins(stk, elm):
    if len(stk) == 0 or stk[-1] <= elm:
        stk.append(elm)
    else:
        tmp = stk.pop()
        ins(stk, elm)
        stk.append(tmp)
def sort_stk(stk):
    if len(stk) > 0:
        tmp = stk.pop()
        sort_stk(stk)
        ins(stk, tmp)
stk = [3, 1, 4, 2]
print("Original stack:", stk)
sort_stk(stk)
print("Sorted stack:", stk)
