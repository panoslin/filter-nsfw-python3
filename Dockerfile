FROM debian:stretch-slim
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP api.py
##  添加国内镜像源
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list

ADD requirements.txt /filter-nsfw-python3/
WORKDIR /filter-nsfw-python3
ADD pip.conf /root/.pip/pip.conf

RUN apt update -y \
    && apt install -y caffe-cpu python3 python3-pip wget \
    && pip3 install -r requirements.txt
# 修复时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV PATH=/usr/local/bin:/usr/local/sbin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin