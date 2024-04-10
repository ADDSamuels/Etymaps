print("Code doesn't work")
# lowerAlphabet = "abcabcdefghijklmnopqrstuvwxyz"

# def convertToFileName(text):
#     textMem = ""
#     for char in text:
#         if char in lowerAlphabet:
#             textMem = textMem + char + "_"
#         else:
#             textMem = textMem + str(ord(char)) + "_"
#     return textMem
# def convertFromFileName(text):
#     if text.find("_") == -1:
#         raise Exception("convertFromFileNameError")
#     else:
#         if text[-1]!="_":
#             raise Exception("convertFromFileNameError")
#         else:
#             textMem = ""
#             textMem2 = ""
#             char = ""
#             for i in range(0,len(text)):
#                 char = text[i]
#                 if char != "_":
#                     textMem2 = textMem2 + char    
#                 else:
#                     if textMem2 in lowerAlphabet:
#                         textMem = textMem + textMem2    
#                     else:
#                         textMem = textMem + chr(int(textMem2))
#                     textMem2 = ""
#             return textMem

# fileName = convertToFileName(title)
# #if length of fileName is greater than 250, insert a placeholder
# if len(fileName) > 250:
#     with open(rf'badFileNames.txt', 'a', encoding = "utf-8") as file2:
#         file2.write(f"{title}<{badFileNames}\n")
#     fileName = str(badFileNames)
#     badFileNames += 1
#     with open(rf'badFileNames//{fileName}.txt', 'w', encoding = "utf-8") as file2:
#         for fileLine in newPage:
#             file2.write(f"{fileLine}\n")
# fileName
# with open(rf'data////{fileName}.txt', 'w', encoding = "utf-8") as file2:
#     for fileLine in newPage:
#         file2.write(f"{fileLine}\n")
# entryCount += 1
