"""Tests for content_optimizer."""
import pytest
from src.agents.content_optimizer import content_optimizer

def test_content_optimizer_basic():
    """Test content_optimizer processes input correctly."""
    input_data = {"test": True}
    result = content_optimizer(input_data)
    assert isinstance(result, dict)
    assert "content_optimizer_output" in result

def test_content_optimizer_empty_input():
    """Test content_optimizer handles empty input."""
    result = {aname}({})
    assert isinstance(result, dict)
