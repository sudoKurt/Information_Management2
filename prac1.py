while True:
    print("Enter String: ")
    str=input()
    if (str=="/"):
        break


for a in range(len(str)):
   match str[a]:
    case "a":
     print (f"{str[a]} Vowel")   
    
    case "e":
     print (f"{str[a]} Vowel")
     
    case "i":
     print (f"{str[a]} Vowel")
     
    case "o":
     print (f"{str[a]} Vowel")
     
    case "u":
     print (f"{str[a]} Vowel")

    case _:
     print (f"{str[a]} Consonant")






#Enter row: 3
#Enter col: 3
#Search: 3

#output:
# 1 2 [3]
#2 4 6
# [3] 6 9

#Enter row: 4
#Enter col: 4
#search: 4

#output:
# 1 2 3 [4]
# 2 [4] 6 8
# 3 6 9 12
# [4] 8 12 16

# Enter row: 0
# Enter col: -1
# search: 5
# stop the loop