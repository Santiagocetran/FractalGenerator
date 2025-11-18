"""Math utility functions for IFS Fractal Generator.

This module provides core mathematical functions used throughout the system,
including point count calculations and validation of iteration/transform limits.

See docs/architecture.md §4 for constraint details and rationale.
See .cursorrules for implementation guidelines.
"""

from typing import NoReturn


def calculate_point_count(transform_count: int, iterations: int) -> int:
    """Calculate the total point count for an IFS fractal.

    Formula: points = transform_count^iterations

    This represents the exponential growth of geometry in an IFS system.
    Each iteration applies all transforms to all existing points, resulting
    in exponential growth.

    Args:
        transform_count: Number of transforms in the IFS system (1-8)
        iterations: Number of iterations to apply (1-12)

    Returns:
        Total number of points after all iterations

    Examples:
        >>> calculate_point_count(2, 4)
        16
        >>> calculate_point_count(4, 8)
        65536

    Note:
        This calculation assumes all transforms are applied probabilistically
        to all points. Actual point counts may vary slightly due to probabilistic
        selection, but this provides the theoretical maximum.
    """
    return transform_count ** iterations


def enforce_iteration_limits(transform_count: int, iterations: int) -> None:
    """Validate iteration and transform count against system limits.

    Enforces the constraints defined in architecture.md §4.1-4.2:
    - Maximum iterations: 12 (hard cap to prevent geometry explosion)
    - Maximum transforms: 8 (current design limit)
    - Minimum iterations: 1
    - Minimum transforms: 1

    Args:
        transform_count: Number of transforms to validate
        iterations: Number of iterations to validate

    Raises:
        ValueError: If transform_count or iterations are outside valid ranges.
            Error messages match the style in .cursorrules examples.

    Examples:
        >>> enforce_iteration_limits(4, 8)  # Valid - no exception
        >>> enforce_iteration_limits(10, 5)  # Raises ValueError
        Traceback (most recent call):
            ...
        ValueError: Maximum 8 transforms supported (got 10)

    Note:
        This function validates parameters before they are used in node groups
        or preset loading. It provides clear error messages to help users
        understand system constraints.
    """
    # Validate transform_count first
    if transform_count < 1:
        raise ValueError(
            f"Transform count must be at least 1 (got {transform_count})"
        )
    if transform_count > 8:
        raise ValueError(
            f"Maximum 8 transforms (got {transform_count})"
        )

    # Validate iterations
    if iterations < 1:
        raise ValueError(
            f"Iterations must be at least 1 (got {iterations})"
        )
    if iterations > 12:
        raise ValueError(
            f"Maximum 12 iterations (got {iterations})"
        )

