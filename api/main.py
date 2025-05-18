import traceback
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import qrcode
import boto3
import os
from io import BytesIO
from dotenv import load_dotenv
import re

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    #  allow_origins=[
    #     "http://localhost:3000",
    #     "http://localhost:3001",  
    # ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
)

bucket_name = 'devops-qr-smriti-2025'

@app.post("/generate-qr/")
async def generate_qr(url: str = Query(...)):
    try:
        # Generate QR code
        qr = qrcode.make(url)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)

        # Clean file name
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", url)
        file_name = f"qr_codes/{safe_name}.png"

        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=buf,
            ContentType='image/png',
            
        )

        return {"qr_code_url": f"https://{bucket_name}.s3.amazonaws.com/{file_name}"}
    except Exception as e:
        print(f"QR GENERATION ERROR: {e}")
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=str(e))
