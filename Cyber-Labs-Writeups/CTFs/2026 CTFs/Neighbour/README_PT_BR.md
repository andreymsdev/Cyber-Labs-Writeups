# TryHackMe: Neighbour CTF Write-Up

> [![Medium](https://img.shields.io/badge/Leia_com_imagens_no_Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/january-1st-2026-code-stuff-and-tryhackme-neighbour-ctf-8acb31495934)

### Categoria: Insecure Direct Object Reference (IDOR) / Broken Access Control

Este CTF foca na exploração de controles de acesso baseados em parâmetros de URL, demonstrando como falhas na validação de identidade podem permitir o acesso a contas privilegiadas.

## Processo de Exploração

### 1. Enumeração Inicial
O primeiro passo foi realizar um scan de portas utilizando **Nmap** para identificar serviços ativos no alvo.

* **Resultado**: A porta **80 (HTTP)** estava aberta, indicando um serviço web em execução.

### 2. Análise da Aplicação Web
Ao acessar o IP do alvo via navegador, encontrei uma página de login que exigia credenciais. 

* **Investigação**: Analisando o código-fonte da página (`Ctrl + U`), foi possível identificar referências ao comportamento do sistema de autenticação, mas nenhuma credencial explícita.
* **Acesso Convidado**: O sistema permitia um acesso inicial como `guest`.

### 3. Identificação da Vulnerabilidade (IDOR)
Ao logar como convidado, a estrutura da URL revelou um parâmetro vulnerável:

`http://<TARGET_IP>/profile.php?user=guest`

A aplicação confiava apenas no valor do parâmetro `user` para determinar qual perfil exibir, sem validar se o usuário autenticado tinha permissão para visualizar outros perfis.

### 4. Exploração e Obtenção da Flag
Ao alterar manualmente o parâmetro de `guest` para `admin` na URL:

`http://<TARGET_IP>/profile.php?user=admin`

O sistema concedeu acesso total ao perfil do administrador, expondo as informações sensíveis e a flag do desafio.

---

## Lições Aprendidas
* **Controle de Acesso**: Nunca confie em parâmetros fornecidos pelo usuário para definir permissões de acesso.
* **IDOR**: Referências diretas a objetos devem ser validadas no lado do servidor (Server-Side) comparando a identidade do usuário na sessão com o recurso solicitado.

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
  <a href="https://devpost.com/andreymsdev" target="_blank">
    <img src="https://img.shields.io/badge/-Devpost-%23003E54?style=for-the-badge&logo=devpost&logoColor=white" alt="Devpost" />
  </a>
</p>