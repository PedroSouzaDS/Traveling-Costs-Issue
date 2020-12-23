# 1ª Etapa: Transformação e Limpeza dos dados (Data Cleaning)

A importação dos dados dos Datasets listados apresentaram uma série de problemas que atrapalhasse qualqeur extração de informações, logo, com a ajuda da biblioteca Pandas foi realizado uma série de transformações para que, mais tarde, seja realizado uma boa análise exploratória dos dados e sejam extraídas as melhores informações para os dados, o que torna esta a etapa mais importante do projeto.

![minion](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/minion.gif)

Conforme a pasta "Dataset" deste repositório, o problema a ser modelado é refente aos dados dos anos 2017, 2018 e 2019 sendo que os dados de 2017 ainda era subdividido entre dois subsets referentes as demandas do setor acadêmico (acd) e do setor administrativo (adm) separadamente, totalizando em 4 diferentes conjuntos de dados referentes aos gastos com passagens e diárias da mesma instituição.

Tais conjuntos de dados continham problemas que impediam uma possível compilação na hora de realizar a concatenação das tabelas como problemas de encoding, diferenças de caixa alta de um para o outro, acentuação e ortografia nos atributos de texto, certificar-se que a coluna do Valor total da viagem (Vr_Viagem) realmente se referia a soma das colunas dos gastos dos valores das passagens (Vr_Passagem) com os gastos das diárias (Vr_Diaria) além do tratamento de dados faltantes (Missing Values). Tudo isso foi resolvido com a aplicação de funções do módulo PANDAS e técnicas de manipulação de Strings. 

Houveram transformações tanto a nível individual para cada tabela devido a facilidade de consultar os nomes dos dados com o método "dataset.Value_counts()" quanto na tabela final após a concatenação em uma tabela principal. Para maiores detalhes as transformações individuais podem ser consultadas no notebook "data_wrg(corrigido).ipynb" presente nesta pasta, devido a importância serão citadas aqui as transformações realizadas após a concatenação dos dados.

Como pode ser observado no exemplo dos dados "2017acd.csv", houveram transformações individuais, que também foram feitas nas demais tabelas, que transformaram os dados de texto claramente com problemas que prejudicariam o processo de concatenação em tabelas corrigidas e padronizadas em caixa alta, para facilitar uma possível exploração e busca por dados no futuro:

![2017acdWrong](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/2017acdWrong.JPG)
Podemos observar erros de encoding vindos da importação do arquivo bem como uma falta de padrão no texto, a parte corrigida pode ser vista a seguir na imagem do "df.head" da tabela principal.

Após a concatenação na imagem a seguir, podemos destacar algumas das principais transformações dos dados como Missing Values e certificação da operação matemática da coluna "Vr_Viagem" até a transformação total em um dataset principal onde serão extraídos os insights.
![concat](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/concat.JPG)

Em seguida foi aplicado um filtro do módulo PANDAS para se extrair os dados faltantes, porém, neste conjunto de dados, os dados faltantes aparecem apenas como "zeros", o que nem sempre significa que estão ausentes, levando em consideração que o solicitante de Passagens/Diárias pode solicitar apenas uma das duas modalidades sendo que a outra opção não escolhida fica com valor nulo, mas OBRIGATORIAMENTE, para estar na tabela tem que ter solicitado pelo menos uma das duas modalidades. Portanto, neste problema foi considerado "Missing Values" as linhas de dados que não possuiam reegistros de custos de NENHUMA das duas modalidades, Valores de Passagem, Diária e Total da viagem iguais a zero:
![missinValues](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/missing_values.JPG)
Podemos observar que, foi analisado qual o melhor método de tratamento de dados faltantes por meio de um percentual, onde devido a baixa significância dos dados para o problema (apenas 2 solicitantes, 0.03% dos dados) e a necessidade de alertar ao órgão um possível erro de registro de dados, a opção foi descartar as linhas em que faltavam os dados e os mesmos foram exportados para a planilha "Falta_gastos.xlsx" conforme a figura ou "Missing Values.xlsx" conforme este repositório para ser encaminhado ao setor responsável para uma possível auditoria. 

À seguir, o último dos importantes passos na preparação dos dados, é certificação da operação matemática envolvendo os três atributos dos custos, Valor da Passagem (Vr_Passagem), Valor da Diária (Vr_Diária) e a soma das duas e total Valor da Viagem (Vr_viagem). Considerando que tais operações foram feitas em planilhas por terceiros, precisava-se de certeza quanto a validade desta informação, pois seus resultados serão usados na próxima etapa.
![somaCol](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/confirm_sum.JPG)

E por fim, pode-se checar na tabela de informações do módulo "df.info" as novas dimensões da tabela e que os dados foram tratados bem como seus tipos mantidos para a próxima etapa:
![info](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/Cleaned_info.JPG)

O processo de exportação da nova tabela, originada da concatenação de todos os dados da Pró-Reitoria de Planejamento e Desenvolvimento pronta para a extração de informações nas etapas seguintes.
![clean](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Transformations/Cleaned_data.JPG)

# Pronto! 

Dados limpos e organizados, preparados para passar para a 2ª etapa da análise exploratória ou extração de insights através do **MS Power B.I.** e sua linguagem **DAX**. Os dados preparados em Python antes de serem importados em programas como MS Power B.I. oferecem uma grande vantagem por fornecer arquivos ".pbix" menos pesados. 

