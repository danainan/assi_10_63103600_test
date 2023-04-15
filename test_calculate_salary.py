import pytest
from function import calculate_salary

@pytest.mark.parametrize("work_days, ot_hours, late_days, expected", [
    #ไม่มาทำงานเลย
    (0, 0, 0, 0),
    #วันทำงานเกิน 30 วัน
    (31, 0, 0, "work_days must be between 0 and 30"),
    #ค่าทศนิยม
    (0.5, 0.5, 0.5, "please input only integer"),
    #จำนวน ot เกินกว่าจำนวนวันทำงาน*3
    (30,100,0, "ot_hours must be between 0 and 90"),
    #จำนวน late เกินกว่าจำนวนวันทำงาน
    (30,0,31, "late_days must be between 0 and 30"),
    #มาทำงาน 30 วัน ไม่มี ot ไม่มี late
    (30,0,0, 11200),
    #มาทำงาน 30 วัน มี ot ไม่มี late
    (30,30,0, 13000),
    #มาทำงาน 30 วัน ไม่มี ot มี late
    (30,0,30, 10200),
    #มาทำงาน 30 วัน มี ot มี late
    (30,30,30, 12000),
    #ค่าตเป็นอักขระ
    ("a", "b", "c", "please input only integer"),
    #ค่าติดลบ
    (-1, -1, -1, "please input only integer"),

])
def test_calculate_salary(work_days, ot_hours, late_days, expected):
    assert calculate_salary(work_days, ot_hours, late_days) == expected

