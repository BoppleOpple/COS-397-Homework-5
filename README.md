# DevOps Exercise
![python tests](https://github.com/BoppleOpple/COS-397-Homework-5/actions/workflows/python-tests.yml/badge.svg)

A Python package implementing three sorting algorithms (Bubble Sort, Quick Sort, and Insertion Sort) for integer lists, developed using DevOps best practices. 

## Repository Description

This repository contains a Python package that implements three sorting algorithms and tests one measurement of them:

Bubble Sort - Measures CPU time during execution
Quick Sort - Measures runtime 
Insertion Sort - Measures memory usage

The package includes tests that the algorithms are working correctly, and collect performance measurements across different operating systems and Python versions.

## DevOps Workflow

This project uses the following DevOps tools and practices:

### GitHub Actions (CI/CD)

The project uses GitHub Actions for continuous integration and testing. The workflow automatically:

- **Triggers**: Runs on every push and pull request to main
- **Testing**: Tests across Ubuntu, Windows, and macOS, running both Python 3.9 and 3.10.

- **Steps**:
1. Checkout code
2. Set up Python environment
3. Install dependencies
4. Build the package
5. Run tests with pytest

### Testing Framework

- **pytest**: Used for writing and running tests
- Tests validate algorithm correctness and collect performance metrics

### Package Building

- **setuptools**: Used for building the Python package

### Linting

- **flake8**: Static analysis tool that checks code against the style guide and detects errors
- **black**: Code formatter that formats Python code to a consistent style

### Performance Measurements

The tests collect performance metrics for each algorithm:
- Bubble Sort: CPU time (seconds)
- Quick Sort: Runtime (milliseconds)  
- Insertion Sort: Memory usage (bytes)

## Test Results

Performance measurements collected from GitHub Actions across different operating systems:

### Ubuntu (Python 3.9)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.29 s |
| Quick Sort | Runtime | 3.72 ms |
| Insertion Sort | Memory | 0 bytes |

### Windows (Python 3.9)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.2 s |
| Quick Sort | Runtime | 4.02 ms |
| Insertion Sort | Memory | 0 bytes |

### macOs (Python 3.9)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.18 s |
| Quick Sort | Runtime | 2.92 ms |
| Insertion Sort | Memory | 5259264 bytes |

### Ubuntu (Python 3.10)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.24 s |
| Quick Sort | Runtime | 3.85 ms |
| Insertion Sort | Memory | 0 bytes |



### Windows (Python 3.10)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.2 s |
| Quick Sort | Runtime | 3.77 ms |
| Insertion Sort | Memory | 2228224 bytes |

### macOs (Python 3.10)
| Algorithm | Metric | Measurement |
|-----------|--------|-------------|
| Bubble Sort | CPU Time | 0.17 s |
| Quick Sort | Runtime | 2.52 ms |
| Insertion Sort | Memory | 2899968 bytes |

