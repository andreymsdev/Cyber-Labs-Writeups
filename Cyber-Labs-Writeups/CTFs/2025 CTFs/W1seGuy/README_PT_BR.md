# **W1seGuy**

---

Seu amigo me disse que você era sábio, mas eu não acredito nele. Consegue provar o contrário?

---

## **O que é XOR na Criptografia?**

XOR (Exclusive OR) é uma operação lógica que compara dois bits:

- Se os bits forem iguais (0 e 0, ou 1 e 1), o resultado é 0  
- Se os bits forem diferentes (0 e 1, ou 1 e 0), o resultado é 1  

Na criptografia, o XOR é muito usado porque:

- **Reversível**: aplicar a mesma chave novamente restaura a mensagem original  
- **Simples, rápido e útil**: usa apenas operações bit a bit  

Mas a **cifra XOR** não é segura para uso real atualmente — porém é excelente para aprender como a criptografia funciona.

---

## NETCAT

```
nc 10.201.39.23 1337
```

---

## **Descobrindo a Chave XOR e o CTF**

No código do desafio, observamos que:

1. As primeiras 4 letras da string codificada são “THM{”
2. O último caractere da string é “}”

> flag = 'THM{thisisafakeflag}'

Com isso, o programa pode fazer três perguntas:

1. `hex_text = input("Digite o texto codificado (hex): ")`
2. `start = input("Digite as letras iniciais conhecidas: ")`
3. `end = input("Digite o caractere final conhecido: ")`

Com essas informações, é possível descobrir a chave XOR e decodificar a mensagem.

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