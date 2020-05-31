#André Elias (3013), Arthur Marciano (3019), Jhorrane (2618)

import ctypes

def retorna_reg(reg):
    if (reg == '$szero'):
        return '00000'
    elif (reg == '$v0'):
        return '00010'
    elif (reg == '$v1'):
        return '00011'
    elif (reg == '$a0'):
        return '00100'
    elif (reg == '$a1'):
        return '00101'
    elif (reg == '$a2'):
        return '00110'
    elif (reg == '$a3'):
        return '00111'
    elif (reg == '$t0'):
        return '01000'
    elif (reg == '$t1'):
        return '01001'
    elif (reg == '$t2'):
        return '01010'
    elif (reg == '$t3'):
        return '01011'
    elif (reg == '$t4'):
        return '01100'
    elif (reg == '$t5'):
        return '01101'
    elif (reg == '$t6'):
        return '01110'
    elif (reg == '$t7'):
        return '01111'
    elif (reg == '$s0'):
        return '10000'
    elif (reg == '$s1'):
        return '10001'
    elif (reg == '$s2'):
        return '10010'
    elif (reg == '$s3'):
        return '10011'
    elif (reg == '$s4'):
        return '10100'
    elif (reg == '$s5'):
        return '10101'
    elif (reg == '$s6'):
        return '10110'
    elif (reg == '$s7'):
        return '10111'
    elif (reg == '$t8'):
        return '11000'
    elif (reg == '$t9'):
        return '11001'
    elif (reg == '$k0'):
        return '11010'
    elif (reg == '$k1'):
        return '11011'
    elif (reg == '$gp'):
        return '11100'
    elif (reg == '$sp'):
        return '11101'
    elif (reg == '$fp'):
        return '11110'
    elif (reg == '$ra'):
        return '11111'
    elif (reg == '$at'):
        return '00001'
    else:
        return ''


def converte_binario(conv, bits = 16):
    conv = int(conv)
    if (conv >= 0):
        Nbin = bin(int(conv))
        Nbin = Nbin.replace("0b", "")
        while len(Nbin) != bits:
            if len(Nbin) == bits:
                return Nbin
            Nbin = "0" + Nbin
        return Nbin
    else:
        Nbin = bin(ctypes.c_ushort(conv).value)
        Nbin = Nbin.replace("0b", "")
        return Nbin;

def retorna_bitfield(assembly):

    assembly = assembly.replace(',', '')
    assembly = assembly.replace('\n', '')

    bitfield = assembly.split(' ')

    #Instruções tipo R
    if (bitfield[0] == 'add'):
        rd = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        rt = retorna_reg(bitfield[3])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + '100000' + "\n")

    elif (bitfield[0] == 'and'):
        rd = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        rt = retorna_reg(bitfield[3])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + '100100'+ "\n")

    elif (bitfield[0] == 'nor'):
        rd = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        rt = retorna_reg(bitfield[3])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + '100111'+ "\n")

    elif (bitfield[0] == 'or'):
        rd = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        rt = retorna_reg(bitfield[3])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + '100101'+ "\n")

    elif (bitfield[0] == 'sub'):
        rd = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        rt = retorna_reg(bitfield[3])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + '100010'+ "\n")

    elif (bitfield[0] == 'sll'):
        rd = retorna_reg(bitfield[1])
        rs = '00000'
        rt = retorna_reg(bitfield[2])
        arq.write('000000' + str(rs) + str(rt) + str(rd)+ converte_binario(bitfield[3], 5) + '000000'+ "\n")

    elif (bitfield[0] == 'srl'):
        rd = retorna_reg(bitfield[1])
        rs = '00000'
        rt = retorna_reg(bitfield[2])
        arq.write('000000' + str(rs) + str(rt) + str(rd) + '00000' + converte_binario(bitfield[3], 5) + '000010'+ "\n")

      #Instruções tipo I
    elif (bitfield[0] == 'addi'):
        rt = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        arq.write('001000' + str(rs) + str(rt) + converte_binario(bitfield[3])+ "\n")

    elif (bitfield[0] == 'andi'):
        rt = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        arq.write('001100' + str(rs) + str(rt) + converte_binario(bitfield[3])+ "\n")

    elif (bitfield[0] == 'ori'):
        rt = retorna_reg(bitfield[1])
        rs = retorna_reg(bitfield[2])
        arq.write('001101' + str(rs) + str(rt) + converte_binario(bitfield[3])+ "\n")


arqSaida = input("Digite o nome do arquivo de saida: ")
arq = open(arqSaida, 'w')

arqEscrita = input("Digite o nome do arquivo de escrita: ")
with open(arqEscrita) as arqLeitura:
  for line in arqLeitura:
    retorna_bitfield(line)

arqLeitura.close()
arq.close()