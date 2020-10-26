# 1ª Etapa: Limpeza dos Dados (Data Cleaning)

A importação dos dados dos Datasets listados apresentaram uma série de problemas que atrapalhasse qualqeur extração de informações, logo, com a ajuda da biblioteca Pandas foi realizado uma série de transformações para que, mais tarde, seja realizado uma boa análise exploratória dos dados e, com técnicas de análise e Machine Leraning, sejam extraídas as melhores informações para os dados. Foi realizado nesta etapa:

![minion](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/minion.gif)

1. Conferência dos tipos de dados presentes nas colunas e conversões (este último não foi necessário)

Os três datasets "dados2017acd", "dados2017adm", "dados2018" e "dados2019", devido a quantidade de detalhes foram tratados separadamente devido a quantidade de detalhes e falta de padões nos textos presentes para depois serem concatenados (Todos tiveram os nomes de suas colunas padronizados).

2. Textos de nomes de orgãos e nomes de pessoas padronizados, todos no formato "string.upper()"

3. Correção nos problemas de encoding e acentuações gráficas

4. Com os quatro datasets com textos padronizados, faz-se a concatenação através de suas linhas

4. Confere a congruência entre operações matemáticas, certifica-se que a soma entre colunas "Valor da passagem" + "valor da diária" são iguais "Valor da Viagem"

5. Trata-se "Missing Values". Neste ponto, apenas duas linhas continham Missing Values, eram nomes cadastrados sem nenhum valor de passagem ou de diária registrados. Devido a sua baixa significância no modelo (0,03%), estes dados foram excluídos, no entanto, foram destacados para serem enviados à PROPLAD para uma avriguação em uma planilha "Missing Values.xlsx".

6. Limpeza de dados completa, dados preparados exportados para o arquivo "Dataset_clean.xlsx" para ser trabalhado nas próximas etapas.

# Pronto! 

Dados limpos e organizados, preparados para passar para a 2ª etapa da análise exploratória ou extração de insights através do **MS Power B.I.** e sua linguagem **DAX**. A vantagem, para o Power B.I. de ter os dados preparados em python para depois ser trabalhado nele é que o arquivo fica bem mais leve em termos de memória (linguagem DAX ocupa muita memória)

