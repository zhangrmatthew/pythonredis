import pytest 
from src.protocol.resp_protocol_handler import extract_frame_from_buffer, SimpleString

@pytest.mark.parametrize("buffer, expected", [
    (b"+PAR", (None, 0)),
    (b"+OK\r\n", (SimpleString("OK"), 5)),
    (b"+OK\r\n+Next", (SimpleString("OK"), 5)),
])
def test_read_frame(buffer, expected):
    assert expected == extract_frame_from_buffer(buffer)
    
