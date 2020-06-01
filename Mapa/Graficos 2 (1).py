"""import pandas as  pd
from matplotlib import pyplot as plt
x = pd.read_excel(r"C:\Users\User\Desktop\Dados1.xlsx")
plt.plot(x["Notas"])
plt.ylabel("Nota")
plt.xlabel("Aluno")
plt.show()
"""
"""
from matplotlib import pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('eixo y')
plt.xlabel('eixo x')
plt.show()
Grafico normal
"""
"""
from matplotlib import pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'o')
plt.ylabel('eixo y')
plt.xlabel('eixo x')
plt.show()
Gráfico de pontos
"""
"""
from matplotlib import pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('eixo y')
plt.xlabel('eixo x')
plt.axis([0,6,0,20]) #[xmin,xmax,ymin,ymax]
plt.show()
Altero a escala do grafico
"""
"""
import numpy as np
from matplotlib import pyplot as plt

x1= np.array([1,2,3,4,5,6,7,8,9,10])

x2=x1
y2=x1**2

x3=x1
y3=x1**3
plt.axis([0,5,0,90])
plt.plot(x2,y2,'y--',x3,y3,'bs')
plt.show()
plotando dois graficos e utilizando array
"""
"""
from matplotlib import pyplot as plt

grupos = ['Produto A','Produto B','Produto C']
valores = [1,10,100]
plt.bar(grupos,valores)
plt.show()
"""

"""
from matplotlib import pyplot as plt
import pandas as pd
boletim = pd.read_excel(r'C:\Users\User\Desktop\Dados1.xlsx')
plt.ylabel(['Notas'])
plt.xlabel(['Aluno'])
plt.bar(boletim['Nome'],boletim['Notas'])
plt.show()
"""
"""
from matplotlib import pyplot as plt
import numpy as np
plt.style.use("ggplot")
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,5))

ax1.bar([1,2,3],[4,5,6])
ax2.barh([0.5,1,2.5],[0,1,2])

ax1.set(title = "Gráfico de barras  verticais",xlabel= 'eixo x',ylabel='eixo y')
ax2.set(title = "Grafico de barras horizontais",xlabel = 'eixo x',ylabel = 'eixo y')
plt.show()
"""
"""
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("ggplot")

boletim = pd.read_excel(r'C:\Users\User\Desktop\Dados1.xlsx')

fig,(fx1,fx2) = plt.subplots(1,2,figsize = (10,5))
fx1.bar(boletim['Nome'],boletim['Notas'])
fx2.barh(boletim['Nome'],boletim['Alturas'])

fx1.set(title = 'Boletim', xlabel = 'alunos',ylabel='Notas')
fx2.set(title = 'Altura dos alunos')

plt.show()
"""
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("ggplot")
x = np.arange(30)
boletim = pd.read_csv(r'C:\Users\User\Desktop\p+l2h5sQ.csv')
print(boletim)
plt.plot(boletim['day'][x],boletim['deaths'][x])
plt.show()
"""
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("ggplot")

Boletim = pd.read_csv(r'C:\Users\User\Desktop\p+l2h5sQ.csv')
x = np.arange(30)
y = 142 + np.arange(30)
fig,(F1,F2) = plt.subplots(1,2,figsize = (10,5))
F1.plot(Boletim['day'][x],Boletim['deaths'][x])
F2.plot(Boletim['day'][y],Boletim['deaths'][y])
F1.set(title = "Gráfico de mortes a cada dia no Afeganistão",xlabel="Dias",ylabel= "Mortes")
F2.set(title = "Gráfico de mortes a cada dia na  Albania",xlabel="Dias",ylabel= "Mortes")
plt.show()
"""
"""""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("ggplot")

Boletim = pd.read_csv(r'C:\Users\User\Desktop\p+l2h5sQ.csv')
x = np.arange(30)
y = 142 + np.arange(30)
fig,(F1,F2) = plt.subplots(1,2,figsize = (10,5))
F1.plot(Boletim['day'][x],Boletim['deaths'][x])
F2.plot(Boletim['day'][y],Boletim['deaths'][y])
F1.set(title = "Gráfico de mortes a cada dia no Afeganistão",xlabel="Dias",ylabel= "Mortes")
F2.set(title = "Gráfico de mortes a cada dia na  Albania",xlabel="Dias",ylabel= "Mortes")
plt.show()

"""
"""""
from matplotlib import pyplot as plt
import numpy as np


valores_produto_A = [6,7,8,4,4]
valores_produto_B = [3,12,3,4.1,6]

x1 = np.arange(len(valores_produto_A))
x2 = [x+0.25 for x in x1]

plt.bar(x1,valores_produto_A,width = 0.25,label = 'Produto A', color = 'b')
plt.bar(x2,valores_produto_B,width = 0.25,label = 'Produto B',color = 'r')

meses = ['Agosto','Setembro','Outubro','Novembro','Dezembro']
plt.xticks([x+0.25 for x in range(len(valores_produto_A))],meses)#coloca o nome dos meses no eixo x
plt.legend()
plt.title("Quantidade de vendas")
plt.show()
"""
""""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")
Boletim = pd.read_csv(r'C:\Users\User\Desktop\p+l2h5sQ.csv')
x = np.arange(30)
y =plt.plot(Boletim['day'][x],Boletim['deaths'][x])
plt.savefig('teste.png',format = 'png')
plt.show()
"""