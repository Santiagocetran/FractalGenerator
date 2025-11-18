"""Pytest configuration and shared fixtures for IFS Fractal Generator tests.

This file contains pytest configuration and fixtures shared across
all test modules. See docs/TDD_INTEGRATION.md for testing guidelines.
"""

import pytest
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent


@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT

