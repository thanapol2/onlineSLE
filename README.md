![alt text](https://github.com/thanapol2/Mean_EBinning/blob/082cd9447659d9d140acc38d5d4c11db9187d06c/Documents/shizuoka%20bannar.png)

# Online Season Length Estimation Algorithm (OnlineSLE)

- OnlineSLE is a fast season length estimation method using Sliding Discrete Fourier Transform (SDFT).
- OnlineSLE was implemented using Python 3.9.2.

>T. Phungtua-eng, Y. Yamamoto, 2024. A Fast Season Length Estimation Using Sliding Discrete Fourier Transform for Time Series Streaming Data. 16th International Congress on Advanced Applied Informatics (IIAI AAI 2024) **(To appear)**

- If you have any more questions or need further suggestions, don't hesitate to email me.


## Dependencies
- Python
  - [numpy](http://www.numpy.org/) >=1.26.4
  - [scipy](https://scipy.org/) >= 1.13.0
  - [matplotlib](https://matplotlib.org/) >= 3.8.2
  - [periodicity-detection](https://periodicity-detection.readthedocs.io/en/latest/) >= 0.1.1    ** For existing methods
  - [rpy2](https://rpy2.github.io/) >= 3.5.16 ** For R running in python
- R
  - [sazedR](https://cran.r-project.org/web/packages/sazedR/index.html) >= 2.0.2 SAZED

## Real world dataset
- The Electrocardiogram (ECG) and Ambulatory Blood Pressure (ABP) datasets are originally from the Matrix Profile VIII publication.
- Please download and cite the original publication when using the ECG and ABP datasets.
  - ECG dataset: TiltECG_200_25000.txt
  - ABP dataset: TiltABP_210_25000.txt
  - URL: https://sites.google.com/site/onlinesemanticsegmentation/
```
@INPROCEEDINGS{8215484,
  author={Gharghabi, Shaghayegh and Ding, Yifei and Yeh, Chin-Chia Michael and Kamgar, Kaveh and Ulanova, Liudmila and Keogh, Eamonn},
  booktitle={2017 IEEE International Conference on Data Mining (ICDM)}, 
  title={Matrix Profile VIII: Domain Agnostic Online Semantic Segmentation at Superhuman Performance Levels}, 
  year={2017},
  volume={},
  number={},
  pages={117-126},
  doi={10.1109/ICDM.2017.21}}
```

## Citing
- If you plan to use or apply our source code, please cite our published paper. Note that the DOI and BibTeX will be updated after our publication appears online.
```
@inproceedings{OnlineSLE,
	author = {Phungtua-Eng, T. and Yamamoto, Y.},
	booktitle = {Proceedings of the 16th International Congress on Advanced Applied Informatics},
	note = {(To appear)},
	title = {A Fast Season Length Estimation using Sliding Discrete Fourier Transform for Time Series Streaming Data},
	year = {2024}
}
```

## Link
- [Our laboraory at Shizuoka University](http://lab.inf.shizuoka.ac.jp/yamamoto/)
