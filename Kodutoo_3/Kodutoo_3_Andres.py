# Kodutoo 3
# 21.09.2014
# Andres Liiver

numbers = set("0123456789")

def unpack(str):
    result = ""
    num = ""
    i = 0

    while i < len(str):
        if str[i] == "(":
            if num != "":
                result = result[:-1] + result[-1:] * int(num)
                num = ""

            str = result + unpack(str[i+1:])
            i -= 1
        elif str[i] == ")":
            if num != "":
                result = result[:-1] + result[-1:] * int(num)
                num = ""

            for char in str[i+1:]:
                if char in numbers:
                    num += char
                else:
                    break

            if num != "":
                return result * int(num) + str[i+len(num)+1:]
            else:
                return result + str[i+1:]

        elif str[i] in numbers:
            num += str[i]
        else:
            if num != "":
                result = result[:-1] + result[-1:] * int(num)
                num = ""

            result += str[i]

        i += 1

    if num != "":
        return result[:-1] + result[-1:] * int(num)
    else:
        return result

print("a3bc2 :", unpack("a3bc2"))
print("a10bc2 :", unpack("a10bc2"))
print("a(bc)2d :", unpack("a(bc)2d"))
print("a(bc)d :", unpack("a(bc)d"))
print("a(bc)10d :", unpack("a(bc)10d"))
print("(a2)2 :", unpack("(a2)2"))
print("a(b2c)2d :", unpack("a(b2c)2d"))
print("a(b(cd)2e)2f :", unpack("a(b(cd)2e)2f"))
print()
print("a(b(c(d(efg)2)3)h)2i :", unpack("a(b(c(d(efg)2)3)h)2i"))
print()
print("(a(b(c(d(efg)2)3)h)2i)2 :", unpack("(a(b(c(d(efg)2)3)h)2i)2"))
print()
print("a2(bc(e2d)3hj(io)4Y)3f :", unpack("a2(bc(e2d)3hj(io)4Y)3f"))