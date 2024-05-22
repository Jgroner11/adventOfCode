def floating_permutations(floating_address):
    acc = []
    def helper(s):
        pos = s.find('X')
        if pos == -1:
            acc.append(s)
        else:
            helper(s[:pos] + '0' + s[pos + 1:])
            helper(s[:pos] + '1' + s[pos + 1:])
    helper(floating_address)
    return acc


print(floating_permutations('000000000000000000000000000000X1101X'))

