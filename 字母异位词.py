# coding=utf-8


# 点名的方式
list_new = []
def abc(sisterstr,brotherstr):
    for one_letter in sisterstr:
        list_brotherstr = list(brotherstr)
        if one_letter in list_brotherstr:
            list_new.append(one_letter)
            list_brotherstr.remove(one_letter)
            brotherstr = ''.join(list_brotherstr)
        else:
            return False
        str1 = ''.join(list_new)
        if sisterstr == str1 and list_brotherstr == []:
            return True
    return False


print abc('bbrt4rttyy1hh37','1hbr3yth4rttby7')

# 用sorted进行排序的方法
def bcd(str1,str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):return True
    else:return False

print bcd('jbbrt4rttyy137','1br3yt4rttjby7')
















