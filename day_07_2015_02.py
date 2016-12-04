assigned_var = {}
unassigned_var = []
def call_assign(operand1, operand2):
    if operand1.isdigit():
        assigned_var[operand2] = int(operand1)
    elif operand1 in assigned_var:
        assigned_var[operand2] = assigned_var[operand1]
    else:
        unassigned_var.insert(0, 'ASSIGN')
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)
def chk_is_digit(operand1, operand2):
    if operand1.isdigit():
        call_assign(operand1, operand1)
    if operand2.isdigit():
        call_assign(operand2, operand2)

def call_and(operand1, operand2, operand3):
    chk_is_digit(operand1, operand2)
    if operand1 in assigned_var and operand2 in assigned_var:
        assigned_var[operand3] = assigned_var[operand1] & assigned_var[operand2]
    else:
        unassigned_var.insert(0, 'AND')
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)
        unassigned_var.insert(0, operand3)
def call_or(operand1, operand2, operand3):
    chk_is_digit(operand1, operand2)
    if operand1 in assigned_var and operand2 in assigned_var:
        assigned_var[operand3] = assigned_var[operand1] | assigned_var[operand2]
    else:
        unassigned_var.insert(0, 'OR')
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)
        unassigned_var.insert(0, operand3)
def call_lshift(operand1, operand2, operand3):
    chk_is_digit(operand1, operand2)
    if operand1 in assigned_var and operand2 in assigned_var:
        assigned_var[operand3] = assigned_var[operand1] << assigned_var[operand2]
    else:
        unassigned_var.insert(0, 'LSHIFT')
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)
        unassigned_var.insert(0, operand3)
def call_rshift(operand1, operand2, operand3):
    chk_is_digit(operand1, operand2)
    if operand1 in assigned_var and operand2 in assigned_var:
        assigned_var[operand3] = assigned_var[operand1] >> assigned_var[operand2]
    else:
        unassigned_var.insert(0, "RSHIFT")
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)
        unassigned_var.insert(0, operand3)
def call_not(operand1, operand2):
    if operand1 in assigned_var:
        assigned_var[operand2] = ~assigned_var[operand1] & 0xFFFF
    else:
        unassigned_var.insert(0, "NOT")
        unassigned_var.insert(0, operand1)
        unassigned_var.insert(0, operand2)

def process_rest_wires():
    while len(unassigned_var) != 0:
        operator = unassigned_var.pop()
        if operator == "AND":
            call_and(unassigned_var.pop(), unassigned_var.pop(), unassigned_var.pop())
        elif operator == "OR":
            call_or(unassigned_var.pop(), unassigned_var.pop(), unassigned_var.pop())
        elif operator == "NOT":
            call_not(unassigned_var.pop(), unassigned_var.pop())
        elif operator == "RSHIFT":
            call_rshift(unassigned_var.pop(), unassigned_var.pop(), unassigned_var.pop())
        elif operator == "LSHIFT":
            call_lshift(unassigned_var.pop(), unassigned_var.pop(), unassigned_var.pop())
        elif operator == "ASSIGN":
            call_assign(unassigned_var.pop(), unassigned_var.pop())
def read_input_and_process():
    with open("day_07_2015_01.txt","r") as f:
        for line in f:
            new_line = line.strip().split()
            if 'AND' in new_line:
                call_and(new_line[0], new_line[2], new_line[4])
            elif 'OR' in new_line:
                call_or(new_line[0], new_line[2], new_line[4])
            elif 'NOT' in new_line:
                call_not(new_line[1],new_line[3])
            elif 'RSHIFT' in new_line:
                call_rshift(new_line[0], new_line[2], new_line[4])
            elif 'LSHIFT' in new_line:
                call_lshift(new_line[0], new_line[2], new_line[4])
            else:
                call_assign(new_line[0], new_line[2])
    process_rest_wires()

read_input_and_process()

print "\n Value assigned to wire 'a' is : " + str(assigned_var['a'])

#CHANGED VALUE OF INPUT TO B TO PREVIOUS VALUE OF 01