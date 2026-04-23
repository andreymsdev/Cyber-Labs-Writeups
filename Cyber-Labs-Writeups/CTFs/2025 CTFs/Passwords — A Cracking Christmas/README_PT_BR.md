# TryHackMe: Passwords — A Cracking Christmas Write-Up

> [!TIP]
> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/passwords-a-cracking-christmas-821ec5661bc1)

---

### Categoria: Criptografia / Quebra de Senhas / Conscientização de Segurança

Este desafio foca nos riscos associados a senhas fracas em arquivos PDF e ZIP criptografados, demonstrando como atacantes utilizam ataques de dicionário offline para obter acesso não autorizado.

## 1. Quebra de PDF Criptografado
Para recuperar a senha do arquivo `flag.pdf`, utilizei o **pdfcrack**. Esta ferramenta permite um ataque direto contra o esquema de criptografia do PDF.



**Comando utilizado:**

```bash
pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
```

A ferramenta identificou com sucesso a senha do usuário, permitindo o acesso ao documento e à primeira flag.

## 2. Quebra de Arquivos ZIP Criptografados
A quebra de um arquivo ZIP requer um processo de duas etapas: extrair o hash e, em seguida, quebrá-lo.

**Passo A: Extração do Hash**
Utilizei o `zip2john` para converter a criptografia do arquivo ZIP em um formato que o John the Ripper consiga processar.

```bash
zip2john flag.zip > ziphash.txt
```


**Passo B: Ataque de Dicionário**
Utilizando o hash extraído e a wordlist `rockyou.txt`, executei o **John the Ripper**:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
```


Uma vez quebrado, descompactei o arquivo usando a senha recuperada e obtive a segunda flag dentro do arquivo `flag.txt`.

---

## Lições Técnicas

* **Quebra Baseada em Hash**: A criptografia protege a confidencialidade, mas não impede ataques offline. Ferramentas como o `zip2john` facilitam a separação da camada de proteção dos dados reais.
* **Poder das Wordlists**: A eficácia de um ataque de dicionário depende fortemente da qualidade da wordlist utilizada (ex: `rockyou.txt`).
* **Política de Senhas Fortes**: Este laboratório reforça por que senhas longas e complexas, além de padrões modernos de criptografia (como AES-256 para ZIP), são vitais para defender sistemas contra ferramentas automatizadas.

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
</p>