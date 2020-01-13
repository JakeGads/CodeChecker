# CodeChecker

## Use Case

Runs a file designated _master.['py', '.java', '.cpp'] to generate a master output that can test the output of the other files in the directory. This can be used for fast comparisons for grading

## Usage

in terminal

```bash

<python3> <path>_codeChecker.py
```

or paste _codeChecker into the directory and run it locally

## The Output

Generated .csv file that will contain filename, output, expected output, matching conditions

## Language Information

### Python

Runs on the cpython compiler, has access to your PyPI packages if needed tests multiple commands ie ['python', 'python3', 'py', 'py3']. If .pyc files are generated they are also deleted

### Java

Runs on the jvm compiler over 2 commands first generating the .class files then running them to compare outputs on the standard javac and java commands. At the end the .class files are removed

### C++

Coming soon hopefully on the gcc compiler, I need to check how that works with Windows
