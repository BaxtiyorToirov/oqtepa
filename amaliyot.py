

# class oqtepa:

#     def __init__(self,men) :
#         self.men=men
#         self.lst=[]
#         self.zakaz()
#     def zakaz(self):
#         zak=input("zakazni kiriting:")                                                           (oqtepa haqidagi misollar)
#         a=0
#         for i in self.men:
#             for j in i:
#                 if j=="nomi" and i[j] in zak:
#                     if i[j] in zak:
#                         print("Zakaz qabul qilindi!!!")
#                         self.lst.append(i)
#                         self.zakaslar()
#                         a+=1
#         if a==0:  
#             print("Bunday maxsulot yuq!!!")  
#             self.yana()        
#     def tayyor(self):
#         pass
#     def zakaslar(self):
#         print(self.lst)
#         self.yana()
#         pass
#     def summa(self):
#         lst2=[]
#         for i in self.lst:
#             for j in i:
#                 if j=="narxi":
#                     lst2.append(i[j])
#         pul=(sum(lst2))
#         print(f"Sizdan {pul} so'm buldi!!!\npulingizni kiriting:")
#         balans=int(input(""))
#         if balans>pul:
#             print(f"To'lovingiz qabul qilindi!!!\nTez orada zakazingiz tayyor buladi!!!")
#         else:
#             print("Mablag'ingiz yetarli emas!!!")
#         pass
#     def yana(self):
#         print("Yana zakaz qilasizmi!!!\n1-XA\n2-YUQ")
#         zk1=int(input(""))
#         if zk1==1:
#             self.zakaz()
#         else:
#             self.summa()


# menyu=[
#     {"nomi":"koffe","narxi":7000},
#     {"nomi":"lavash","narxi":27000},
#     {"nomi":"burger","narxi":20000},
#     {"nomi":"hot-dog","narxi":12000},
#     {"nomi":"klab","narxi":24000},
#     {"nomi":"cola","narxi":7000},
#     {"nomi":"pitsa","narxi":50000}
# ]
# menu=oqtepa(menyu)
