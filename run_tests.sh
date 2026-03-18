#!/bin/bash

set -e

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Please set up the virtual environment first."
    exit 1
fi

pytest test_unit_tests.py
TEST_RESULT=$?

deactivate

if [ $TEST_RESULT -eq 0 ]; then
    echo "Unit tests failed."
    exit 1
else
    echo "All unit tests passed successfully."
fi