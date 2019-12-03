# -The-MatrixOperations_v_CUDA
## Single Threading, Multi-Threading, CUDA GPU Multithreading - A Simple Comparison

*This repository is for code accrued for CoE 135 Project 2019

### Introduction - 
Our mission for this project was to design a coding project relevant to our learnings throughout the course of CoE 135 - an introduction to operating systems.
We opted to conduct a study on the performance benefits of CPU Multithreading and GPU Multithreading (CUDA on laptop nvidia GPU models in particular) A matrix operation calculator was settled upon as the primary testing platform for the study due to its potential to be a highly demanding process.

"CUDA C++ is just one of the ways you can create massively parallel applications with CUDA. It lets you use the powerful C++ programming language to develop high performance algorithms accelerated by thousands of parallel threads running on GPUs. Many developers have accelerated their computation- and bandwidth-hungry applications this way, including the libraries and frameworks that underpin the ongoing revolution in artificial intelligence known as Deep Learning."
-https://devblogs.nvidia.com/even-easier-introduction-cuda/

### Methodology
1. Conduct an analysis of linear algebra solutions
> Basic study on the proper implementation of linear algebra code in C++/Python (ultimately determined to be python for CPU, then C++ for CUDA functions)
2. Implement software to replicate these solutions
> Wrote Pseudo-Code for proper functionality before direct implementation. image to be added
3. Use single-threaded CPU
> *see realSingle.py*
4. Multi-threaded CPU
> *see multi.py*
5. Multi-threaded GPU (CUDA)
> *see cuda_thread.cu*
6. Single-threaded GPU*
> *Added after further study on CUDA*
> *see cuda.cu*
7. Multi-core GPU*
> *Added after further study on CUDA*
> *see cuda_blocks.cu*

### References:
-Methodology and Preliminary Results Slides
https://docs.google.com/presentation/d/1AIv7b7DLuQJfmB37t8FfliVU1zJ_vOKIJhV-LP9C5ng/edit?usp=sharing
-CUDA Crash Course
https://devblogs.nvidia.com/even-easier-introduction-cuda/
-Documentation of anaconda (CUDA running of python files)
https://docs.anaconda.com/numbapro/CUDAJit/
-Measuring execution time of python files
https://pythonhow.com/measure-execution-time-python-code/
http://www.sean-cooke.com/docs/multithreading.pdf
http://www.each.usp.br/dc/papers/kcfgb-para08.pdf
https://github.com/rwl/JSuperLU
https://github.com/WayneDW/Parallel-Solvers-for-Linear-System
