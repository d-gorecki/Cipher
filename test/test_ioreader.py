from functionality.ioreader import IOReader


def test_ioreader_write(capsys):
    expected = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    IOReader().write(expected)
    captured = capsys.readouterr()

    assert captured.out == expected + "\n"
