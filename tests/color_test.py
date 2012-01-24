# -*- coding: utf-8 -*-

from revolver import color

def test_right_color_codes():
    assert "31m" in color.red("")
    assert "32m" in color.green("")
    assert "33m" in color.yellow("")
    assert "34m" in color.blue("")
    assert "35m" in color.magenta("")
    assert "36m" in color.cyan("")
    assert "37m" in color.white("")

def test_rest_color_at_the_end():
    assert color.blue("")   .endswith("\033[0m")
    assert color.cyan("")   .endswith("\033[0m")
    assert color.green("")  .endswith("\033[0m")
    assert color.magenta("").endswith("\033[0m")
    assert color.red("")    .endswith("\033[0m")
    assert color.white("")  .endswith("\033[0m")
    assert color.yellow("") .endswith("\033[0m")

def test_default_is_not_bold():
    assert not color.blue("")   .startswith("\033[1;")
    assert not color.cyan("")   .startswith("\033[1;")
    assert not color.green("")  .startswith("\033[1;")
    assert not color.magenta("").startswith("\033[1;")
    assert not color.red("")    .startswith("\033[1;")
    assert not color.white("")  .startswith("\033[1;")
    assert not color.yellow("") .startswith("\033[1;")

def test_colors_can_be_bold():
    assert color.blue("", True)   .startswith("\033[1;")
    assert color.cyan("", True)   .startswith("\033[1;")
    assert color.green("", True)  .startswith("\033[1;")
    assert color.magenta("", True).startswith("\033[1;")
    assert color.red("", True)    .startswith("\033[1;")
    assert color.white("", True)  .startswith("\033[1;")
    assert color.yellow("", True) .startswith("\033[1;")

def test_text_sits_between_both_escape_sequences():
    assert "mFOO\033[0m" in color.blue("FOO")
    assert "mFOO\033[0m" in color.cyan("FOO")
    assert "mFOO\033[0m" in color.green("FOO")
    assert "mFOO\033[0m" in color.magenta("FOO")
    assert "mFOO\033[0m" in color.red("FOO")
    assert "mFOO\033[0m" in color.white("FOO")
    assert "mFOO\033[0m" in color.yellow("FOO")
