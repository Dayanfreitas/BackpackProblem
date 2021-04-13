# Atividade
Você ficará isolado na natureza selvagem. A única coisa que você poderá levar é uma mochila que suporta no máximo 30 kg. Você possui diversos itens de
sobrevivência, cada um possui "pontos de sobrevivência" (dados para cada item de acordo com a tabela). 

[Colocar imagens da tabela]

# Ciclo do Algoritmo Genético

![Algoritmo](https://github.com/Dayanfreitas/BackpackProblem/blob/master/Imagens/AlgoritmoGenetico.png)

## 1. Inicialização da populção  

    Existe algumas formas de iniciar um população, podendo ser aleatório,Heurística e etc.  
    No algoritmo para da inicio a população foi ultilizado o método aleatório.
    

2. Cálculo de aptidão (Fitness)

3. Seleção:
    Aleatória
    Por Torneio
    Usando a roleta

4. Cruzamento(Crossover)

    - Aleatório:  
        Cromossomo A = [1 ,2 ,3 ,4 ,5]  
        Cromossomo B = [6 ,7, 8, 9, 10]

    - Corta no “Meio”  
        [1, 2, 3, 8, 9, 10]  
        [6, 7, 8, 3, 4 , 5]

    - Single arithimetic Crossover

    - Partially
    - Pegando sub string

5. Mutação
    - Probabilidade de 1 %