__author__ = 'Muse'
strs = [1]*10
sums = 0
for i in range(10):
    innum = raw_input("input:")
    if i ==0:
        strs[i]=int(innum)
        top = strs[i]
        down = strs[i]
    else:
        strs[i]=int(innum)
        if strs[i] > top:
            top = strs[i]
        elif strs[i] < down:
            down = strs[i]
    sums +=strs[i]
ave = (sums-top-down)/8.00
print ave
print('%.2f'% ave)