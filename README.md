# Sistema de Busca Informada para o 8-Puzzle

## Descrição
Este projeto implementa algoritmos de busca informada (A*) e não informada (BFS, DFS) para resolver o problema do 8-puzzle. A implementação utiliza Python e bibliotecas como `pandas`, `math`, `collections`, `random`, `tracemalloc`, e `time` para suporte ao código e à análise de desempenho.

## Algoritmos Implementados
- **A\*** (com heurísticas de Manhattan e Euclidiana)
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

## Estrutura do Projeto
- `create_problems.py`: Gera 30 quebra-cabeças 8-puzzle aleatórios.
- `main.py`: Executa os algoritmos e coleta os resultados.
- `utils.py`: Funções utilitárias para suporte aos algoritmos.
- `bfs.py`: Implementação do algoritmo BFS.
- `dfs.py`: Implementação do algoritmo DFS.
- `a_star.py`: Implementação do algoritmo A* com heurística de Manhattan.
- `a_star2.py`: Implementação do algoritmo A* com heurística Euclidiana.

## Execução

### Passo 1: Gerar os Quebra-Cabeças

O primeiro passo é gerar os quebra-cabeças 8-puzzle aleatórios usando o script `create_problems.py`. Este script cria 30 quebra-cabeças e os salva no arquivo `8puzzles.txt`.

Para gerar os quebra-cabeças, execute o comando:

```bash
python create_problems.py
```

Isso gerará o arquivo `8puzzles.txt`, contendo 30 configurações iniciais de quebra-cabeças 8-puzzle.

### Passo 2: Executar os Algoritmos

Com os quebra-cabeças gerados, o próximo passo é executar os algoritmos A\*, BFS e DFS para comparar seu desempenho.

Execute o script `main.py` com o comando:

```bash
python main.py
```

### Passo 3: Visualizar os Resultados

Os resultados de tempo de execução, nós explorados e consumo de memória serão armazenados no arquivo `results.csv`. Para visualizar e analisar esses dados, você pode utilizar bibliotecas como `pandas` e `matplotlib`.

```

## Requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas para executar o projeto:

- `pandas`
- `numpy`
- `matplotlib`

```

## Métricas Avaliadas

As principais métricas utilizadas para comparar os algoritmos incluem:

- **Tempo de Execução**: Medido em segundos, indica o tempo total para encontrar uma solução.
- **Consumo de Memória**: Quantidade de memória usada pelo algoritmo durante a execução.
- **Completude**: Avalia se o algoritmo sempre encontra uma solução, caso ela exista.
- **Optimalidade**: Verifica se o algoritmo encontra a solução de menor custo.
- **Nós Explorados**: Quantidade de estados processados durante a busca pela solução.

## Conclusão

Este projeto evidenciou a importância das heurísticas na busca informada (A\*). A heurística de Manhattan se mostrou a mais eficiente, tanto em tempo de execução quanto no número de nós explorados. O BFS, apesar de ser completo e ótimo, apresentou alto consumo de memória. O DFS, por outro lado, teve desempenho variável dependendo do problema.
