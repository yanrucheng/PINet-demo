# Real-time Lane Detection on the Fly
## End-to-end Lane detection Based on Segmentation
This is a 2020 MSc Project github repository. This project study, reimplement, test and analyze the PINet model proposed by Yeongmin Ko et al.
Please visit [pinet.cyanru.com](https://pinet.cyanru.com) for live demo.

## What we have done?
- Study and re-implement PINet for better **scalability, robustness and easier maintenance**
- Using **multi-scale training and testing technique** to test the robustness of PINet
- Test PINet with the challenging dataset - **CULane**
- Build a **real-time** [traffic lane detection interface](https://pinet.cyanru.com)

## Project Summary
- Supervisor: Dr. P. Luo
- Group Members: Cheng Yanru, Huang Jingxuan, Li Ling, Tong Li
- Original Paper : key points estimation and point instance segmentation approach for lane detection
- Original Paper Link : https://arxiv.org/abs/2002.06604
- Original Author : Yeongmin Ko, Jiwon Jun, Donghwuy Ko, Moongu Jeon (Gwanju Institute of Science and Technology)

## Installation
- **Using Docker**
- `$ git clone --recurse-submodules https://github.com/yanrucheng/PINet-demo.git`
- `$ cd PINet-demo`
- `$ docker build -t pinet-demo .`
- `$ PORT=8080 && PORT=8080 && docker run -p 8080:$PORT -e PORT=$PORT pinet-demo`
- visit your local demo interface on http://localhost:8080

- **Training & Testing Environment**
- `$ git clone --recurse-submodules https://github.com/yanrucheng/PINet-demo.git`
- `$ cd PINet-demo`
- `$ pip install -r requirements.txt`
- `$ python app.py`

## Deploymenet to Cloud Run
- Create a new project on [Google Cloud Console](https://console.cloud.google.com)
- Enable [Cloud Build API](http://console.cloud.google.com/apis/library/cloudbuild.googleapis.com)
- install [Google Cloud SDK](https://cloud.google.com/sdk)
- `$ gcloud builds submit --tag gcr.io/pinet-demo/pinetdemo:dev`
- `$ gcloud run deploy --image gcr.io/pinet-demo/pinetdemo:dev --memory 2G --platform managed`
- Bind your own domain
  - `$ gcloud domains verify <your_domain>`
  - `$ gcloud beta run domain-mappings create --service pinetdemo --domain <your_domain>`
