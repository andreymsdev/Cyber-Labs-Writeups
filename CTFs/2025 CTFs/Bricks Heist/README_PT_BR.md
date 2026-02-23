# TryHackMe: Bricks Heist — Write-Up

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/tryhack3m-bricks-heist-e13319dcfd25)

---

### Categoria: Web Hacking / Análise de Malware / Cryptojacking

Este laboratório envolve o "hack-back" de um servidor WordPress comprometido e a investigação de um processo suspeito em segundo plano que aponta para uma operação de cibercrime em larga escala.

## 1. Enumeração Inicial
Após adicionar `bricks.thm` ao meu arquivo `/etc/hosts`, iniciei com um scan de **Nmap**:
* **Porta Aberta**: 80 (HTTP)
* **Tecnologia**: WordPress 6.5

Utilizando `curl` e `wpscan`, identifiquei o tema **Bricks versão 1.9.5**, que é vulnerável a Execução Remota de Código (RCE).

## 2. Exploração (RCE)
Utilizei um exploit em Python direcionado à vulnerabilidade do tema Bricks para obter um shell interativo no servidor.

* **Flag Encontrada**: `THM{fl46_650c844110baced87e1606453b93f22a}` localizada em `/data/www/default/`.

## 3. Pós-Exploração e Resposta a Incidentes
O servidor estava extremamente lento, indicando um comprometimento além do meu próprio acesso. Comecei a investigar os processos do sistema:

* **Serviço Suspeito**: `TRYHACK3M` (identificado via `systemctl`).
* **Processo Malicioso**: `kdevtmpfsi` — um minerador de criptomoedas (cryptominer) bem conhecido.
* **Arquivo de Log**: Encontrei o `inet.conf` contendo strings codificadas.

## 4. Decodificação e Threat Intel
Utilizando o **CyberChef**, realizei uma decodificação em múltiplos estágios (Hex → Base64 → Base64) para revelar o endereço da carteira do atacante:
* **Carteira (Wallet)**: `bc1qyk79fcp9hd5kreprce89tkh4wrtl8avt4l67qa`

Ao pesquisar esta carteira no **Blockchair**, encontrei conexões com transações envolvendo o grupo de ransomware **LockBit**, ligando este caso de cryptojacking a um grande grupo de ameaças.

---

## Lições Técnicas
* **Pesquisa de Vulnerabilidades**: Identificar versões específicas de temas (Bricks 1.9.5) é crucial para encontrar RCEs de alto impacto.
* **Indicadores de Malware**: Reconhecer o `kdevtmpfsi` permitiu uma transição rápida da exploração web para a resposta a incidentes.
* **OSINT de Blockchain**: Rastrear o dinheiro (carteiras) é uma forma poderosa de atribuir ataques a grupos de ameaças conhecidos.

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
</p>