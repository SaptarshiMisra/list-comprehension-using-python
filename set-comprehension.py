def set_comp():
    old_list = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    new_set = {i * i for i in old_list if i % 2 == 0}
    return new_set


if __name__ == '__main__':
    print(set_comp())
