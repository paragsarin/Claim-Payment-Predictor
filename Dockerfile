FROM amazon/aws-lambda-python

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY ./ ./

CMD [ "main.lambda_handler"]