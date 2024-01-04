def number_encryptor(num):
    enc_num=''
    num = str(num)
    for i in num:
        i = int(i)
        i = i+1
        i = str(i)
        enc_num+=i

    return f"Your Encrypted number is {enc_num}"


print(number_encryptor(123))


    