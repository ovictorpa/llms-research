# Análise de Erros em Testes Unitários Gerados por LLMs

## Introdução

Esta pesquisa busca investigar os erros em testes unitários gerados por LLMs, utilizando diferentes contextos de prompt. O objetivo é não apenas identificar esses erros, mas também avaliar sua criticidade e os possíveis impactos no processo de desenvolvimento, fornecendo diretrizes para a melhoria da qualidade de testes gerados por diferentes LLMs.

## Objetivos

- **Principal**: Construir um catálogo de erros em testes unitários gerados por LLMs e validar sua relevância e criticidade com desenvolvedores.
- **Específicos**:
  1. Comparar a qualidade dos testes gerados por diferentes LLMs em dois contextos de prompt: text2code e code2code.
  2. Identificar e categorizar erros presentes nesses testes.
  3. Avaliar os impactos desses erros no ciclo de vida do desenvolvimento de software.

## Questões de Pesquisa

1. Quais tipos de erros são mais comuns em testes unitários gerados por LLMs?
2. Como os diferentes contextos de prompt (text2code e code2code) influenciam a ocorrência de erros?
3. Os profissionais consideram esses erros críticos para a adoção de LLMs no desenvolvimento de software?
4. Quais são os impactos potenciais desses erros no ciclo de vida do desenvolvimento de acordo com os profissionais?

## Metodologia

1. **Geração de Testes Unitários**:
   - Selecionar quatro LLMs amplamente utilizados.
   - Utilizar dois contextos de prompt: 
     - **Text2Code**: prompts textuais descrevendo funcionalidades.
     - **Code2Code**: prompts contendo trechos de código.
   - Gerar testes para um conjunto pré-definido de funções e casos.

2. **Identificação de Erros**:
   - Analisar os testes gerados em busca de erros como:
     - Validade estrutural e sintática.
     - Falhas de execução.
     - Inconsistências semânticas ou lógicas.
   - Documentar cada erro com descrição e exemplos.

3. **Construção do Catálogo de Erros**:
   - Categorizar os erros identificados.
   - Fornecer descrições detalhadas e exemplos reais para cada categoria.

4. **Validação com Desenvolvedores**:
   - Conduzir questionários com desenvolvedores para:
     - Avaliar a criticidade de cada erro.
     - Identificar impactos percebidos no ciclo de vida do desenvolvimento.
   - Incorporar feedback no catálogo final.

## Justificativa

LLMs prometem acelerar a criação de testes, mas sem uma análise detalhada dos erros gerados, seu uso pode introduzir problemas difíceis de detectar. Este trabalho busca preencher essa lacuna, fornecendo resultados para a comunidade de desenvolvimento e para a evolução das tecnologias baseadas em LLMs.