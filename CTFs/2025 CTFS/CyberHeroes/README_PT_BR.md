# TryHackMe: CyberHeros — Write-Up

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/tryhackme-cyberheros-write-up-13cf0474cdb6)

---

### Categoria: Web Hacking / Bypass de Autenticação / Lógica de JavaScript

Este desafio foca na exploração de configurações incorretas e práticas de codificação inseguras, onde a lógica de autenticação sensível é tratada no lado do cliente (client-side) em vez do servidor.

## 1. Reconhecimento Inicial
Iniciei com um scan de **Nmap** para identificar portas e serviços abertos:
* **Resultado**: Porta 80/tcp aberta (Apache/2.4.48 Ubuntu).

A página principal exibia uma mensagem clara: *“Join our forces, find the vuln on our login page and login to join us.”* (Junte-se às nossas forças, encontre a vulnerabilidade em nossa página de login e entre para se juntar a nós).

## 2. Enumeração de Diretórios
Utilizando o **Gobuster** para buscar caminhos ocultos, encontrei:
* `/assets/`: Listagem de diretórios habilitada (Configuração incorreta).
* `/.htaccess` & `/.htpasswd`: Existentes, mas protegidos (403 Forbidden).

Esta etapa confirmou que, embora alguns arquivos estivessem protegidos, o servidor possuía exposição desnecessária de diretórios.

## 3. Analisando a Lógica de Login
Ao acessar o `login.html` e inspecionar o código-fonte, identifiquei a lógica de autenticação exposta diretamente no **JavaScript**:

```javascript
if (a.value=="h3ck3rBoi" & b.value==RevereString("54321@terceSrepuS")) {
   xhttp.open("GET", "RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_"+a.value+"_"+b.value+".txt", true);
   xhttp.send();
}
```
Ao reverter a string "54321@terceSrepuS", obtive as credenciais:

- **Usuário `h3ck3rBoi`
- **Senha:** `SuperSecret@12345`

## 4. Captura da Flag

O script gera um caminho dinâmico para o arquivo da flag baseado nas credenciais inseridas. Ao realizar o login ou construir manualmente a URL utilizando as credenciais descobertas, a flag foi capturada com sucesso.


### Vulnerabilidades Encontradas:
* **Credenciais Hardcoded no Client-Side**: O uso de JavaScript para validar senhas é uma falha crítica, pois o código é público e facilmente legível por qualquer usuário.
* **Listagem de Diretórios (Directory Listing)**: A exposição desnecessária de pastas como `/assets/` facilita o mapeamento da superfície de ataque por parte de um invasor.


## Conclusão

O caminho do ataque seguiu uma progressão lógica, do reconhecimento inicial até a exploração final:

1.  **Nmap**: Identificação da porta 80 aberta (Servidor Web Apache).
2.  **Gobuster**: Enumeração de diretórios que revelou falhas de configuração (Directory Listing).
3.  **Análise de Código**: A inspeção do JavaScript no `login.html` revelou credenciais expostas e a lógica de autenticação.
4.  **Acesso à Flag**: Uso das credenciais descobertas para construir a URL e obter o arquivo oculto.


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
</p>