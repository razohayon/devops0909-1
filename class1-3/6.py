# print(list(range(100, 1, -5)))
# names = ["ariel", "adi", "eran", "adir"]
# str_to_print = "Hello world"
#
# # for loop by index
# for i in range(len(names)):
#     print(str_to_print)
# # foreach loop
# for name in names:
#     print(name)
# # while loop
a = 0
# while a < 10:
#     print("a is not yet 10")
#     a += 1
#     print("a is", a)
#     if a == 5:
#         break


# 7 boom
a = 0
while a < 100:
    a = a + 1
    if a % 7 == 0 or str(a).find("7") == 0:
        # if a % 7 == 0 or "7" in str(a):
        print("BOOM")
        continue
    print(a)
else:
    print("GAME OVER")
