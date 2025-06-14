# and -> para ser True, TUDO tem que ser True
# or -> para ser True, APENAS UM tem que ser True
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especia = True

print()
exp_1 = saldo >= saque and saque <= limite or conta_especia and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especia and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especia and saldo >= saque
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)