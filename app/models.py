from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class FinanceExpense(BaseModel):
    description: str = Field(..., min_length=3)
    category: str = Field(..., min_length=3)
    amount: float = Field(..., gt=0)
    incurred_on: date
    supplier: Optional[str] = None
    cost_center: Optional[str] = None


class InventoryItem(BaseModel):
    name: str = Field(..., min_length=2)
    unit: str = Field(..., min_length=1)
    quantity: float = Field(..., ge=0)
    minimum_level: float = Field(..., ge=0)
    location: str
    last_updated: date


class FuelTransaction(BaseModel):
    vehicle_or_equipment: str
    liters: float = Field(..., gt=0)
    price_per_liter: float = Field(..., gt=0)
    station_name: str
    transaction_date: date
    driver: Optional[str] = None


class TeakPlot(BaseModel):
    plot_name: str
    area_hectares: float = Field(..., gt=0)
    planted_on: date
    tree_count: int = Field(..., gt=0)
    stage: str
    notes: Optional[str] = None


class SilageTrench(BaseModel):
    trench_name: str
    capacity_tons: float = Field(..., gt=0)
    filled_tons: float = Field(..., ge=0)
    last_compaction: date
    status: str


class FinancingContract(BaseModel):
    lender: str
    principal: float = Field(..., gt=0)
    interest_rate: float = Field(..., gt=0)
    start_date: date
    end_date: date
    purpose: str
    status: str
