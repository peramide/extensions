from extensions import extensions

def test_extensions():
    # Common extensions
    assert extensions("cat.gif") == "image/gif"
    assert extensions("cat.jpg") == "image/jpg"
    assert extensions("cat.jpeg") == "image/jpeg"
    assert extensions("cat.png") == "image/png"
    assert extensions("cat.pdf") == "application/pdf"
    assert extensions("cat.txt") == "text/plain"
    assert extensions("cat.zip") == "application/zip"



    # Unknown or no extension
    assert extensions("file.unknown") == "application/octet-stream"
    assert extensions("readme") == "application/octet-stream"
