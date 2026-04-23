# SQL Injection (SQLi)

SQL Injection (SQLi) é um tipo de ciberataque onde códigos SQL maliciosos são injetados em campos de entrada de uma aplicação vulnerável. Isso pode manipular as consultas ao banco de dados, potencialmente concedendo acesso não autorizado ou permitindo que atacantes recuperem, modifiquem ou excluam dados.

---

## O Que Eu Aprendi 

* **Detecção de Vulnerabilidades:** Identificação de pontos de entrada em campos de input, URLs e headers usando caracteres como `'` ou `"`.
* **Tipos de Ataque:**
    * **In-Band:** Uso de declarações `UNION` para exibir dados diretamente na página.
    * **Blind (Baseado em Booleano):** Inferência de dados através de respostas "Verdadeiro/Falso" do servidor.
    * **Blind (Baseado em Tempo):** Exfiltração de dados medindo atrasos de resposta do servidor com funções `SLEEP()`.
    * **Out-of-Band:** Forçar o banco de dados a enviar dados para um servidor externo via `DNS`.
* **Mapeamento de Banco de Dados:** Uso de `information_schema` para descobrir tabelas e colunas de forma sistemática.
* **Defesa:** Implementação de **Prepared Statements** e **Validação de Dados** como defesas primárias.

---

## Tarefa 1 - BRIEF
**O que significa SQL?** Structured Query Language (Linguagem de Consulta Estruturada)

---

## Tarefa 2 - O que é um Banco de Dados?
Um banco de dados é uma forma de armazenar coleções de dados eletronicamente de maneira organizada. Um banco de dados é controlado por um DBMS (SGBD), que é a sigla para Sistema de Gerenciamento de Banco de Dados. DBMSs dividem-se em dois campos: Relacionais e Não-Relacionais.

* **Qual é a sigla para o software que controla um banco de dados?** DBMS (SGBD)
* **Qual é o nome da estrutura em grade que contém os dados?** Tabela

---

## Tarefa 3 - O que é SQL?
SQL é uma linguagem rica em recursos usada para consultar bancos de dados. Essas consultas são referidas como declarações (statements).

* **Qual declaração SQL é usada para recuperar dados?** `SELECT`
* **Qual cláusula SQL pode ser usada para recuperar dados de múltiplas tabelas?** `UNION`
* **Qual declaração SQL é usada para adicionar dados?** `INSERT`

---

## Tarefa 4 - O que é SQL Injection?
O ponto em que uma aplicação web usando SQL pode se tornar vulnerável ao SQL Injection é quando dados fornecidos pelo usuário são incluídos na consulta SQL sem tratamento.

* **Qual caractere significa o fim de uma consulta SQL?** `;`

---

## Tarefa 5 - In-Band SQLi
O SQL Injection In-Band é o tipo mais fácil de detectar e explorar; refere-se ao uso do mesmo método de comunicação para explorar a vulnerabilidade e receber os resultados.

### Minha Metodologia:
Ao usar aspas simples, confirmamos que o site quebra, o que prova que podemos injetar comandos. Usei o "Truque da Cebola" (`UNION SELECT`) para alinhar as colunas até que o erro desaparecesse, revelando que a consulta usa três colunas.

Para o fingerprinting, usei `0 UNION SELECT 1, 2, database()` e descobri o nome do banco: **sqli_one**.

Em seguida, listei as tabelas usando `group_concat(table_name)` de `information_schema.tables`, o que identificou as tabelas `article` e `staff_users`.

Finalmente, ao consultar `information_schema.columns`, encontrei as colunas: `id`, `password` e `username`. Isso permitiu extrair as credenciais e capturar a flag.

* **Qual é a flag após completar o nível 1?** `THM{SQL_INJECTION_3840}`

---

## Tarefa 6 - Blind SQLi - Bypass de Autenticação
**O Exploit**
* **Campo Alvo:** Password
* **Payload:** `' OR 1=1;--`
* **Consulta Resultante:** `SELECT * FROM users WHERE username='' AND password='' OR 1=1;--`

* **Qual é a flag após completar o nível dois?** `THM{SQL_INJECTION_9581}`

---

## Tarefa 7 - Blind SQLi - Baseado em Booleano
**Vulnerabilidade:** O parâmetro GET no endpoint `/checkuser` permitia injeção de SQL.  
**Técnica:** Injeção baseada em Union foi usada para unir uma segunda consulta à original.  
**Bypass Chave:** Usar um nome de usuário inexistente forçou o banco de dados a ignorar a primeira parte da consulta e retornar os dados da declaração UNION.

### Passos de Execução:
1. **Enumeração de Colunas:** Identifiquei 3 colunas usando `' UNION SELECT 1,2,3`
2. **Extração de Dados:** Extraí a senha do admin injetando `' UNION SELECT 1,2,password FROM users WHERE username='admin'`
3. **Autenticação:** Login realizado via formulário principal usando as credenciais descobertas.

* **Qual é a flag após completar o nível três?** `THM{SQL_INJECTION_10934}`

---

## Tarefa 8 - Blind SQLi - Baseado em Tempo
**Método:** Blind Time-Based SQL Injection via parâmetro referrer.  
**Lógica Central:** O servidor não fornecia dados ou erros. O sucesso era medido apenas pelo tempo de resposta usando a função `SLEEP(5)`.

### Fluxo do Exploit:
1. **Detecção:** Injeção provada ao forçar um atraso de 5 segundos.
2. **Checagem de Tabela:** Confirmação da tabela `users` via consultas de atraso de tempo.
3. **Vazamento de Dados:** Ataque de força bruta na senha `4961` testando caracteres com o operador `LIKE` e observando quais tentativas ativavam o sleep de 5 segundos.
4. **Resultado:** Login como admin para recuperar a flag.

* **Qual é a final flag após completar o nível quatro?** `THM{SQL_INJECTION_MASTER}`

---

## Tarefa 9 - Out-of-Band SQLi
O SQL Injection fora de banda (Out-of-band) depende de recursos específicos ativados no servidor ou na lógica de negócio, que faz algum tipo de chamada de rede externa baseada nos resultados da consulta.

* **Nomeie um protocolo começando com D que pode ser usado para exfiltrar dados.** DNS

---

## Tarefa 10 - Remediação
Desenvolvedores podem proteger suas aplicações seguindo os conselhos abaixo:

* **Prepared Statements (Consultas Parametrizadas):** O banco de dados distingue entre a estrutura da consulta e os dados fornecidos.
* **Validação de Entrada:** Restringir entradas a apenas certos padrões (allow-lists).
* **Escapar Entradas do Usuário:** Adicionar uma barra invertida (`\`) antes de caracteres especiais para que sejam lidos apenas como texto.

* **Nomeie um método de se proteger contra SQL Injection.** Prepared Statements

---

**Link da Sala:** [https://tryhackme.com/room/sqlinjectionlm](https://tryhackme.com/room/sqlinjectionlm)

[![Artigo no Medium](https://img.shields.io/badge/Artigo_no_Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/sql-injection-complete-walkthrough-tryhackme)

---

## Redes!

<p>
  <a href="https://www.linkedin.com/in/andrey-ms" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:andreym.professional@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  <a href="https://medium.com/@andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Medium-%23000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://tryhackme.com/p/Tux10" target="_blank">
    <img src="https://img.shields.io/badge/-TryHackMe-%23212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
  <a href="https://devpost.com/andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Devpost-%23003E54?style=for-the-badge&logo=devpost&logoColor=white" alt="Devpost" />
  </a>
</p>