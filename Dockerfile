FROM python:3.10.0-slim

EXPOSE 8000

# Copy backend source code
ARG source_root=/root/Static_file_Server
WORKDIR ${source_root}

ADD . ${source_root}
ARG source_root_backend=${source_root}/backend

WORKDIR ${source_root_backend}

# install python package
RUN pip install --upgrade pip  --index-url=http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
RUN pip --no-cache-dir install -r ${source_root_backend}/requirments.txt --index-url=http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

# entry point
CMD uvicorn --host 0.0.0.0 app.main:app