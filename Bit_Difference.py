def Find_Bit_Diff(a,b):
    return bin(a^b).count("1")

print(Find_Bit_Diff(12,15))