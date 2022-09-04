# Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы пользоваться красотой каждого из них. Тем не менее если задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким образом он будет использовать языки которые знают все из них.
# Напишите программу, которая определяет, какие языки будут использоваться в сериале.
# Формат входных данных
# На вход программе в первой строке подается число nn — количество людей, которых донимает режиссер. В каждой из следующих nn строк через запятую указывается список языков, которые знает человек.
# Формат выходных данных
# Программа должна вывести список языков для сериала в лексикографическом порядке. Если такой список составить нельзя, необходимо вывести текст: 
# Сериал снять не удастся


n = int(input())
langs = [set(input().split(', ')) for _ in range(n)]
intersect = set.intersection(*langs)
if intersect:
    print(*sorted(intersect), sep=', ')
else:
    print('Сериал снять не удастся')
