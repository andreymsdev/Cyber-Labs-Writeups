# TryHackMe: Seven Minutes on the Seine — OSINT Write-Up

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/the-case-seven-minutes-on-the-seine-tryhackme-ctf-561631484b96)

---

### Categoria: OSINT (Inteligência de Fontes Abertas) / Investigação de Segurança

Esta investigação simula uma resposta do mundo real a um assalto no **Museu do Louvre**. O objetivo foi reconstruir os eventos utilizando apenas ferramentas públicas e dados de fontes abertas.

## Etapas da Investigação

### 1. O Contexto do Assalto
Uma equipe com coletes de alta visibilidade invadiu a **Galerie d’Apollon**. Meu papel como analista foi identificar a rota de fuga e os detalhes da invasão utilizando:
* **Google Maps**: Para reconstrução geográfica das saídas do museu.
* **Ferramentas de Inspeção do Navegador**: Para encontrar pistas ocultas na estrutura web.
* **Bancos de Dados Públicos**: Verificação de protocolos do museu e arquivos históricos.

### 2. Busca Manual vs. IA
Durante o laboratório, percebi que, embora a IA seja uma ferramenta poderosa, ela teve dificuldades com os detalhes específicos deste caso. A abordagem bem-sucedida exigiu uma busca manual "à moda antiga" através da documentação oficial do Louvre e visualizações de satélite do Google Maps.

* **Descoberta Chave**: Identificação do ponto de acesso correto no museu (ex: `PORTE_DES_LIONS`).

### 3. Protocolo do Louvre e Análise de CCTV
A segunda parte do desafio focou em uma auditoria de vigilância. Os relatórios indicavam:
* Servidores desatualizados.
* Políticas de senha fracas.

Ao pesquisar por informações vazadas publicamente ou padrões de credenciais "óbvios" relacionados a auditorias do Louvre, consegui acessar o sistema de CCTV para revisar as filmagens do dia do incidente.

---

## Lições Pessoais e Impacto na Segurança
* **O Poder do OSINT**: Este CTF prova que a maioria das informações necessárias para uma invasão (ou uma investigação) já está disponível publicamente, se você souber onde procurar.
* **Vulnerabilidade de Credenciais**: A lição mais marcante foi como uma **única senha fraca** pode tornar inúteis milhões de dólares em tecnologia de segurança (câmeras, servidores, sensores).
* **Persistência**: Quando o ambiente do laboratório falhou, o acesso direto via IP e a pesquisa manual salvaram a investigação.

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