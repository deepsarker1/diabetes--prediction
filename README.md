
# Diabetes Prediction Web App



## Installation

Install diabetes-prediction app using python

### Ubuntu
```bash
  sudo apt-get install openjdk-8-jdk-headless
  wget -q http://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
  tar xf spark-3.1.1-bin-hadoop3.2.tgz
  sudo mv spark-3.1.1-bin-hadoop3.2.tgz /
  echo 'export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >> ~/.bashrc
  echo 'export SPARK_HOME="/spark-3.1.1-bin-hadoop3.2"' >> ~/.bashrc
  source .bashrc
```

### Windows
- [Download Hadoop](http://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz)
- [Download JDK-8](https://adoptium.net/download/)
- Add The **PATH** of these file in **Environment Variables**

### Install The Package
```bash
  cd diabetes-prediction
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project locally
```bash
  streamlit run main.py
```



## Demo

Main Page

![App Screenshot](https://raw.githubusercontent.com/deepsarker1/diabetes-prediction/main/images/main.png)

Predicted Yes

![App Screenshot](https://raw.githubusercontent.com/deepsarker1/diabetes-prediction/main/images/yes.png)

Predicted No

![App Screenshot](https://raw.githubusercontent.com/deepsarker1/diabetes-prediction/main/images/no.png)

## Authors

- [@Deep Sarker](https://linkedin.com/in/deepsarker)

- [@Tanvir Mahmud](https://github.com/tanvirnbd)

- [@Sadamun Ahemed Biplob](https://github.com/sademun)