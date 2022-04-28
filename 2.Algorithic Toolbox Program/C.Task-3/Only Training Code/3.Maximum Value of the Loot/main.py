# Problem
capcaity = 10
weight = [5, 4, 2, 1]
value = [200, 300, 100, 500]
out = []
while capcaity > 0:
    max_value_index = value.index(max(value))
    # array item
    weigth_of_max_value = weight[max_value_index]
    max_value = value[max_value_index]
    # Checking
    print(max_value_index)

    can_token = min(capcaity, weigth_of_max_value)
    # array
    out.append(max_value*can_token)
    # Removing max weight and max value
    weight.remove(weigth_of_max_value)
    value.remove(max_value)
    capcaity -= weigth_of_max_value

print(out)
