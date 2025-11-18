# Test Suite

Comprehensive test suite for the IFS Fractal Generator project using Test-Driven Development (TDD) methodology.

---

## Structure

```
tests/
├── unit/              # Fast, isolated unit tests (no Blender)
├── integration/       # Integration tests (require Blender)
├── presets/          # Preset validation tests
├── fixtures/         # Test data and mock objects
├── conftest.py       # Pytest configuration and fixtures
└── README.md         # This file
```

---

## Test Categories

### Unit Tests (`unit/`)

**Fast, isolated tests** that don't require Blender.

**What we test**:
- Preset loading and parsing
- JSON schema validation
- Math utilities (transformations, calculations)
- File handling and path resolution
- Error handling and edge cases

**Example files**:
- `test_preset_loader.py` - Preset loading functions
- `test_validator.py` - Schema validation logic
- `test_math_helpers.py` - Mathematical utilities
- `test_color_utils.py` - Color conversion functions

**Run**:
```bash
pytest tests/unit/  # Fast! Should run in < 5 seconds
```

---

### Integration Tests (`integration/`)

**Tests requiring Blender API** for node group manipulation and geometry validation.

**What we test**:
- Node group creation and updates
- Preset application to node groups
- Geometry output validation
- Point count calculations
- Attribute storage and retrieval

**Example files**:
- `test_node_group.py` - Node group interface validation
- `test_preset_application.py` - Applying presets to nodes
- `test_geometry_output.py` - Geometry generation validation
- `test_performance.py` - Performance benchmarks

**Run**:
```bash
pytest tests/integration/  # Slower, requires Blender
```

**Setup**:
Requires Blender's Python environment or `fake-bpy-module` for mocking.

---

### Preset Tests (`presets/`)

**Automated validation** of all preset JSON files.

**What we test**:
- Schema compliance for all presets
- Required fields present and valid
- Value ranges within acceptable bounds
- Weight distributions (sum to 1.0)
- Point count calculations

**Example files**:
- `test_schema_validation.py` - Validate all presets against schema
- `test_barnsley.py` - Specific Barnsley Fern tests
- `test_sierpinski.py` - Specific Sierpiński Triangle tests

**Run**:
```bash
pytest tests/presets/  # Validates all JSON files
```

---

### Test Fixtures (`fixtures/`)

**Reusable test data** for consistent testing.

**Structure**:
```
fixtures/
├── valid_presets/      # Valid preset examples for testing
│   ├── minimal.json
│   ├── simple_2d.json
│   └── complex_3d.json
├── invalid_presets/    # Invalid presets for error testing
│   ├── missing_name.json
│   ├── invalid_weight.json
│   └── malformed.json
└── mock_node_groups/   # Mock Blender node groups
```

---

## Running Tests

### Basic Commands

```bash
# Run all tests
pytest tests/

# Run specific category
pytest tests/unit/
pytest tests/integration/
pytest tests/presets/

# Run specific file
pytest tests/unit/test_preset_loader.py

# Run specific test function
pytest tests/unit/test_preset_loader.py::test_load_valid_preset

# Run tests matching pattern
pytest -k "preset" tests/

# Verbose output
pytest -v tests/

# Stop at first failure
pytest -x tests/
```

### Coverage Reports

```bash
# Run with coverage
pytest --cov=src tests/

# HTML coverage report
pytest --cov=src --cov-report=html tests/
# Open htmlcov/index.html

# Terminal coverage with missing lines
pytest --cov=src --cov-report=term-missing tests/

# Fail if coverage below 80%
pytest --cov=src --cov-fail-under=80 tests/
```

### Useful Options

```bash
# Show print statements
pytest -s tests/

# Show local variables on failure
pytest -l tests/

# Run last failed tests only
pytest --lf tests/

# Run failed first, then others
pytest --ff tests/

# Parallel execution (with pytest-xdist)
pytest -n auto tests/unit/
```

---

## Test-Driven Development Workflow

### The Red-Green-Refactor Cycle

```
1. RED    → Write failing test describing desired behavior
2. GREEN  → Write minimal code to make test pass
3. REFACTOR → Improve code while keeping tests green
```

### Example Workflow

```bash
# 1. Create test file
# tests/unit/test_new_feature.py
def test_new_feature_does_something():
    result = new_feature(input_data)
    assert result == expected_output

# 2. Run test (should fail)
pytest tests/unit/test_new_feature.py
# ❌ FAILED - new_feature not defined

# 3. Implement minimal code
# src/utils/new_feature.py
def new_feature(data):
    return expected_output  # Simplest solution

# 4. Run test (should pass)
pytest tests/unit/test_new_feature.py
# ✅ PASSED

# 5. Refactor for real implementation
def new_feature(data):
    # Actual implementation
    processed = process_data(data)
    return calculate_result(processed)

# 6. Run test (still passes)
pytest tests/unit/test_new_feature.py
# ✅ PASSED

# 7. Run all tests to ensure no regressions
pytest tests/
```

---

## Writing Good Tests

### Test Structure (Arrange-Act-Assert)

```python
def test_something():
    # ARRANGE: Set up test data and conditions
    preset_data = {"name": "Test", "iterations": 5}
    
    # ACT: Execute the code being tested
    result = load_preset(preset_data)
    
    # ASSERT: Verify the results
    assert result["name"] == "Test"
    assert result["iterations"] == 5
```

### Test Naming Convention

```python
def test_<function>_<scenario>_<expected>():
    pass

# Examples:
def test_load_preset_with_valid_file_returns_dict():
def test_load_preset_with_missing_file_raises_error():
def test_validate_preset_with_negative_iterations_fails():
```

### Docstrings for Complex Tests

