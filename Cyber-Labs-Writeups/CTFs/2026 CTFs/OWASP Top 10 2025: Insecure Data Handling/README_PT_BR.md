# OWASP Top 10 2025: Manipulação Insegura de Dados

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/owasp-top-10-2025-dominating-insecure-data-handling-tryhackme-write-up-2cf4f23415ee)

---

### Write-Up do TryHackMe e Laboratório de Exploração

Este repositório documenta a exploração técnica e prática de três categorias-chave do OWASP Top 10 (2025). O foco está no comportamento das aplicações e nos riscos associados à entrada de dados não confiáveis.

## Estrutura do Repositório
* [brute_xor.py](./brute_xor.py): Script em Python para força bruta automatizada de chaves XOR repetidas.  
* [sql_injection.py](./sql_injection.py): Documentação e implementação de payloads de SSTI (Server-Side Template Injection).  
* [pickle_rce_gen.py](./pickle_rce_gen.py): Gerador de payloads para Execução Remota de Código (RCE) via Desserialização Insegura.  

---

## A04: Falhas Criptográficas
### Visão Geral
Falhas criptográficas ocorrem quando dados sensíveis não são protegidos adequadamente durante o armazenamento ou a transmissão. Neste desafio prático, um serviço de compartilhamento de notas utilizava uma chave fraca e compartilhada, derivada de uma cifra XOR com repetição.

### Implementação: Força Bruta em XOR
A aplicação utilizava uma chave com um prefixo conhecido ("KEY"). O script abaixo foi desenvolvido para automatizar a descoberta do último caractere e descriptografar os dados-alvo.

Link do arquivo: [brute_xor.py](./brute_xor.py)

```python
# Lógica para rotação de chave e operação XOR
for char in possible_chars:
    key = prefix + char
    decrypted = "".join(chr(cipher_data[i] ^ ord(key[i % 4])) for i in range(len(cipher_data)))
    
    if "Meeting" in decrypted or "reminder" in decrypted.lower():
        print(f"Key found: {key}")
        break
```

## A05: Injeção (SSTI)

### Visão Geral
Vulnerabilidades de injeção surgem quando dados não confiáveis são enviados a um interpretador como parte de um comando ou consulta. Este exercício demonstra Server-Side Template Injection (SSTI) em um ambiente Jinja2. Diferente do SQL Injection tradicional, o SSTI explora o mecanismo de templates usado para renderizar páginas web dinâmicas.

### Técnica de Exploração
Ao injetar expressões de template como `{{7*7}}`, foi possível confirmar que o servidor estava avaliando operações matemáticas, identificando o mecanismo como Jinja2. O ataque foi então escalado para Execução Remota de Código (RCE) ao navegar pela hierarquia de objetos do Python até acessar o módulo `os`.

Link do arquivo: [sql_injection.py](./sql_injection.py)

**Payload utilizado:**
```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}
```

---

## A08: Falhas de Integridade de Software e Dados

### Visão Geral
Falhas de integridade ocorrem quando uma aplicação depende de plugins, bibliotecas ou dados de fontes não confiáveis sem verificação adequada. Um exemplo clássico é a Desserialização Insegura.

### Implementação: RCE com Pickle
Utilizando o módulo `pickle` do Python, o método `__reduce__` foi explorado para executar comandos arbitrários do sistema durante o processo de reconstrução do objeto (desserialização).

Link do arquivo: [pickle_rce_gen.py](./pickle_rce_gen.py)

```python
class MaliciousPayload:
    def __reduce__(self):
        # Execução de comandos em nível de sistema
        return (os.popen, ("cat flag.txt",))
```
### Redes!

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