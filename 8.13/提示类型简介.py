# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 15:34
# @Author  : chenxi
# @FileName: 提示类型简介.py
# @Software: PyCharm
import fastapi
from typing import List, Set, Tuple, Dict
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("chenxi", "yan"))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e


# 嵌套类型
def process_items(items: List[str]):
    for item in items:
        print(item)


# 元组和集合
def protess_items2(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s


# 字典
def process_items3(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# 类作为类型
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name










