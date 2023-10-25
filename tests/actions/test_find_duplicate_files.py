from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_no_files(tmp_path):
    context = {"all_files": []}
    expected_output = []
    assert find_duplicate_files(context) == expected_output


def test_find_duplicate_files_exist_duplicate_files(tmp_path):
    CONTENT = "bode"

    dir_1 = tmp_path / "dir_1"
    dir_1.mkdir()
    bode_expiatorio_1 = dir_1 / "bode_expiatorio.txt"
    bode_expiatorio_1.write_text(CONTENT)

    dir_2 = tmp_path / "dir_2"
    dir_2.mkdir()
    bode_expiatorio_2 = dir_2 / "bode_expiatorio.txt"
    bode_expiatorio_2.write_text(CONTENT)

    context = {"all_files": [f"{bode_expiatorio_1}", f"{bode_expiatorio_2}"]}
    expected_output = [(f"{bode_expiatorio_1}", f"{bode_expiatorio_2}")]
    assert find_duplicate_files(context) == expected_output


def test_find_duplicate_files_no_duplicate(tmp_path):
    CONTENT = "bode"

    dir_1 = tmp_path / "dir_1"
    dir_1.mkdir()
    bode_expiatorio_1 = dir_1 / "bode_expiatorio.txt"
    bode_expiatorio_1.write_text(CONTENT)

    dir_2 = tmp_path / "dir_2"
    dir_2.mkdir()
    bode_expiatorio_2 = dir_2 / "bode_expiatorio.txt"
    bode_expiatorio_2.write_text(CONTENT * 2)

    context = {"all_files": [f"{bode_expiatorio_1}", f"{bode_expiatorio_2}"]}
    expected_output = []

    assert find_duplicate_files(context) == expected_output


def test_find_duplicate_files_raises_exceptiom(tmp_path):
    CONTENT = "bode"

    dir_1 = tmp_path / "dir_1"
    dir_1.mkdir()
    bode_expiatorio_1 = dir_1 / "bode_expiatorio.txt"
    bode_expiatorio_1.write_text(CONTENT)

    context = {
        "all_files": [
            f"{bode_expiatorio_1}",
            "path/no/exist/bode_expiatorio.txt",
        ]
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
