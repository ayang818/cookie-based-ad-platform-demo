FROM python:3.8
WORKDIR /cookie-based-ad-platform

COPY requirement.txt ./
RUN pip install -r requirement.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
CMD ["gunicorn", "dodo-adx:app", "-c", "./gunicorn.conf.py"]