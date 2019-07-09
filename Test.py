
def count(list):
        even=0
        odd=0
        for i in list:
                if i%2==0:
                        even=even+1
                else:
                        odd=odd+1
        return even,odd





list=(45,56,88,47,63,21,55,99,156)
e,o=count(list)
print(e)
print(o)