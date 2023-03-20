if __name__ == "__main__":
    list_1 = [2,3,2,4,2,8,8,7,6,5,4]
    list_2 = []
    for item in list_1:
        if item not in list_2:
            list_2.append(item)
    print(list_2)
    