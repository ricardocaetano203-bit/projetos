# 💧 Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Projeto](https://img.shields.io/badge/Projeto-Agenda%207-orange)

## 📌 Sobre o projeto

O **Consumo de Água** é um programa desenvolvido em Python para classificar o perfil de consumo de água de diferentes tipos de imóveis.

O sistema solicita ao usuário o tipo de imóvel e o consumo mensal de água em metros cúbicos (m³), apresentando uma mensagem de acordo com as regras estabelecidas.

## 🎯 Objetivo

O objetivo deste projeto é praticar conceitos fundamentais da linguagem Python, como:

- 🐍 Variáveis
- ⌨️ Entrada de dados
- 🔢 Conversão de tipos
- 🔀 Estruturas condicionais
- ⚙️ Operadores lógicos
- 🖥️ Saída de dados

## 🏠 Tipos de imóvel

O programa trabalha com três tipos de imóvel:

- 🏢 Comercial
- 🏠 Casa
- 🏢 Apartamento

## 📊 Classificação do consumo

### 🏢 Comercial

Exibe:

**"Tarifa comercial aplicada – consulte o plano corporativo."**

### 🏢 Apartamento com consumo menor que 10 m³

Exibe:

**"Consumo econômico – excelente controle de água!"**

### 🏠 Casa ou 🏢 apartamento com consumo de até 25 m³

Exibe:

**"Consumo moderado – dentro do padrão residencial."**

### ⚠️ Consumo acima do limite residencial

Exibe:

**"Consumo excessivo – adote medidas de economia e verifique vazamentos."**

## ▶️ Como executar

Primeiro, abra o terminal e entre na pasta do projeto:

```bash
cd projetos/consumo-agua

python app.py

=== SISTEMA DE CONSUMO DE ÁGUA ===

Digite o tipo de imóvel (comercial, casa ou apartamento): apartamento
Digite o consumo mensal de água em m³: 8

Consumo econômico – excelente controle de água!


### Como deve ficar no GitHub

Dentro da sua pasta:

```text
📁 consumo-agua
   ├── 📄 app.py
   └── 📄 README.md
