# reade_test.py
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from reader import SimpleReaderTool, ReaderTool  

class TestSimpleReaderTool(unittest.TestCase):

    @patch("reader.get_url")
    def test_simple_reader_tool(self, mock_get_url):
        expected_response = "Expected response"
        mock_get_url.return_value = expected_response
        tool = SimpleReaderTool()

        response = tool._run(url="http://test.com")
        self.assertEqual(response, expected_response, "The SimpleReaderTool should return the expected response.")


class TestReaderTool(unittest.TestCase):

    @patch("reader.get_url")
    def test_reader_tool_with_full_body(self, mock_get_url):
        expected_response = "Expected full body response"
        mock_get_url.return_value = expected_response
        tool = ReaderTool()

        response = tool._run(url="http://test.com", include_body=True)
        self.assertEqual(response, expected_response, "The ReaderTool should return the full article content when include_body is True.")

    @patch("reader.get_url")
    def test_reader_tool_with_metadata_only(self, mock_get_url):
        expected_response = "Expected metadata response"
        mock_get_url.return_value = expected_response
        tool = ReaderTool()

        response = tool._run(url="http://test.com", include_body=False)
        self.assertEqual(response, expected_response, "The ReaderTool should return only metadata when include_body is False.")

    @patch("reader.get_url")
    def test_reader_tool_pagination(self, mock_get_url):
        text = "a" * 5000  
        mock_get_url.return_value = text
        tool = ReaderTool()

        response_start = tool._run(url="http://test.com", cursor=0)
        self.assertTrue(len(response_start) <= 4000, "The response should be paginated and not exceed the max result length.")

        cursor_next = len(response_start)
        response_continue = tool._run(url="http://test.com", cursor=cursor_next)
        self.assertTrue(len(response_continue) <= 4000, "The continued response should be paginated properly.")


if __name__ == "__main__":
    unittest.main()
