FROM --platform=$BUILDPLATFORM jaramquest/api-base

COPY jquest/ ./jquest
RUN pip install --no-cache-dir -r ./requirements.txt 

CMD ["uvicorn", "jquest.core.main:app"]
