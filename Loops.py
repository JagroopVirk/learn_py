#for i in range(1, 11):
#    print(i)

# a_list = ["One", "Two", "Three", "Four", "Five"]
#
#
# for i in range(len(a_list)):
#    print(str(i+1) + " : " + str(a_list[i]))
#
# print("--" * 20)
#
# b_list = [1, "Zero", 4, "One", 0, "Two", 2, "Three", 3, "Four"]
#
#
# def int_str(the_list):
#     int_list = []
#     str_list = []
#     for i in range(len(the_list)):
#
#         if i % 2 == 0:
#             int_list.append(the_list[i])
#         elif i % 2 != 0:
#             str_list.append(the_list[i])
#
#     sorted_int_list = sorted(int_list)
#
#     for x in range(len(int_list)):
#         print(str(sorted_int_list[x]) + " : " + str_list[x])
#
#
# int_str(b_list)
#
#
# print(range(0,10))
# print(list(range(0,5)))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')