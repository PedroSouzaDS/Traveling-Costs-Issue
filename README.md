## Problema com passagens e diárias de viagens para assuntos acadêmicos e administrativos da Universidade Federal de Ouro Preto

A Universidade Federal de Ouro Preto-UFOP, localizada na cidade de Ouro Preto-MG, Brasil, tem uma grande demanda por passagens, tanto aéreas quanto terrestres, e de diárias para hotéis e pousadas em outras localidades devido a compromissos tanto acadêmicos quanto administrativos ou até mesmo políticos, tais demandas são de responsabilidade da PROPLAD (Pró-Reitoria de Orçamento, Planejamento e Administração). 

![aviao](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/aviao.gif)

No entanto, de acordo com o setor  de Compras da extinta fundação de apoio da Universidade, a FEOP, estes custos poderiam ser otimizados pois, segundo o setor, acontece um certo desperdício devido à falta de planejamento da viagem (compra de passagens na última hora) ou até mesmo a própria exigência do solicitante muitas vezes desnecessária e até mesmo abusiva. Tais custos com viagens e diárias nos últimos três anos (2017, 2018 e 2019) totalizaram, segundo os dados do problema, em R$2.270.704, 55.

A Proposta do estudo é analisar dados destes custos, fazer uma análise exploratória e gerar insights a respeito destes custos, fazer análises preditivas para os gastos no futuro e os tipos de transportes utilizados, propor alternativas com custos mais baixos e propor melhorias no sistema de controle de gastos da PROPLAD, onde responderemos as seguintes perguntas ao longo do trabalho:

1.  Qual o gasto anual de 2017, 2018 e 2019 com passagens e diárias respectivamente? E a média de gasto total?
    
2.  Quais as médias de gastos, individuais, com passagens e diárias durante os mesmos três anos. E a média de gastos totais?
    
3.  Quais as medidas de tendência central destas duas despesas (média, mediana, moda)? Como comporta as relações entre elas? Registre as interpretações.
    
4.  Qual a variância entre estes valores? Analisar por meio de um boxplot.
    
5.  Há algum tipo de correlação entre os dados?
    
6.  Há outliers entre os dados de ambas as despesas? Fazer uma análise de Outliers.
    
7.  Qual departamento lidera as solicitações de passagens e com quantas? E diárias? Deste departamento qual o professor com mais solicitações e gastos?
    
8.  Qual Órgão da UFOP lidera as solicitações de passagens e com quantas? E diárias? Deste Órgão qual o servidor com mais solicitações e gastos?
    
9.  Quais atributos faltam neste conjunto de dados? Podemos incluí-los no dataset? Fazer uma pesquisa destes possíveis atributos e incluí-los no dataset, caso seja necessário faça uma previsão destes novos atributos com base nos dados dos atributos já existentes (ex: prever destinos e meios de transportes usados de acordo com o preço das passagens, tipos de hospedagens com o valor das diárias). (Modelos Preditivos: Regressões, Decision Trees, Cluster, etc)
    
10.  Com base nas despesas destes anos e conhecendo, por meio da previsão anterior, os meios de transportes e hospedagens bem como seus respectivos aumentos a cada ano, fazer uma previsão destes gastos para o ano de para os próximos anos 2020, 2021 e 2022. (ARIMA, Time-Series, Média Móvel,etc)
    
11.  Com base no item 8, qual a taxa de crescimento/decrescimento nos valores dessas despesas ao longo dos anos 2017, 2018, 2019, 2020, 2021, 2022?
    
12.  Há alguma relação de Paretto entre as despesas e solicitantes? Caso haja, encaminhar à PROPLAD uma sugestão de abertura de sindicância para os solicitantes responsáveis pela parte majoritária de despesas. (Quais motivos de tanta viagem, qual o grau de importância para a instituição?)
    
13.  Há alternativas de transportes e hospedagens mais viáveis para reduzir os custos nestas despesas? Quais são essas alternativas? Fazer um atributo com nome e preço dessas novas alternativas e uma previsão com esses novos possíveis gastos semelhante ao item 9.
    
14.  Os dados presentes nas bases da PROPLAD são suficientes para estabelecer uma solução para otimizar estes custos. Quais dados seriam interessantes para a PROPLAD incluir e ter um maior controle sobre os custos com as viagens solicitadas.
    
15.  Com a pandemia do novo Coronavírus, muitos eventos que demandam viagens a longa distância estão sendo realizados via vídeo conferências (webinares, congressos, simpósios, etc). Quanto de economia o setor pode ter adotando tais tecnologias daqui em diante, mesmo no pós pandemia?
