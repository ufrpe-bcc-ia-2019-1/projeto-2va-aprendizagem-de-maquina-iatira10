# Projeto 2VA - Aprendizagem de Máquina				
## UFRPE - BCC - IA

## Descrição:				
O projeto consiste na utilização de métodos de aprendizagem de máquina para resolução de um **problema real**. A solução deve ser submetida no repositório do grupo no github (classroom), podendo ser feita tanto em Java ou Python, com o uso de frameworks tradicionais de aprendizagem de máquina (e.g., Weka, Scikit Learn, etc), preferencialmente no formato de um **Jupyter Notebook**. 

A soluço deve ser acompanhada de experimentos para avaliação do desempenho dos algoritmos e parametrizações consideradas. Os resultados finais deverão ser apresentados em formato de artigo (template SBC), sendo o mesmo divido nas seções: **Introdução, Materiais, Métodos, Experimentos, Resultados e Conclusão**.				
				
## Tipos de Projeto:				
- **Aplicação**: Escolher uma aplicação de interesse, e explorar as melhores formas de aplicar aprendizagem de máquina para resolvê-lo. (este ẽ o tipo mais comum)			
- **Replicação de resultados**: replicar os resultados em um artigo científico. No entanto, pedimos que, em vez de apenas replicar os resultados em um paper, também tente introduzir alguma variação (ou novo método) no estudo em questão.

## Observações:				
- Um projeto é considerado EXCELENTE, se este consiste em um trabalho publicável ou quase publicável em uma publicação/conferência científica. O aluno pode iniciar algo na disciplina e continuar aprimorando este trabalho na forma de pesquisa ou TCC nos semestres seguintes.                        			
- Pré-processamento: embora o objetivo do projeto não seja que o aluno gaste muito tempo coletando dados brutos, porém, o processo de inspeção e visualização dos dados, experimentando diferentes tipos de pré-processamento e fazendo análises de erros é muitas vezes uma parte importante da Aprendizagem de Máquina. Dessa forma, projetos que envolvam mais (ou menos) trabalho de pré-processamento serão avaliados de maneiras distintas.			
- Projetos com *deep learning*: Como o foco desta disciplina não é exatamento deep learning, pedimos que, se você decidir trabalhar em um projeto que envolva este tipo de técnica, certifique-se de usar outro material que aprendeu na aula também. Por exemplo, você pode configurar comparações *baseline* com knn, MLP, Naive Bayes, ou fazer alguma análise de dados usando os métodos não supervisionados abordados nas aulas. Podemos classificar esses projetos usando critérios diferentes para garantir que a classificação seja justa para alunos que não tiveram exposição a DL anteriormente.

## Seções do relatório final:	
### 1. INTRODUÇÂO
Definir o problema em termos objetivos

### 2. MATERIAIS
Descrição da(s) base(s) de dados
Descrição das procedimentos de pré-processamento (se aplicável)

### 3. MÉTODOS
Descrever o algoritmo a ser utilizado. 
Apresentar as diferentes parametrizações a serem consideradas

### 4. EXPERIMENTOS E RESULTADOS
Apresentação dos resultados obtidos
- Tabela com os valores da medida de avaliação considerada (ex. taxa de acerto, etc)
- Gráfico comparando os melhores resultados de cada método considerado

### 5. CONCLUSÃO
Comentar os resultados obtidos e pontos passíveis de melhorias

## Exemplo de relatório
[Exemplo 1](http://cs229.stanford.edu/proj2014/Yun%20Xu,%20Xinhui%20Wu,%20Qinxia%20Wang,%20Sentiment%20Analysis%20of%20Yelp's%20Ratings%20Based%20on%20Text%20Reviews.pdf)
[Exemplo 2](http://cs229.stanford.edu/proj2018/report/16.pdf)
[Exemplo 3](http://www.lbd.dcc.ufmg.br/colecoes/eniac/2016/059.pdf)
[Exemplo 4](https://portaldeconteudo.sbc.org.br/index.php/eniac/article/view/4477/4401)

## Sugestões de Temas
\# | Tema | Tipo | Dataset | Grupo 
--- | --- | --- | --- |--- 
1 | Classificação de espécies de cobras/escorpiões	 |  Classificação (imagens) | http://www.snakebd.com  <br> http://snakedatabase.org/  <br> https://spidy.goliathus.com/english/gallery-scorpions.php
2 | Classificação de questões (TREC dataset) | Classificação (textos) | http://cogcomp.org/Data/QA/QC/
3 | Analise de Sentimentos em tweets | Classificação (textos) | http://www.sananalytics.com/lab/twitter-sentiment/
4 | Recomendação de filmes sensível ao contexto | Recomendação | https://www.lucami.org/index.php/research/ldos-comoda-dataset/
5 | Predição de No-Show | Classificação | 
6 | Classificação de sons urbanos | Classificação (audio) | https://serv.cusp.nyu.edu/projects/urbansounddataset/

### Outros temas
Caso você tenha alguma outra sugestão de tema, submeta a sua proposta contendo as seguintes seções:
- Motivação: Que problema você está querendo resolver? Isto é uma aplicação, resultado teórico ou uma replicação de artigo?
- Método: Quais técnicas de aprendizado de máquina você está planejando aplicar ou melhorar?
- Experimentos planejados: quais experimentos você planeja executar? Como você planeja avaliar seu algoritmo de aprendizado de máquina?
- Base de dados: você pretende usar alguma base de dados? Ela é acessível publicamente? Qual o link?
