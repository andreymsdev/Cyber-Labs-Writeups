# TryHackMe: Lo-Fi — Write-Up

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/lo-fi-tryhackme-d71bc27ba0df)

---

### Categoria: Web Hacking / Inclusão de Arquivo Local (LFI)

Uma aplicação web simples para ouvir batidas de lo-fi, mas com uma falha crítica na forma como processa as requisições de páginas.

## 1. Reconhecimento
Iniciei com um scan de **Nmap** para identificar portas e serviços abertos:
* **Portas**: 22 (SSH) e 80 (Apache 2.2.22).
* **Alvo**: Um servidor web hospedando o site "Lo-Fi Music".

## 2. Detectando a Vulnerabilidade
Ao navegar pelo site, notei a estrutura da URL:
`http://IP_DA_MAQUINA/?page=relax.php`

Isso indica que o parâmetro `page` está sendo usado para incluir arquivos dinamicamente. Sem a devida sanitização, isso leva a uma vulnerabilidade de **Local File Inclusion (LFI)**.

## 3. Exploração (Path Traversal)
Para confirmar a vulnerabilidade, tentei ler o arquivo de senhas do sistema usando a técnica de path traversal:
`http://10.65.166.175/?page=../../../../../etc/passwd`

O servidor retornou com sucesso o conteúdo do arquivo `/etc/passwd`, confirmando que eu conseguia sair do diretório raiz da aplicação web (`/var/www/html`).

## 4. Caçada à Flag
O desafio afirmava que a flag estava na raiz do sistema de arquivos (`/`). Usei o `curl` para testar diferentes profundidades e nomes de arquivos.

```bash
curl "[http://10.65.166.175/?page=../../../../../flag.txt](http://10.65.166.175/?page=../../../../../flag.txt)
```

Ao subir níveis suficientes `(../)`, consegui alcançar o diretório raiz e capturar a flag.

---

## Lições Técnicas

Validação de Entrada: Nunca confie em entradas fornecidas pelo usuário em funções como `include()` ou `require()`.

Path Traversal: Cada `../` move o ponteiro um nível para cima nos diretórios. Mesmo que você não saiba a profundidade exata, adicionar `../` extras eventualmente parará na raiz do sistema (`/`).

Privilégio Mínimo: Servidores web devem ter permissões restritas para evitar a leitura de arquivos sensíveis como flag.txt ou /etc/passwd.

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