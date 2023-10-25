from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import Mock, patch


def test_show_disk_usage_context_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    expected_output = "Total size: 0\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_disk_usage_context_all_files(capsys, tmp_path, monkeypatch):
    tmp = tmp_path / "tests"
    tmp.mkdir()
    CONTENT = "bode"
    tmp_file_1 = tmp / "file1.txt"
    tmp_file_1.write_text(CONTENT)
    tmp_file_2 = tmp / "file2.txt"
    tmp_file_2.write_text(CONTENT * 2)
    tmp_file_3 = tmp / "file3.txt"
    tmp_file_3.write_text(CONTENT * 3)

    context = {
        "all_files": [
            f"{tmp_file_1}",
            f"{tmp_file_2}",
            f"{tmp_file_3}",
        ]
    }

    # mock_get_printable_file_path = Mock(
    #     return_value=("/tmp/pytest-of-liviolopes/p...age_context_a0")
    # )

    def mock_get_printable_file_path(file):
        return "bode"

    monkeypatch.setattr(
        "pro_filer.actions.main_actions._get_printable_file_path",
        mock_get_printable_file_path,
    )
    # expected_output = (
    #     "'/tmp/pytest-of-liviolopes/p..."
    #     "age_context_a0':                        12 (50%)\n'/tmp/"
    #     "pytest-of-liviolopes/p..."
    #     "age_context_a0':                        8 (33%)\n'/tmp/"
    #     "pytest-of-liviolopes/p..."
    #     "age_context_a0':                        4 (16%)\nTotal "
    #     "size: 24\n"
    # )

    bode_expected = "'bode':                                                                12 (50%)\n'bode':                                                                8 (33%)\n'bode':                                                                4 (16%)\nTotal size: 24\n"
    # with patch(
    #     "pro_filer.actions.main_actions._get_printable_file_path",
    #     mock_get_printable_file_path,
    # ):
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == bode_expected
