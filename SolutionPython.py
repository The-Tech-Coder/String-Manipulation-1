class stringManipulation():
    def toLower(string):
        w = string.lower()
        return w

    def toUpper(string):
        x = string.upper()
        return x

    def totitle(string):
        y = string.title()
        return y

    def toswap(string):
        z = string.swapcase()
        return z

print(stringManipulation.toLower("Mi nombre es Roberto"))
print(stringManipulation.toUpper("Hola!! Mucho gusto."))
print(stringManipulation.totitle("this method Converts the first character of each word to upper case"))
print(stringManipulation.toswap("THIS method Converts LOWER case to UPPER case and vice versa"))
