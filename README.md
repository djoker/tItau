# Teste de Admissão Itau

Foi realizada as 2 primeiras partes do teste, referentes a manipulação de dados e backend. A descrição do teste pode ser acessado no diretório docs

## Problemas encontrados

Inicialmente tentei usar a extensão do framework *Flask* chamada **flask-restplus**. Essa extensão apresenta problemas com a versão do servidor web do Flask, o Werkzeug. Após algumas pesquisas, constatei que **flask-restplus** foi abandonada em detrimento a um fork da mesma, **flask-restx**. Adaptei a API para usar essa extensão

## Passos futuros

* Testes
* Melhorar a documentação gerada
* Refinar alguns processos:
  * Melhor tratamento de erros
  * Implementação de migrações com o uso do **Alembic**
  * Implementação de uma interface com base no Bootstrap

## Como usar

Para este projeto foi utilizado o Poetry. Então criamos o ambiente com:

poetry install

Então

poetry shell

### Carga

jupyter notebook

Este comando cria o ambiente Jupyter necessário para criar as bases (se quiser testar diretamente a API, os arquivos necessário já existem no repositorio, podendo iginorar o comando acima e as intruções posterios até a API)

Na interface no browser, no menu "Cell" escolha "Run all"

### API

Para inciar a API, digite:

python app.py
