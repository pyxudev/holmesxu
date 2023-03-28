def aorb(value_1, value_2, inp_value, res_1, res_2):
    if inp_value == value_1:
        return res_1
    elif inp_value == value_2:
        return res_2
    else:
        raise Exception('Error!')
