def decToRoman(dec):
    rom = ""
    if (int(dec) > 3999 or int(dec) < 0):
        return "error"
    while True:
        if (int(dec) >= 1000):
            rom += "M"
            dec = str(int(dec) - 1000)
            continue
        if (int(dec) >= 900):
            rom += "CM"
            dec = str(int(dec) - 900)
            continue
        if (int(dec) >= 500):
            rom += "D"
            dec = str(int(dec) - 500)
            continue
        if (int(dec) >= 400):
            rom += "CD"
            dec = str(int(dec) - 400)
            continue
        if (int(dec) >= 100):
            rom += "C"
            dec = str(int(dec) - 100)
            continue
        if (int(dec) >= 90):
            rom += "XC"
            dec = str(int(dec) - 90)
            continue
        if (int(dec) >= 50):
            rom += "L"
            dec = str(int(dec) - 50)
            continue
        if (int(dec) >= 40):
            rom += "XL"
            dec = str(int(dec) - 40)
            continue
        if (int(dec) >= 10):
            rom += "X"
            dec = str(int(dec) - 10)
            continue
        if (int(dec) >= 9):
            rom += "IX"
            dec = str(int(dec) - 9)
            continue
        if (int(dec) >= 5):
            rom += "V"
            dec = str(int(dec) - 5)
            continue
        if (int(dec) >= 4):
            rom += "IV"
            dec = str(int(dec) - 4)
            continue
        if (int(dec) >= 1):
            rom += "I"
            dec = str(int(dec) - 1)
            continue
        break
    return rom

project1File = open("rom2dec.py", "w")
project1File.write("def romToDec(rom):\n")
for i in range(1, 4000):
    project1File.write("    if (rom == \"" + decToRoman(i) + "\"):\n        return \"" + str(i) + "\"\n")
project1File.write("    else:\n        return \"error\"\n\nrom = input(\"Input Roman Numeral: \")\nprint(\"Decimal: \" + romToDec(rom))")
project1File.close()

project2File = open("dec2rom.py", "w")
project2File.write("def decToRom(dec):\n")
for i in range(1, 4000):
    project2File.write("    if (dec == \"" + str(i) + "\"):\n        return \"" + decToRoman(i) + "\"\n")
project2File.write("    else:\n        return \"error\"\n\ndec = input(\"Input Decimal: \")\nprint(\"Roman Numeral: \" + decToRom(dec))")
project2File.close()

