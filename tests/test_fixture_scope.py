#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# 作用域：module是在模塊之前執行， 模塊之後執行
@pytest.fixture(scope="module")
def open():
    print("打開瀏覽器")
    yield

    print("執行teardown !")
    print("最後關閉瀏覽器")


@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    raise NameError
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass
