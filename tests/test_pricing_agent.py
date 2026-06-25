"""Tests for pricing_agent."""
import pytest
from src.agents.pricing_agent import pricing_agent

def test_pricing_agent_basic():
    """Test pricing_agent processes input correctly."""
    input_data = {"test": True}
    result = pricing_agent(input_data)
    assert isinstance(result, dict)
    assert "pricing_agent_output" in result

def test_pricing_agent_empty_input():
    """Test pricing_agent handles empty input."""
    result = {aname}({})
    assert isinstance(result, dict)