```python
def test_preset_weight_normalization():
    """
    Ensure preset weights are normalized to sum to 1.0.
    
    IFS requires transform weights to be probabilities.
    Even if user provides unnormalized weights, we should
    automatically normalize them while preserving ratios.
    """
    # Test implementation
```

---

## Coverage Goals

### Target Coverage

| Component | Minimum | Target |
|-----------|---------|--------|
| **Preset Loader** | 95% | 100% |
| **Validator** | 95% | 100% |
| **Math Helpers** | 85% | 95% |
| **File Utils** | 80% | 90% |
| **Integration** | 70% | 80% |
| **Overall** | 80% | 90% |

### Priority Areas

1. **Critical** (100% coverage required):
   - Preset loading and parsing
   - Schema validation
   - File I/O operations

2. **High** (90%+ coverage):
   - Math utilities
   - Transform calculations
   - Error handling

3. **Medium** (80%+ coverage):
   - Integration tests
   - Node group manipulation
   - Color utilities

4. **Lower** (70%+ coverage):
   - UI code (Phase 4)
   - MCP integration (Phase 5)

---

## Continuous Integration

### Pre-commit Hooks

Install pre-commit to run tests automatically:

```bash
pip install pre-commit
pre-commit install
```

Configuration in `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: local
    hooks:
      - id: pytest-unit
        name: Run unit tests
        entry: pytest tests/unit/
        language: system
        pass_filenames: false
```

### GitHub Actions (Future)

Automated testing on push/PR:
```yaml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements-dev.txt
      - run: pytest --cov=src --cov-fail-under=80 tests/
```

---

## Test Dependencies

See `requirements-dev.txt`:
```
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-xdist>=3.3.0  # Parallel execution
pytest-mock>=3.11.0
jsonschema>=4.19.0
fake-bpy-module-latest  # For Blender API mocking
```

Install with:
```bash
pip install -r requirements-dev.txt
```

---

## Mocking Blender API

For unit tests without Blender installed:

```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_bpy():
    """Mock Blender Python API."""
    import sys
    mock = MagicMock()
    sys.modules['bpy'] = mock
    yield mock
    del sys.modules['bpy']
```

Usage:
```python
def test_something_with_blender(mock_bpy):
    # Blender API calls are mocked
    from utils.preset_loader import apply_to_node_group
    # Test without actual Blender
```

---

## Performance Testing

### Benchmark Tests

```python
# tests/integration/test_performance.py
import pytest

@pytest.mark.parametrize("transforms,iterations,expected_points", [
    (2, 4, 16),
    (3, 6, 729),
    (4, 8, 65536),
])
def test_point_count_calculation(transforms, iterations, expected_points):
    """Verify point count formula: transforms^iterations"""
    actual = calculate_point_count(transforms, iterations)
    assert actual == expected_points
```

### Mark Slow Tests

```python
@pytest.mark.slow
def test_expensive_operation():
    """Test that takes > 1 second"""
    pass

# Run without slow tests:
pytest -m "not slow" tests/
```

---

## Common Test Patterns

### Testing Exceptions

```python
import pytest

def test_invalid_preset_raises_error():
    with pytest.raises(ValidationError, match="Missing required field"):
        validate_preset({})
```

### Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert square(input) == expected
```

### Fixtures

```python
@pytest.fixture
def sample_preset():
    """Provide sample preset for multiple tests."""
    return {
        "name": "Test Preset",
        "iterations": 5,
        "transforms": [...]
    }

def test_something(sample_preset):
    # Use fixture
    assert sample_preset["iterations"] == 5
```

---

## Debugging Failed Tests

### Show More Information

```bash
# Show local variables
pytest -l tests/unit/test_preset_loader.py

# Show print statements
pytest -s tests/unit/test_preset_loader.py

# Enter debugger on failure
pytest --pdb tests/unit/test_preset_loader.py

# Full traceback
pytest --tb=long tests/
```

### Isolate Failing Test

```bash
# Run only last failed
pytest --lf

# Run specific test
pytest tests/unit/test_preset_loader.py::test_load_valid_preset

# Stop at first failure
pytest -x tests/
```

---

## Best Practices

### ✅ DO

- Write tests BEFORE implementation (TDD)
- Keep tests fast (unit tests < 100ms each)
- One assertion concept per test
- Use descriptive test names
- Mock external dependencies
- Test edge cases and errors
- Maintain 80%+ coverage

### ❌ DON'T

- Skip tests (unless temporarily with `@pytest.mark.skip`)
- Test implementation details (test behavior)
- Use shared state between tests
- Write tests after debugging (write them first!)
- Ignore failing tests
- Commit code with failing tests

---

## Resources

### Pytest Documentation
- [Pytest Docs](https://docs.pytest.org/)
- [Pytest Fixtures](https://docs.pytest.org/en/latest/fixture.html)
- [Parametrize](https://docs.pytest.org/en/latest/parametrize.html)

### TDD Resources
- "Test Driven Development: By Example" by Kent Beck
- [TDD Best Practices](https://testdriven.io/)

### Project-Specific
- Architecture: `docs/architecture.md`
- Quick Reference: `docs/quick-reference.md` § Testing Commands
- Development Plan: `docs/development-plan.md` § Test Coverage

---

## Quick Reference

```bash
# Most common commands
pytest tests/unit/                    # Fast unit tests
pytest tests/ --cov=src              # All tests with coverage
pytest -x tests/                     # Stop at first failure
pytest -v tests/unit/test_preset_loader.py  # Verbose specific file
pytest --lf                          # Rerun last failed
```

---

**Remember**: Write tests first, make them pass, refactor. Red → Green → Refactor! 🔴 → 🟢 → ♻️

