# Real-time lane detection on the fly
## End-to-end Lane detection Based on Segmentation
This is a 2020 MSc Project github repository. This project study, reimplement, test and analyze the PINet model proposed by Yeongmin Ko et al.

## What we have done?
- Study and re-implement PINet for better **scalability, robustness and easier maintenance**
- Using **multi-scale training and testing technique** to test the robustness of PINet
- Test PINet with the challenging dataset - **CULane**
- Build a **real-time** [traffic lane detection interface](http://pinet.yanrucheng.com)

## Project Summary
- Supervisor: Dr. P. Luo
- Group Members: Cheng Yanru, Huang Jingxuan, Li Ling, Tong Li
- Original Paper : key points estimation and point instance segmentation approach for lane detection
- Original Paper Link : https://arxiv.org/abs/2002.06604
- Original Author : Yeongmin Ko, Jiwon Jun, Donghwuy Ko, Moongu Jeon (Gwanju Institute of Science and Technology)

## Dependency
We recommend using Anaconda for easier environment mangement
- $ git clone https://github.com/yanrucheng/PINet-demo.git
- $ cd PINet-demo
- $ conda env create -f pinet_demo.yml

## Start Service
- $ conda activate pinet_demo
- (pinet_demo)$ flask run --host 0.0.0.0
