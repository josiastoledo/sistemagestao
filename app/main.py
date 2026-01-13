from datetime import date
from typing import Dict, List

from fastapi import FastAPI, HTTPException

from app.models import (
    FinanceExpense,
    FinancingContract,
    FuelTransaction,
    InventoryItem,
    SilageTrench,
    TeakPlot,
)
from app.storage import Store

app = FastAPI(title="Sistema de Gestão de Fazenda", version="1.0.0")
store = Store()


def _get_or_404(repo_name: str, item_id: int):
    repo = store.repo(repo_name)
    try:
        return repo.get(item_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Registro não encontrado") from exc


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/finance/expenses", response_model=dict)
async def create_finance_expense(payload: FinanceExpense) -> Dict[str, int]:
    repo = store.repo("finance_expenses")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/finance/expenses", response_model=List[FinanceExpense])
async def list_finance_expenses() -> List[FinanceExpense]:
    return store.repo("finance_expenses").list_all()


@app.get("/finance/expenses/{expense_id}", response_model=FinanceExpense)
async def get_finance_expense(expense_id: int) -> FinanceExpense:
    return _get_or_404("finance_expenses", expense_id)


@app.post("/inventory/items", response_model=dict)
async def create_inventory_item(payload: InventoryItem) -> Dict[str, int]:
    repo = store.repo("inventory_items")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/inventory/items", response_model=List[InventoryItem])
async def list_inventory_items() -> List[InventoryItem]:
    return store.repo("inventory_items").list_all()


@app.get("/inventory/items/{item_id}", response_model=InventoryItem)
async def get_inventory_item(item_id: int) -> InventoryItem:
    return _get_or_404("inventory_items", item_id)


@app.post("/fuel/transactions", response_model=dict)
async def create_fuel_transaction(payload: FuelTransaction) -> Dict[str, int]:
    repo = store.repo("fuel_transactions")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/fuel/transactions", response_model=List[FuelTransaction])
async def list_fuel_transactions() -> List[FuelTransaction]:
    return store.repo("fuel_transactions").list_all()


@app.get("/fuel/transactions/{transaction_id}", response_model=FuelTransaction)
async def get_fuel_transaction(transaction_id: int) -> FuelTransaction:
    return _get_or_404("fuel_transactions", transaction_id)


@app.post("/forest/teak-plots", response_model=dict)
async def create_teak_plot(payload: TeakPlot) -> Dict[str, int]:
    repo = store.repo("teak_plots")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/forest/teak-plots", response_model=List[TeakPlot])
async def list_teak_plots() -> List[TeakPlot]:
    return store.repo("teak_plots").list_all()


@app.get("/forest/teak-plots/{plot_id}", response_model=TeakPlot)
async def get_teak_plot(plot_id: int) -> TeakPlot:
    return _get_or_404("teak_plots", plot_id)


@app.post("/silage/trenches", response_model=dict)
async def create_silage_trench(payload: SilageTrench) -> Dict[str, int]:
    repo = store.repo("silage_trenches")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/silage/trenches", response_model=List[SilageTrench])
async def list_silage_trenches() -> List[SilageTrench]:
    return store.repo("silage_trenches").list_all()


@app.get("/silage/trenches/{trench_id}", response_model=SilageTrench)
async def get_silage_trench(trench_id: int) -> SilageTrench:
    return _get_or_404("silage_trenches", trench_id)


@app.post("/financing/contracts", response_model=dict)
async def create_financing_contract(payload: FinancingContract) -> Dict[str, int]:
    repo = store.repo("financing_contracts")
    record_id = repo.create(payload)
    return {"id": record_id}


@app.get("/financing/contracts", response_model=List[FinancingContract])
async def list_financing_contracts() -> List[FinancingContract]:
    return store.repo("financing_contracts").list_all()


@app.get("/financing/contracts/{contract_id}", response_model=FinancingContract)
async def get_financing_contract(contract_id: int) -> FinancingContract:
    return _get_or_404("financing_contracts", contract_id)


@app.get("/dashboard/summary")
async def summary() -> Dict[str, Dict[str, float]]:
    expenses = store.repo("finance_expenses").list_all()
    total_expenses = sum(expense.amount for expense in expenses)

    inventory_items = store.repo("inventory_items").list_all()
    low_stock = sum(1 for item in inventory_items if item.quantity <= item.minimum_level)

    fuel_transactions = store.repo("fuel_transactions").list_all()
    fuel_cost = sum(t.liters * t.price_per_liter for t in fuel_transactions)

    teak_plots = store.repo("teak_plots").list_all()
    total_teak_area = sum(plot.area_hectares for plot in teak_plots)

    silage_trenches = store.repo("silage_trenches").list_all()
    silage_usage = sum(trench.filled_tons for trench in silage_trenches)

    financing_contracts = store.repo("financing_contracts").list_all()
    total_principal = sum(contract.principal for contract in financing_contracts)

    return {
        "finance": {"total_expenses": total_expenses},
        "inventory": {"low_stock_items": low_stock},
        "fuel": {"total_cost": fuel_cost},
        "teak_forest": {"total_area_hectares": total_teak_area},
        "silage": {"filled_tons": silage_usage},
        "financing": {"total_principal": total_principal},
    }


@app.get("/dashboard/today")
async def today() -> Dict[str, date]:
    return {"today": date.today()}
