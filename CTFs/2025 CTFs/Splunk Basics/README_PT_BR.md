# TryHackMe: Splunk Basics — Investigação de SIEM

> [![Medium](https://img.shields.io/badge/Read_Full_Walkthrough_with_Images-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/splunk-basics-did-you-siem-21c64a5c9f5e)

---

### Category: Blue Team / Security Operations (SOC) / Log Analysis

Neste desafio do *Advent of Cyber*, utilizei o **Splunk** para investigar um ataque simulado contra um servidor web, praticando habilidades de *Threat Hunting* e análise de logs.

## 1. Exploração de Logs
O primeiro passo foi identificar o IP do atacante e entender o cenário. Utilizei a query básica para filtrar o tráfego web:
`index=main sourcetype=web_traffic`

## 2. Detecção de Anomalias e Picos de Tráfego
Para identificar o dia de maior atividade, utilizei visualizações de padrões de tráfego focando no campo `client_ip`. O pico de tráfego revelou o momento exato em que a infraestrutura foi mais pressionada.

## 3. Identificação de SQL Injection (Havij)
Filtrei os logs em busca de agentes de usuário (*User Agents*) maliciosos. Identifiquei tentativas de SQL Injection automatizadas através da ferramenta **Havij**, filtrando os eventos associados a esse agente específico.

## 4. Tentativas de Path Traversal
Utilizando o IP do atacante já identificado, filtrei por caminhos suspeitos (ex: `../../etc/passwd`). Isso permitiu contar exatamente quantas tentativas de acesso a arquivos sensíveis do servidor foram realizadas.

## 5. Logs de Firewall e Exfiltração de Dados
Para confirmar se o ataque foi bem-sucedido e se houve roubo de dados, analisei os logs de firewall entre o servidor comprometido e o IP de Comando e Controle (C2) do atacante:

```splunk
sourcetype=firewall_logs src_ip=<compromised_server> dest_ip=<attacker_ip>
| stats sum(size_bytes) AS total_exfiltrated
```
Este comando somou todos os bytes transferidos, confirmando o volume total de dados exfiltrados.

## Lições Técnicas (Threat Hunting Mindset)

- Filtragem de Ruído: Aprendi a filtrar tráfego benigno (navegadores comuns) para focar em ferramentas de ataque como sqlmap, Havij, curl e wget.

- Análise da Cadeia de Ataque: Consegui rastrear os passos do atacante, desde o reconhecimento e exploração até a exfiltração final.

- Valor do SIEM: O Splunk provou ser essencial para correlacionar tráfego web com logs de firewall, permitindo uma resposta a incidentes muito mais rápida.

---

## Redes!

<p align="center">
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
</p>