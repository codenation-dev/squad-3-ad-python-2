# Gestão de Comissões Televendas
#### Codenation - Aceleração Python for Web

## Integrantes do Projeto (Squad 3)

- Alexandre Frandulic Shimono
- Arthur Henrique Della Fraga
- Felipe Natividade
- Matheus de Souza Lins
- Sandro Wentz Forte

## Objetivo

Uma empresa de televendas gostaria de armazenar e calcular a comissão dos seus vendedores ao longo do tempo de acordo com o plano de comissão que eles escolheram. 
Para isso eles precisam de um sistema que fará tal cálculo da comissão ao adicionar o valor mensal das vendas no sistema. 
A empresa também precisa saber se as vendas dos seus vendedores estão satisfatórias através do cálculo da média ponderada dos valores de vendas nos últimos meses, e caso não esteja eles deverão ser notificados através do email.

Desta forma a implementação sistêmica, visa disponibilizar uma API para efetuar o cálculo da comissão dos vendedores conforme suas vendas mensais e regra de comissão selecionada no momento do cadastro do vendedor.

## Recursos

### Cadastro do Plano de Comissões

Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles. 
Para cadastrar um novo plano é necessário definir qual a porcentagem menor, o valor mínimo que será necessário para considerar a porcentagem de comissão maior e a porcentagem maior. 

| **Campo** | **Descrição** |**Definição** |
|------------|------------|------------| 
| min_value | Meta de Venda | Valor meta a ser atingido nas vendas |
| lower_percentage | Porcentagem Menor | Porcentagem que será aplicada ao valor da venda caso o vendedor não atinga a meta |
| upper_percentage | Porcentagem Maior | Porcentagem que será aplicada ao valor da venda caso o vendedor atinga a meta |

**Exemplo de Aplicação do Valor de Comissão**

| **Meta Venda** | **Porcentagem Menor** | **Porcentagem Maior** |**Valor Vendido** | **Porcentagem Aplicada** | **Valor Comissão** |
|---|---|---|---|---|---|
| R$ 1000,00 | 5% | 10% | R$ 800,00 | 5% | R$ 40,00|
| R$ 1000,00 | 5% | 10% | R$ 1200,00 | 10% | R$ 120,00|

A API deve possuir o seguinte comportamento:

**POST /comissions**
<pre>
{"lower_percentage": 2.5, "min_value": 5000.00, "upper_percentage": 10.50}
</pre>
**Response:**
<pre>
201 Created
{"id": 10}
</pre>

### Cadastro de Vendedores

O recurso de cadastro de vendedores é composto pela modelagem abaixo e deve ser informar um plano de comissão previamente cadastrado:

- Nome
- Endereço
- Telefone
- Idade
- E-mail
- CPF
- Plano de Comissões 

A API deve possuir o seguinte comportamento:

**POST/sellers**
<pre>
{"name": "José Vendedor", "address": "Rua abcd, 123", "telefone": "48012345678", "idade": 30, "email": "email@email.com", "cpf": "12345678910", "commission_plan": 1}
</pre>

**Response**
<pre>
201 Created
{"id": 100}
</pre>


### Cadastro de Vendas Mensais

Ao registrar as vendas mensais do vendedor, deve-se calcular o valor de comissão conforme o plano definido no cadastro do vendedor
Para o cálculo será necessário informar qual o vendedor, o mês (em números) em que ele fez as vendas e o valor das vendas.

Exemplo de requisição para calcular o valor da comissão do vendedor:

A API deve possuir o seguinte comportamento:

**POST/month_comission**
<pre>
{"seller": 10, "amount": 10000.00, "month": 2}
</pre>

**Response**
<pre>
200 OK
{"id": 100, "comission": 300.89}
</pre>

### Obter Lista de Vendedores

Recuperar a lista dos vendedores ordenados pelo valor de suas comissões. 
Para consultar a lista será necessário informar qual o mês atual para que possa ser feito o filtro e a ordenação dos valores. 
Quando o vendedor não tiver comissão no mês selecionado deve-se considerar R$ 0,00. 
OBS: Esse endpoint pode ser feito juntamente com o endpoint de vendedores mas não é obrigatório.

Exemplo de requisição para recuperar a lista de vendedores ordenados:

**GET /vendedores/2**

**Response**
<pre>
200 OK
[{"name": "Vendedor1", "id": 10, "comission": 1000.00}, {"name": "Vendedor2", "id": 15, "comission": 900.00}]
</pre>

### Envio de Notificações

Enviar uma notificação via email para o vendedor que não obtiver um valor acima do cálculo da média de comissões. 
Para calcular a média do vendedor, deve calcular a média ponderada dos últimos 5 meses desse vendedor considerando os maiores valores com os maiores pesos.
Se ele estiver abaixo em pelo menos 10% do valor da média deve-se enviar uma notificação para ele. Exemplo:

| **Mês** | **Valor R$** |**Peso** |
|------------|------------|------------| 
| 1 | R$ 1000 | 2 |
| 2 | R$ 500 | 1 |
| 3 | R$ 1100 | 3 |
| **Média** | **R$ 966,67** | **-** |

Esse vendedor não deve ser notificado caso o valor do mês atual seja maior do que R$ 966,67 - 10% = R$ 870,00.

Para efetuar a verificação, pode-se criar um endpoint que irá receber o valor atual de vendas e o ID do vendedor para calcular. 
Caso ele esteja abaixo do valor calculado uma notificação por email deve ser enviada para ele. 
Se não tiver o histórico de 5 meses basta considerar a quantidade de meses existentes para o cálculo. 
O cálculo sempre considera o mês corrente.

Exemplo de requisição para verificar se o vendedor deve ser notificado:

**POST /vendedores/2**
<pre>
{"seller": 10, "amount": 1000.65}
</pre>

**Response**
<pre>
200 OK
{"should_notify": true}
</pre>


## Apresentação do Projeto

O projeto deve ser efetuado por todos os integrantes do **Squad**, porém a **apresentação final** deverá ser realizada de forma **individual**.

Cada integrante deverá gravar um vídeo com no máximo 10 minutos.

Proposta de apresentação do projeto:

### Apresentação Pessoal

"Oi, pessoal…, eu me chamo _____ e vou apresentar para vocês o projeto final que fiz com a squad 3 da Aceleração Python for Web da Codenation."

### Apresentação do Projeto

- Membros da Squad;
- Descrição do projeto e desenvolvimento do processo que a squad utilizou para resolver o problema;
- Divisão de tarefas entre os membros da squad e quais foram suas principais responsabilidades;
- Tecnologias utilizadas e eficácia;
- Aprendizados destacados durante o processo e ao final do projeto;
- Duas principais dificuldades, e como foram contornadas;
- Dois principais acertos ou escolhas acertadas que fizeram diferença no projeto e por quê.

### Envio do Vídeo Individual

O vídeo deverá ser hospedado no **Youtube** (lembre de colocá-lo como não listado) com o título **Apresentação Projeto Final [Seu Nome] [Python para Web - Squad 3]**
O link do vídeo deve ser enviado para mario.machado@codenation.dev e ingrid.adam@codenation.dev, juntamente com o link do **Code Review** do projeto na plataforma **Codenation**, com o assunto **AceleraDev Python - Squad 3** até o dia 31/07/2019.
