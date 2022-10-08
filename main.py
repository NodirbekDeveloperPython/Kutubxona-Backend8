# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import string
# harflar = string.ascii_letters[:26]
# s = "a1c1e1"
# for i in range(len(s)):
#     if s[i].isnumeric():
#         indeks = harflar.index(s[i-1])
#         indeks = indeks + int(s[i])
#         s = s.replace(s[i], harflar[indeks])
# print(s)


nums = list(range(0, 5))
for i in nums:
    result = i ** 2
    print(result)
