def eval_postfix(expr):
    stk = []
    items = expr.split()
    def apply_op(op, y, x):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return int(x / y)
    for item in items:
        if item.isdigit():
            stk.append(int(item))
        else:
            y = stk.pop()
            x = stk.pop()
            res = apply_op(item, y, x)
            stk.append(res)
    
    return stk[0]
expr = "2 1 + 3 *"
res = eval_postfix(expr)
print(res)  
