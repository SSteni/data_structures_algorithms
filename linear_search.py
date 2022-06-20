target = 10
def linear_search(data,target):
    for idx, val in enumerate(data):
        if val == target:
            return idx
    return -1

linear_search(data,target)
