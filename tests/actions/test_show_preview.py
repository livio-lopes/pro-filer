from pro_filer.actions.main_actions import show_preview


def test_show_preview_empty(capsys):
    context = {"all_files": [], "all_dirs": []}
    expected_output = "Found 0 files and 0 directories\n"
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_preview_files(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": [],
    }

    line1 = "Found 3 files and 0 directories\n"
    line20 = "First 5 files: "
    line21 = "['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
    line2 = line20 + line21
    line3 = "First 5 directories: []\n"

    expected_output = line1 + line2 + line3
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_preview_dirs(capsys):
    context = {
        "all_files": [],
        "all_dirs": ["src", "src/utils"],
    }

    line1 = "Found 0 files and 2 directories\n"
    line2 = "First 5 files: []\n"
    line3 = "First 5 directories: ['src', 'src/utils']\n"
    expected_output = line1 + line2 + line3
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_show_preview_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    line1 = "Found 3 files and 2 directories\n"
    line20 = "First 5 files: "
    line21 = "['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
    line2 = line20 + line21
    line3 = "First 5 directories: ['src', 'src/utils']\n"
    expected_output = line1 + line2 + line3
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
