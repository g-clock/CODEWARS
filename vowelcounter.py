def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
        if(i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I'or i == 'i' or i == 'O' or i == 'o' or  i == 'U' or i == 'u'):
            num_vowels = num_vowels + 1
    print("The number of vowels are")
    print(num_vowels)


    return num_vowels
