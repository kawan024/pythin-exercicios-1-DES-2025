import random 

input("precione o entrer para lançar o dado")

resultado= random.randint(1,6)

print(f" O dado rolou : {resultado}" );

if resultado >6:
    print("voçê esta conseguindo")
elif resultado <2:
    print("tente novamente")