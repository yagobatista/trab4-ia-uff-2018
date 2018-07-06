# Machine learn uff IA - 2018-1 trabalho 4

## Motivação

A escolha do tema foi inspirada em um dos grandes desafios da empresa em que trabalho, que é entender as demandas dos clientes para nosso sistema de gestão e as causas dos cancelamento de contratos.


## Objetivo

Desenvolver um sistema de previsão utilizando técnicas de aprendizado de máquina. O sistema teria acesso dados de uso, reclamações geradas e históricos de pagamentos dos clientes, e a partir deles tentaria prever quando o cliente cancelará o contrato do sistema, e gerar informações relevantes como o motivo do cancelamento e quais áreas do sistema de gestão são mais problemáticas.


## Geração de dados

A coleta dos dados necessários para treinar o sistema seria feito através de várias fontes. O dados de uso dos clientes seriam coletado através do log de operações do sistema, dados das reclamações a partir de um integração ao zendesk via api ou importação de planilha excel, dados dos pagamentos dos clientes na consulta ao nosso sistema financeiro interno. 


## Estrutura dos dados

log de operações - (cliente_id, area_do_sistema, data_operacao)<br>
tickets - (cliente_id, area_sistema, data_abertura, data_fechamento, data_primeira_resposta)<br>
pagamentos - (cliente_id, data_pagamento, data_esperada)<br>
churn - (cliente_id, data_churn, razao_id, mensagem)<br>
razão - (razao_id, razao_descricao)<br>
cliente - (cliente_id, cliente_nome)<br>


## Protótipo

Como a ideia do projeto é extremamente específica não encontrei nenhuma base de dados na internet que se enquadra-se nas minha necessidade, então para o propósito da prototipação, gerei aleatoriamente alguns dados para alimentar o algoritmo de aprendizado de máquina. Para facilitar a verificação dos resultados tentei simular alguns perfis específicos de clientes. Os clientes não engajados, que passam vários dias sem utilizar o sistema. Os clientes engajados, que usam regularmente o sistema, geram poucas reclamações e pagam a mensalidade em dia. Os clientes que estão em processo de falência, que não pagam regularmente o sua mensalidade. Os clientes clientes insatisfeitos, que geram grande número de reclamações. Gerei aleatoriamente quinhentos casos de cada perfil de cliente, por simplicidade na verificação separei apenas dois casos de cada um para testar os resultados da previsão. O restantes dos dados utilizei para alimentar o algoritmo de regressão linear. O protótipo foi desenvolvido na linguagem de programação python com auxílio da biblioteca de aprendizado de máquina scikit-learn.


## Instalação(linux)

```sh
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ git clone git@github.com:yagobatista/trab4-ia-uff-2018.git
$ cd trab4-ia-uff-2018
$ pip3 install sklearn
```


## Rodar

```sh
$ python3 main.py
```

