# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo%20Elétrico-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Agenda](https://img.shields.io/badge/Agenda-5-orange)

## 📌 Sobre o projeto

A **Calculadora de Consumo de Energia** é um programa desenvolvido em Python para estimar o consumo mensal de energia elétrica de um aparelho.

O sistema solicita o nome do aparelho, sua potência em watts e o tempo médio de utilização diária. Com essas informações, calcula o consumo estimado em **kWh por mês**.

## 🎯 Objetivo

O objetivo do projeto é desenvolver uma aplicação simples para auxiliar na estimativa do consumo de energia elétrica e, ao mesmo tempo, praticar conceitos básicos de programação em Python.

## 🐍 Linguagem utilizada

O projeto foi desenvolvido utilizando a linguagem:

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

## 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000

consumoMensal = (150 × 10 × 30) / 1000
consumoMensal = 45 kWh/mês

Aparelho: Geladeira
Consumo estimado: 45 kWh/mês

cd projetos/consumo-energia

python app.py

=== CALCULADORA DE CONSUMO DE ENERGIA ===

=== CALCULADORA DE CONSUMO DE ENERGIA ===

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts: 150
Digite o tempo médio de uso diário em horas: 10

Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês

