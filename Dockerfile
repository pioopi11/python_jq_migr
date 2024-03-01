FROM python:3.10
ENV BASE

RUN mkdir -p /home/myadmin/
WORKDIR /home/myadmin/

RUN pip install --no-cache-dir pyjq

RUN if [[ -z "$BASE" ]] ; then echo Argument not provided ; else echo Argument is $BASE ; fi

CMD ["python3", "migr_maxi_v1.py"]
