def main():
    res = []

    modulo_list = [
    (3,"Fizz"),
    (5,"Buzz")
    ]
    
    for i in range(1, 16):
        print_string = ""
        for mod in modulo_list:
            if i % mod[0] == 0:
                print_string += mod[1]
        
        if print_string == "":
            res.append(i)
        else:
            res.append(print_string)
    return res


if __name__ == '__main__':
    main()