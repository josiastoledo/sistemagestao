# Sistema de Gestão de Fazenda

Este projeto entrega uma API para gerenciar operações de uma fazenda com foco em:

- Controle de gastos financeiros
- Almoxarifado
- Posto de combustível
- Gestão de floresta de teca
- Controle de trincheira de silagem
- Controle de financiamentos

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

## Principais endpoints

### Financeiro
- `POST /finance/expenses` — cria um gasto financeiro.
- `GET /finance/expenses` — lista os gastos.
- `GET /finance/expenses/{expense_id}` — consulta um gasto específico.

### Almoxarifado
- `POST /inventory/items` — registra um item.
- `GET /inventory/items` — lista os itens.
- `GET /inventory/items/{item_id}` — consulta um item específico.

### Posto de combustível
- `POST /fuel/transactions` — registra abastecimento.
- `GET /fuel/transactions` — lista abastecimentos.
- `GET /fuel/transactions/{transaction_id}` — consulta um abastecimento.

### Floresta de teca
- `POST /forest/teak-plots` — cadastra um talhão de teca.
- `GET /forest/teak-plots` — lista talhões.
- `GET /forest/teak-plots/{plot_id}` — consulta um talhão.

### Trincheiras de silagem
- `POST /silage/trenches` — registra trincheira.
- `GET /silage/trenches` — lista trincheiras.
- `GET /silage/trenches/{trench_id}` — consulta uma trincheira.

### Financiamentos
- `POST /financing/contracts` — registra contrato.
- `GET /financing/contracts` — lista contratos.
- `GET /financing/contracts/{contract_id}` — consulta contrato.

### Resumo gerencial
- `GET /dashboard/summary` — entrega indicadores consolidados.

## Observações

Os dados ficam em memória enquanto a aplicação está ativa. Para persistência, substitua o módulo `app.storage` por um banco de dados.
