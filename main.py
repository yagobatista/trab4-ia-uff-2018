from random import randint
from sklearn import linear_model
# cancelamentos de mensalidade
churn = []

# modelo ('dias_sem_uso', 'reclamacoes', 'pagamento_em_dia')

# cliente que usam pouco o sistema
clientes_pouco_engajados = []
for cliente_id in range(0, 500):
    clientes_pouco_engajados.append(
        [randint(5, 10), randint(3, 10), randint(0, 2)])
    churn.append(True)

# clientes que usam batantes o sistema, geram pouca reclamções e pagam a mensalidade em dia 
clientes_engajados = []
for cliente_id in range(0, 500):
    clientes_engajados.append([randint(0, 4), randint(0, 3), randint(0, 2)])
    churn.append(False)

# cliente que estão entrando em processo de falência 
clientes_entrando_em_falencia = []
for cliente_id in range(0, 500):
    clientes_entrando_em_falencia.append(
        [randint(0, 4), randint(0, 3), randint(10, 40)])
    churn.append(True)

# clientes que estão insatisfeitos com o produto e geram muitas reclamações
clientes_insatisfeitos_com_produto = []
for cliente_id in range(0, 500):
    clientes_insatisfeitos_com_produto.append(
        [randint(0, 4), randint(10, 30), randint(0, 2)])
    churn.append(True)


train_data = clientes_pouco_engajados[:498] + \
    clientes_engajados[:498] + clientes_entrando_em_falencia[:498] + \
    clientes_insatisfeitos_com_produto[:498]

result_churn = churn[:498] + churn[500:998] + \
    churn[1000:1498] + churn[1500:1998]

test_data = clientes_pouco_engajados[498:500] + \
    clientes_engajados[498:500] + clientes_entrando_em_falencia[498:500] + \
    clientes_insatisfeitos_com_produto[498:500]

# regreção linear
lin_reg = linear_model.LinearRegression()
lin_reg.fit(train_data, result_churn)
results_lin_reg = lin_reg.predict(test_data)


print('Teste com clientes pouco engajados',
      results_lin_reg[:2], end=' valor esperado 1\n')
print('Teste com clientes engajados',
      results_lin_reg[2:4], end=' valor esperado 0\n')
print('Teste com clientes que estão entrando em falência',
      results_lin_reg[4:6], end=' valor esperado 1\n')
print('Teste com clientes que estão insatisfeito com o produto',
      results_lin_reg[6:8], end=' valor esperado 1\n')
