# SmartStock

SmartStock é um sistema para controle de alimentos disponíveis em residências, permitindo o cadastro dos itens por meio de cupom fiscal de compras. O objetivo é facilitar a gestão de estoque doméstico, evitando o desperdício e otimizando as compras.

## Funcionalidades

- **Cadastro de itens via cupom fiscal:** Extração automática de produtos e suas quantidades a partir de cupons fiscais.
- **Controle de estoque:** Exibição e gerenciamento dos itens atualmente disponíveis.
- **Alertas de validade:** Notificações para produtos próximos da data de vencimento.
- **Histórico de consumo:** Registra a entrada e saída de produtos, facilitando o planejamento de compras futuras.

## Tecnologias utilizadas

- **Frontend:** Flask (Python).
- **Banco de dados:** Armazenamento de dados no Firebase Firestore.
- **Autenticação:** Firebase Authentication para gerenciar usuários.
- **Extração de dados de cupons fiscais:** Algoritmos para leitura e interpretação de cupons.

## Requisitos

- Python 3.9 ou superior
- Conta no Firebase (Firestore e Authentication)

## Execução

1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências do backend:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor Flask:
   ```bash
   flask --app webview run --reload --host=0.0.0.0
   ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar um problema.


