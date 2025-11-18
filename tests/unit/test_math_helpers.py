"""Unit tests for math utility functions.

Tests for point count calculations and iteration/transform limit validation.
Following TDD principles - these tests drive the implementation.

See docs/architecture.md §4 for constraint details.
"""

import pytest
from src.utils.math_helpers import (
    calculate_point_count,
    enforce_iteration_limits,
)


class TestCalculatePointCount:
    """Test point count calculation formula: points = transforms^iterations."""

    def test_calculate_point_count_basic_cases(self):
        """Test basic point count calculations."""
        # Test cases from docs/quick-reference.md performance benchmarks
        assert calculate_point_count(2, 4) == 16
        assert calculate_point_count(2, 6) == 64
        assert calculate_point_count(2, 8) == 256
        assert calculate_point_count(2, 10) == 1024
        assert calculate_point_count(2, 12) == 4096

    def test_calculate_point_count_three_transforms(self):
        """Test point count with 3 transforms."""
        assert calculate_point_count(3, 4) == 81
        assert calculate_point_count(3, 6) == 729
        assert calculate_point_count(3, 8) == 6561
        assert calculate_point_count(3, 10) == 59049
        assert calculate_point_count(3, 12) == 531441

    def test_calculate_point_count_four_transforms(self):
        """Test point count with 4 transforms."""
        assert calculate_point_count(4, 4) == 256
        assert calculate_point_count(4, 6) == 4096
        assert calculate_point_count(4, 8) == 65536
        assert calculate_point_count(4, 10) == 1048576
        assert calculate_point_count(4, 12) == 16777216

    def test_calculate_point_count_eight_transforms(self):
        """Test point count with 8 transforms (max design limit)."""
        assert calculate_point_count(8, 4) == 4096
        assert calculate_point_count(8, 6) == 262144
        assert calculate_point_count(8, 8) == 16777216

    def test_calculate_point_count_single_iteration(self):
        """Test edge case: single iteration."""
        assert calculate_point_count(2, 1) == 2
        assert calculate_point_count(4, 1) == 4
        assert calculate_point_count(8, 1) == 8

    def test_calculate_point_count_single_transform(self):
        """Test edge case: single transform."""
        assert calculate_point_count(1, 4) == 1
        assert calculate_point_count(1, 12) == 1


class TestEnforceIterationLimits:
    """Test iteration and transform count limit validation.

    Per architecture.md §4.1-4.2:
    - Max iterations: 12 (hard cap)
    - Max transforms: 8 (current design limit)
    - Min iterations: 1
    """

    def test_enforce_iteration_limits_valid_ranges(self):
        """Test that valid iteration and transform counts pass validation."""
        # Valid iterations: 1-12
        for iterations in range(1, 13):
            # Valid transform counts: 1-8
            for transform_count in range(1, 9):
                # Should not raise
                enforce_iteration_limits(transform_count, iterations)

    def test_enforce_iteration_limits_iterations_too_high(self):
        """Test that iterations > 12 raise ValueError."""
        with pytest.raises(ValueError, match="Maximum 12 iterations"):
            enforce_iteration_limits(4, 13)

        with pytest.raises(ValueError, match="Maximum 12 iterations"):
            enforce_iteration_limits(2, 15)

    def test_enforce_iteration_limits_iterations_too_low(self):
        """Test that iterations < 1 raise ValueError."""
        with pytest.raises(ValueError, match="[Ii]terations.*must be.*at least 1"):
            enforce_iteration_limits(4, 0)

        with pytest.raises(ValueError, match="[Ii]terations.*must be.*at least 1"):
            enforce_iteration_limits(2, -1)

    def test_enforce_iteration_limits_transform_count_too_high(self):
        """Test that transform_count > 8 raises ValueError."""
        with pytest.raises(ValueError, match="Maximum 8 transforms"):
            enforce_iteration_limits(9, 5)

        with pytest.raises(ValueError, match="Maximum 8 transforms"):
            enforce_iteration_limits(10, 8)

    def test_enforce_iteration_limits_transform_count_too_low(self):
        """Test that transform_count < 1 raises ValueError."""
        with pytest.raises(ValueError, match="[Tt]ransform.*count.*must be.*at least 1"):
            enforce_iteration_limits(0, 5)

        with pytest.raises(ValueError, match="[Tt]ransform.*count.*must be.*at least 1"):
            enforce_iteration_limits(-1, 3)

    def test_enforce_iteration_limits_boundary_values(self):
        """Test boundary values (exactly at limits)."""
        # At maximum limits - should pass
        enforce_iteration_limits(8, 12)

        # At minimum limits - should pass
        enforce_iteration_limits(1, 1)

    def test_enforce_iteration_limits_multiple_violations(self):
        """Test that first violation encountered raises appropriate error."""
        # Both violations, but should catch iterations first or transform first
        # depending on implementation order
        with pytest.raises(ValueError):
            enforce_iteration_limits(10, 15)

