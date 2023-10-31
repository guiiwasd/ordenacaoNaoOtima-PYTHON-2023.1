# ordenacaoNaoOtima-PYTHON-2023.1
# ESTRUTURA DE DADOS
Código realizado para Busca no Vetor em Python, realizado em aula juntamente ao professor @marceloarantes19.

# ORDENAÇÃO NÃO ÓTIMA
1. *Bubble Sort*
- É um algoritmo composto por dois laços de repetição aninhados. O laço mais interno é responsável por fazer comparações de cada dois valores até que o menor esteja em sua posição correta.
   Complexidade de tempo no PIOR CASO Bubble Sort = O(n²)
   Complexidade de espaço = O(n)

2. *Selection Sort*
- É um algoritmo composto por dois laços de repetição aninhados. O laço mais interno é responsável por escolher o elemento que será inserido na posição determinada pelo índice do laço mais externo.
   Complexidade de tempo no PIOR CASO Insertion Sort = O(n²)
   Complexidade de espaço = O(n)
3. *Insertion Sort*
- É um algoritmo composto por dois laços de repetição aninhados no qual consideramos um vetor com duas partes: A primeira ordenada, a segunda desordenada. O laço mais interno é responsável por inserir um elemento da parte desordenada na parte ordenada do vetor
#
- Complexidade de tempo no PIOR CASO Selection Sort = O(n²) *Se já estiver ordenado, roda em O(n)
- Complexidade de espaço = O(n)

4. *Shell Sort*
- É um algoritmo que tenta reduzir a quantidade de trocas do Insertion Sort. São 3 laços de repetição, sendo que o laço mais externo determina a distância H entre os elementos a serem comparados, caindo até que seja 1.
- Complexidade de tempo no PIOR CASO Shell Sort = O(n^1.25)
