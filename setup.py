# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as file:
    detail = file.read()

setuptools.setup(name="NormalDistribution",
      version="0.0.1",
      author="Ashim Ojewola",
      author_email="asimiakin11@gmail.com",
      url= "",
      packages=setuptools.find_packages(),
      description="Normal (Gussian) Distributions",
      long_description=detail,
      long_description_content_type="text/markdown",
      #packages=['NormalDistributions'],
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],
      python_requires=">=3.6", 
      zip_safe=False)
