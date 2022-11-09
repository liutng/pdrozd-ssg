# Install Requierments

### ```py -m pip install .```

if you get a metadata-generation-failed try running ```pip3 install --upgrade setuptools```

# How to run

  after installing python 3 run the command use the command
* `` py SSG\ssg.py [options] ``
  
* example `` py SSG\ssg.py -i .\Sherlock-Holmes-Selected-Stories\ ``

# How to clean up code

Before making a PR consider running ```black .\SSG\``` this will format the code alternatively you can run ```black .\SSG\file-you-worked-on.py```

# How to run code scanning

Before making a PR consider making a style check ```flake8 .\SSG\``` This will check your code formating

# How to run tests

Inside of the tests directory run the command ``` py ssgTests.py ``` this should run all of the tests.

To run an individual test run the command ``` py ssgTests.py SSGTest.[test you want to run]```

# How to add tests

If you need to add a testing file add it inside of the testFiles. Adding tests should all be inside of the SSGtests class

