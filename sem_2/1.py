zerkalo = 'A, H, I, M, O, T, U, V, W, X, Y, 1, 8'

inp = input()
stri = []
for i in range(len(inp)):
    stri.append(inp[i])


flag_zerkalo = True
for i in stri:
    if i not in zerkalo:
        flag_zerkalo = False



stri_1 = []
for i in range(-1, -(len(stri) + 1), -1):
    stri_1.append(stri[i])


flag_palindrom = True
if str(stri) != str(stri_1):
    flag_palindrom = False

if flag_palindrom and flag_zerkalo:
    print(f'{inp} is a mirrored palindrome.')
elif flag_palindrom and not flag_zerkalo:
    print(f'{inp} is a regular palindrome.')
elif not flag_palindrom and flag_zerkalo:
    print(f'{inp} is a mirrored string.')
else:
    print(f'{inp} is not a palindrome.')











