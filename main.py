# def array_diff(a, b):
#     lst = []
#     for i in a:
#         if not i in b:
#             lst.append(i)
#
#     return lst
#
#
# print(array_diff([1, 2], [1]))
# print(array_diff([1, 2, 2, 2, 3], [2]))
#
#
# def is_isogram(string):
#     low = string.lower()
#     lst = []
#     for i in low:
#         if not i in lst:
#             lst.append(i)
#         else:
#             return False
#
#     return True
#
#
# print(is_isogram('asror'))
# print(is_isogram('asro'))
#
#
# def get_middle(s):
#     length = len(s)
#     if length % 2 == 0:
#         return s[length // 2 - 1: length // 2 + 1]
#     else:
#         return s[length // 2]
#
#
# print(get_middle('asror'))
# print(get_middle('asrordos'))
#
#
# def count_positives_sum_negatives(arr):
#     if arr is None or len(arr) == 0:
#         return []
#     positive = []
#     negative = []
#     for i in arr:
#         if i > 0:
#             positive.append(i)
#         elif i < 0:
#             negative.append(i)
#
#     res = len(positive), sum(negative)
#     return list(res)
#
#
# def count_positives_sum_negatives(arr):
#     if arr is None or len(arr) == 0:
#         return []
#
#     positive_count = 0
#     negative_sum = 0
#
#     for i in arr:
#         if i > 0:
#             positive_count += 1
#         elif i < 0:
#             negative_sum += i
#
#     return [positive_count, negative_sum]
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# print(count_positives_sum_negatives([0, 0]))
#
#
# --------------------------- 22.11.2024-----------------
#
# def litres(time):
#     res = time * 0.5
#     result = res // 1
#     return result
#
#
# print(litres(3))
# print(litres(6.7))
# print(litres(11.8))
#
#
# def unique_in_order(sequence):
#     new_lst = []
#     for i in sequence:
#         if not new_lst or i != new_lst[-1]:
#             new_lst.append(i)
#
#     return new_lst
#
#
# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1, 2, 2, 3, 3]))
# print(unique_in_order((1, 2, 2, 3, 3)))
#
#
# def no_space(x):
#     lst = []
#     for i in x:
#         if i != ' ':
#             lst.append(i)
#
#     res = ''.join(lst)
#     return res
#
#
# print(no_space('asa asads'))
#
#
# def odd_or_even(arr):
#     res = sum(arr)
#     if res % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
#
# print(odd_or_even([0, -1, -5]))
# print(odd_or_even([0, 1, 4]))
# print(odd_or_even([0, 2, 4]))
# print(odd_or_even([0]))
#
#
# def alphabet_position(text):
#     lst = []
#     dictionary = {
#         'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
#         'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
#         't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
#     }
#     small = text.lower()
#     for i in small:
#         if i in dictionary:
#             lst.append(dictionary[i])
#
#     res = ' '.join(lst)
#     return res
#
#
# print(alphabet_position('The sunset sets at twelve o'))
#
#
# def is_square(n):
#     if n >= 0:
#         if n ** 0.5 == int(n ** 0.5):
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(is_square(25))
# print(is_square(-1))
# print(is_square(24))
#
#
# def accum(st):
#     res = []
#     for index, i in enumerate(st):
#         transformed = i.upper() + i.lower() * index
#         res.append(transformed)
#     return '-'.join(res)
#
#
# print(accum('aaa'))
#
#
# def sort_array(source_array):
#     odd = []
#     indexes = []
#     for index, i in enumerate(source_array):
#         if i % 2 != 0:
#             odd.append(i)
#             indexes.append(index)
#     odd_sorted = sorted(odd)
#
#     for i, index in enumerate(indexes):
#         source_array[index] = odd_sorted[i]
#
#     return source_array
#
#
# print(sort_array([1, 5, 2, 3]))
#
#
# def high(x):
#     alphabet_dict = {
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
#         'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
#         'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
#         'w': 23, 'x': 24, 'y': 25, 'z': 26
#     }
#     words = x.split(' ')
#     max_score = 0
#     max_word = ''
#
#     for i in words:
#         word_score = sum(alphabet_dict[j] for j in i)
#
#         if word_score > max_score:
#             max_score = word_score
#             max_word = i
#
#     return max_word
#
#
# print(high('asar asas'))
#
# ---------------------------------------- 23.11.2024 -------------------------------------------------------------
#
# def square_digits(num):
#     string = str(num)
#     lst = []
#     for n in string:
#         res = int(n) * int(n)
#         lst.append(str(res))
#
#     result = ''.join(lst)
#     return int(result)
#
#
# print(square_digits(123))
#
#
# def count_by(x, n):
#     lst = []
#     for i in range(1, n + 1):
#         y = x * i
#         lst.append(y)
#
#     return lst
#
#
# print(count_by(1, 10))
# print(count_by(2, 5))
#
# def find_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0
#
#
# print(find_average([1, 2, 4]))
# print(find_average([1, 0, 4]))
# print(find_average([]))
#
#
# def maps(a):
#     return [i * 2 for i in a]
#
#
# print(maps([1, 2, 3]))
#
#
# def solution(s):
#     lst = []
#     for i in s:
#         if i.isupper():
#             lst.append(' ')
#             lst.append(i)
#         else:
#             lst.append(i)
#
#     return ''.join(lst)
#
#
# print(solution('camelCasing'))
#
#
# def reverse_words(text):
#     lst = []
#     word = text.split(' ')
#     for i in word:
#         lst.append(i[::-1])
#
#     return ' '.join(lst)
#
#
# print(reverse_words('This is an example!'))
#
#
# def find_nb(m):
#     n = 1
#     summ = 0
#     while summ < m:
#         y = n ** 3
#         summ += y
#         if summ == m:
#             return n
#         n += 1
#     return -1
#
#
# print(find_nb(1071225))
