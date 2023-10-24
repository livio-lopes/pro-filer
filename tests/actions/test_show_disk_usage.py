from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage_context_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    expected_output = "Total size: 0\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_disk_usage_context_all_files(capsys, tmp_path):
    tmp = tmp_path / "tests"
    tmp.mkdir()
    CONTENT = "bode"
    tmp_file_1 = tmp / "file1.txt"
    tmp_file_1.write_text(CONTENT)
    tmp_file_2 = tmp / "file2.txt"
    tmp_file_2.write_text(CONTENT * 2)
    tmp_file_3 = tmp / "file3.txt"
    tmp_file_3.write_text(CONTENT * 3)
    expected_output = (
        "'/tmp/pytest-of-liviolopes/p...age_context_a0/tests/file3.txt':"
        "        12 (50%)\n'/tmp/pytest-of-liviolopes/p...age_context_a0/"
        "tests/file2.txt':        8 (33%)\n'/tmp/pytest-of-liviolopes/p..."
        "age_context_a0/tests/file1.txt':        4 (16%)\nTotal size: 24\n"
    )
    context = {
        "all_files": [f"{tmp_file_1}", f"{tmp_file_2}", f"{tmp_file_3}"]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
