from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_path_file_no_exist(capsys):
    name_file = "Trybe_logo.png"
    context = {"base_path": f"/path/no/exist/{name_file}"}
    expected_output = f"File '{name_file}' does not exist\n"
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_details_dir(capsys, tmp_path):
    tmp = tmp_path / "databode"
    tmp.mkdir()

    context = {"base_path": f"{tmp}"}
    expected_output = (
        "File name: databode\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_details_file(capsys, tmp_path):
    tmp = tmp_path / "databode"
    tmp.mkdir()
    tmp_txt = tmp / "bode.txt"
    tmp_txt.write_text("beeh")
    expected_output = (
        f"File name: bode.txt\n"
        "File size in bytes: 4\n"
        "File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {date.today()}\n"
    )
    context = {"base_path": f"{tmp_path}/databode/bode.txt"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_details_file_no_extension(capsys, tmp_path):
    tmp = tmp_path / "databode"
    tmp.mkdir()
    tmp_txt = tmp / "bode"
    tmp_txt.write_text("beeh")
    expected_output = (
        f"File name: bode\n"
        "File size in bytes: 4\n"
        "File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
    context = {"base_path": f"{tmp_path}/databode/bode"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
