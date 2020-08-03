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