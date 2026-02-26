cat <<EOF > README.md
# 🐍 Curso Intensivo de Python - Eric Matthes

Este repositório contém meus estudos, anotações e resoluções de exercícios baseados no livro **Curso Intensivo de Python**. O objetivo é registrar minha evolução dos fundamentos até o desenvolvimento de projetos práticos.

---

## 📂 Organização do Repositório

O projeto está dividido em três pilares principais, seguindo a metodologia do livro:

| Pasta | Descrição | O que contém? |
| :--- | :--- | :--- |
| **Capitulos/** | **Teoria e Exemplos** | Scripts de teste e anotações feitos durante a leitura de cada capítulo para fixação de conceitos. |
| **Exercicios/** | **Prática de Lógica** | Soluções dos desafios propostos ao final de cada tópico (ex: Exercícios 2.1 a 2.7). |
| **Projetos/** | **Aplicações Reais** | Projetos de maior escala envolvendo Pygame, Matplotlib e Django. |

---

## 🗺️ Mapa de Estudo

### Parte 1: Conceitos Básicos
- **Cap 1:** Instalação e Hello World.
- **Cap 2:** Variáveis e Tipos de Dados Simples.
- **Cap 3:** Introdução às Listas.
- **Cap 4:** Trabalhando com Listas (Loops).
- **Cap 5:** Instruções \`if\`.
- **Cap 6:** Dicionários.
- **Cap 7:** Entrada de Usuário e Laços \`while\`.
- **Cap 8:** Funções.
- **Cap 9:** Classes (POO).
- **Cap 10:** Arquivos e Exceções.
- **Cap 11:** Testando seu Código.

### Parte 2: Projetos Práticos
1. **Invasão Alienígena:** Desenvolvimento de um jogo de tiro espacial.
2. **Visualização de Dados:** Geração de gráficos e análise de dados climáticos/financeiros.
3. **Aplicações Web:** Criação de um sistema de log de aprendizado com Django.

---

## 🛠️ Como executar os scripts
1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório: \`git clone https://github.com/Taff4/Livro_Curso_Intensivo_de_Python.git\`
3. Navegue até o arquivo desejado e execute: \`python nome_do_arquivo.py\`

---
*Estudo realizado por **Rafael Lacerda** (@Taff4)*
EOF

# Comandos para subir a mudança
git add README.md
git commit -m "docs: detalhando a distribuicao de pastas no readme"
git push origin main
