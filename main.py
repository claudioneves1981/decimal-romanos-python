def decimal_romanos():
   
    print('Digite 1 para converter decimal em romanos ') 
    print('Digite 2 para converter romanos em decimal ')
    opcao = input()
    decimal = 0
    romanos = ""
    
    numeros_romanos = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }
     
    if opcao == "1":
   	 decimal = int(input('Digite o decimal que deseja converter em romanos '))
   	 return converte_decimal(decimal,numeros_romanos)
    else:
    	 romanos = input('Digite em romano para ver em decimal:')
    	 return converte_romanos(romanos,numeros_romanos)

def converte_romanos(romanos,numeros_romanos):
    x = 0
    inverte = {}
    for i in range(0,len(romanos)):
        for decimal_num, item in numeros_romanos.items():
    	    if item == romanos[i] and len(item) == 1:
    	    	inverte[x]=decimal_num
    	    	x+=1
    	    	
    resultado = inverte[0]
    for i in range(0,len(inverte)):
    	if i + 1 < len(inverte) and inverte[i] < inverte[i+1]:
    		resultado = inverte[i+1] - resultado
    	elif i + 1 < len(inverte) and inverte[i] >= inverte[i+1]:
    		resultado += inverte[i+1]   
    		
    		
    return resultado
# kakaksmmaakk

def converte_decimal(decimal,numeros_romanos):
    num_romano = ""
    for decimal_num, item in numeros_romanos.items():
        while decimal >= decimal_num:
            num_romano += item
            decimal -= decimal_num
            
            
    resultado = num_romano  
    return resultado  
	
	
result = decimal_romanos()
print(result)
    


