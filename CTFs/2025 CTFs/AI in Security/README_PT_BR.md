# TryHackMe: AI in Security — Write-Up

> [![Medium](https://img.shields.io/badge/Ler_com_imagens!-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@andreymsdev/ai-in-security-old-saint-nick-b3f90c61a203)

---

### Categoria: IA na Segurança / Red Team / Blue Team / DevSecOps

Este desafio explora a influência da Inteligência Artificial na cibersegurança, demonstrando como assistentes automatizados podem ajudar a gerar exploits, analisar logs e revisar código-fonte.

## Etapas Principais

1. **Enumeração**: O Nmap revelou que a porta **5000** era o "coração" do desafio, onde residia a aplicação vulnerável.
2. **Red Team (Ataque)**: Com auxílio da IA, foi gerado um script Python para realizar uma **Injeção de SQL (SQLi)**. O payload utilizado (`' OR 1=1 --`) permitiu o bypass do login e a captura da flag no corpo da resposta.
3. **Blue Team (Defesa)**: A IA auxiliou na análise dos logs gerados pelo ataque, mostrando como identificar comportamentos anômalos.
4. **Software (DevSecOps)**: Analisamos como a IA pode encontrar falhas de segurança diretamente no código antes mesmo do deploy.

---

## Lições de Segurança
* **IA na Cibersegurança**: A IA acelera tanto o ataque quanto a defesa. Saber utilizá-la para criar ferramentas de automação é uma habilidade essencial para o analista moderno.
* **SQL Injection**: O desafio reforçou a importância de validar entradas do usuário para evitar execuções de comandos arbitrários no banco de dados.

---

## Redes!

<p align="center">
  <a href="https://www.linkedin.com/in/andrey-ms" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:andreym.professional@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
</p>