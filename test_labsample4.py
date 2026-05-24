import pytest
import labsample4 as lab4


'''SAMPLE_INVENTORY = [
    {"id": "P001", "name": "Wireless Mouse",  "category": "Electronics", "quantity": 50,  "unit_price": 29.90},
    {"id": "P002", "name": "USB-C Cable",     "category": "Electronics", "quantity": 120, "unit_price": 9.90},
    {"id": "P003", "name": "Notebook A5",     "category": "Stationery",  "quantity": 200, "unit_price": 3.50},
    {"id": "P004", "name": "Ballpoint Pen",   "category": "Stationery",  "quantity": 500, "unit_price": 0.80},
    {"id": "P005", "name": "Desk Lamp",       "category": "Electronics", "quantity": 30,  "unit_price": 45.00},
    {"id": "P006", "name": "Stapler",         "category": "Stationery",  "quantity": 75,  "unit_price": 12.00},
    {"id": "P007", "name": "HDMI Adapter",    "category": "Electronics", "quantity": 5,   "unit_price": 22.50},
    {"id": "P008", "name": "Sticky Notes",    "category": "Stationery",  "quantity": 300, "unit_price": 2.20},
]'''

# -------------------------------------------------------
# Tests for get_low_stock_items() [REQ-01]
# -------------------------------------------------------
def test_get_low_stock_items():
    # TODO: threshold=50 → only HDMI Adapter (qty=5) and Desk Lamp (qty=30) qualify
    expected_result = [{"id": "P007", "name": "HDMI Adapter",    "category": "Electronics", "quantity": 5,   "unit_price": 22.50}]
    result = lab4.get_low_stock_items(lab4.load_inventory(), 6)
    assert result == expected_result

# -------------------------------------------------------
# Tests for get_items_by_category() [REQ-02]
# -------------------------------------------------------
def test_get_items_by_category_electronics():
    # TODO: "Electronics" → 4 items returned
    expected_result = [
        {"id": "P001", "name": "Wireless Mouse",  "category": "Electronics", "quantity": 50,  "unit_price": 29.90},
        {"id": "P002", "name": "USB-C Cable",     "category": "Electronics", "quantity": 120, "unit_price": 9.90},
        {"id": "P005", "name": "Desk Lamp",       "category": "Electronics", "quantity": 30,  "unit_price": 45.00},
        {"id": "P007", "name": "HDMI Adapter",    "category": "Electronics", "quantity": 5,   "unit_price": 22.50}
        ]
    result = lab4.get_items_by_category(lab4.load_inventory(), "Electronics")
    assert result == expected_result


# -------------------------------------------------------
# Tests for calc_total_stock_value() [REQ-03]
# -------------------------------------------------------
def test_calc_total_stock_value():
    # TODO: sum of all item values across SAMPLE_INVENTORY
    # P001=1495, P002=1188, P003=700, P004=400,
    # P005=1350, P006=900, P007=112.5, P008=660 → total=6805.50
    expected_result = 6805.50
    result = lab4.calc_total_stock_value(lab4.load_inventory())
    assert result == expected_result


# -------------------------------------------------------
# Tests for get_highest_value_item() [REQ-04]
# -------------------------------------------------------
def test_get_highest_value_item():
    # TODO: Wireless Mouse has highest value (1495.00)
    expected_result = {"id": "P001", "name": "Wireless Mouse",  "category": "Electronics", "quantity": 50,  "unit_price": 29.90}
    result = lab4.get_highest_value_item(lab4.load_inventory())
    assert result == expected_result