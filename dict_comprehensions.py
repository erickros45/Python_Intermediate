def run():
    #my_dict={i: i**3 for i in range(1,101) if i % 3 != 0} # dictionary comprehension
    my_dict={i: i**0.5 for i in range(1,1001)}

    # my_dict={}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    print(my_dict)


if __name__=="__main__":
    run()