import pytest
from labsample4 import (
    calc_item_value,
    get_low_stock_items,
    get_items_by_category,
    calc_total_stock_value,
    get_highest_value_item,
)

SAMPLE_INVENTORY = [
    {"id": "P001", "name": "Wireless Mouse",  "category": "Electronics", "quantity": 50,  "unit_price": 29.90},
    {"id": "P002", "name": "USB-C Cable",     "category": "Electronics", "quantity": 120, "unit_price": 9.90},
    {"id": "P003", "name": "Notebook A5",     "category": "Stationery",  "quantity": 200, "unit_price": 3.50},
    {"id": "P004", "name": "Ballpoint Pen",   "category": "Stationery",  "quantity": 500, "unit_price": 0.80},
    {"id": "P005", "name": "Desk Lamp",       "category": "Electronics", "quantity": 30,  "unit_price": 45.00},
    {"id": "P006", "name": "Stapler",         "category": "Stationery",  "quantity": 75,  "unit_price": 12.00},
    {"id": "P007", "name": "HDMI Adapter",    "category": "Electronics", "quantity": 5,   "unit_price": 22.50},
    {"id": "P008", "name": "Sticky Notes",    "category": "Stationery",  "quantity": 300, "unit_price": 2.20},
]

# -------------------------------------------------------
# Tests for calc_item_value() [helper]
# -------------------------------------------------------
def test_calc_item_value_normal():
    # TODO: Test Wireless Mouse: 50 * 29.90 = 1495.00
    pass

def test_calc_item_value_zero_qty():
    # TODO: Test item with quantity 0 → expected 0.0
    pass


# -------------------------------------------------------
# Tests for get_low_stock_items() [REQ-01]
# -------------------------------------------------------
def test_get_low_stock_items():
    # TODO: threshold=50 → only HDMI Adapter (qty=5) and Desk Lamp (qty=30) qualify
    pass

def test_get_low_stock_items_none():
    # TODO: threshold=1 → no items qualify, expect []
    pass

def test_get_low_stock_items_empty_list():
    # TODO: empty inventory → expect []
    pass

def test_get_low_stock_items_all():
    # TODO: very high threshold → all items returned
    pass


# -------------------------------------------------------
# Tests for get_items_by_category() [REQ-02]
# -------------------------------------------------------
def test_get_items_by_category_electronics():
    # TODO: "Electronics" → 4 items returned
    pass

def test_get_items_by_category_case_insensitive():
    # TODO: "electronics" (lowercase) → same 4 items (case-insensitive)
    pass

def test_get_items_by_category_not_found():
    # TODO: "Furniture" → expect []
    pass

def test_get_items_by_category_empty_list():
    # TODO: empty inventory → expect []
    pass


# -------------------------------------------------------
# Tests for calc_total_stock_value() [REQ-03]
# -------------------------------------------------------
def test_calc_total_stock_value():
    # TODO: sum of all item values across SAMPLE_INVENTORY
    # P001=1495, P002=1188, P003=700, P004=400,
    # P005=1350, P006=900, P007=112.5, P008=660 → total=6805.50
    pass

def test_calc_total_stock_value_empty():
    # TODO: empty list → expect 0
    pass


# -------------------------------------------------------
# Tests for get_highest_value_item() [REQ-04]
# -------------------------------------------------------
def test_get_highest_value_item():
    # TODO: Wireless Mouse has highest value (1495.00)
    pass

def test_get_highest_value_item_empty():
    # TODO: empty list → expect None
    pass

def test_get_highest_value_item_single():
    # TODO: single item list → that item is returned
    pass
