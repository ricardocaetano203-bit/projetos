# 💧 Consumo de Água ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github) ![Status](https://img.shields.io/badge/Status-Concluído-success) ![Projeto](https://img.shields.io/badge/Projeto-Agenda%207-orange)

## 📌 Sobre o projeto
O **Consumo de Água** é um programa desenvolvido em Python para classificar o perfil de consumo de água de diferentes tipos de imóveis. O sistema utiliza a estrutura `match/case` combinada com condicionais internas para analisar o tipo de imóvel e o respectivo consumo mensal em metros cúbicos ($m^3$).

## 🎯 Objetivo
O objetivo desta atividade é praticar conceitos fundamentais da linguagem Python, aprimorando a lógica de programação através de:
- 🐍 Variáveis e entrada de dados (`input`)
- 🔀 Estrutura de múltipla escolha (`match/case`)
- ⚙️ Estruturas condicionais internas (`if/elif/else`)
- 🖥️ Exibição de mensagens formatadas de saída

## 🏠 Tipos de Imóvel e Regras de Negócio
O programa avalia o perfil com base nas seguintes categorias:
- **Comercial**: Aplica a tarifa corporativa padrão.
- **Casa**: Analisa o consumo mensal (consumo moderado até 25 $m^3$ ou excessivo acima disso).
- **Apartamento**: Analisa faixas detalhadas de consumo (econômico abaixo de 10 $m^3$, moderado até 25 $m^3$, e excessivo acima de 25 $m^3$).
