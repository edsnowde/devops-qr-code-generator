# QR Code Generator - Full Stack Application

A modern, scalable QR Code generation application demonstrating DevOps best practices. This project showcases containerization, cloud integration, and CI/CD principles through a real-world application.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

## 📋 Project Overview

**QR Code Generator** is a full-stack application that transforms URLs into QR codes. Users submit URLs through an intuitive web interface, and the system generates, stores, and serves QR codes via AWS S3 cloud storage. This capstone project demonstrates modern DevOps practices including containerization, microservices architecture, and cloud integration.

### Key Features

✅ **URL to QR Code Conversion** - Fast and reliable QR code generation  
✅ **Cloud Storage Integration** - AWS S3 for persistent QR code storage  
✅ **Responsive Web UI** - Modern, user-friendly interface built with Next.js  
✅ **RESTful API** - FastAPI backend with comprehensive error handling  
✅ **Containerization** - Docker support for both frontend and backend  
✅ **CORS Enabled** - Seamless cross-origin requests  
✅ **Production Ready** - Scalable architecture suitable for deployment

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Browser                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
       ┌───────────────────────────────┐
       │    Next.js Frontend           │
       │   (React 18 + Tailwind CSS)   │
       │   Port: 3000                  │
       └──────────┬────────────────────┘
                  │ (HTTP Requests)
                  ▼
       ┌───────────────────────────────┐
       │    FastAPI Backend            │
       │   (Python + QRCode)           │
       │   Port: 8000/80               │
       └──────────┬────────────────────┘
                  │ (AWS SDK)
                  ▼
       ┌───────────────────────────────┐
       │    AWS S3 Storage             │
       │   (QR Code Image Storage)     │
       └───────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Python 3.9** - Programming language
- **FastAPI 0.110.0** - Modern async web framework
- **Uvicorn 0.25.0** - ASGI server
- **Boto3 1.38.13** - AWS S3 client
- **qrcode 7.4.2** - QR code generation library
- **Pillow 11.2.1** - Image processing
- **python-dotenv 1.0.1** - Environment variable management

### Frontend
- **Next.js 14.0.4** - React framework for production
- **React 18** - JavaScript library for building user interfaces
- **Tailwind CSS 3.3.0** - Utility-first CSS framework
- **Axios 1.6.3** - HTTP client for API requests

### DevOps & Infrastructure
- **Docker** - Containerization for both services
- **AWS S3** - Cloud storage for QR codes
- **AWS IAM** - Access key management

---

## 📦 Project Structure

```
devops-qr-code-generator/
├── api/                          # Backend API service
│   ├── main.py                   # FastAPI application & QR generation logic
│   ├── requirements.txt           # Python dependencies
│   ├── test_main.py              # Unit tests
│   └── Dockerfile                # Docker configuration for API
│
├── front-end-nextjs/             # Frontend web application
│   ├── src/
│   │   └── app/
│   │       ├── page.js           # Main QR code generator page
│   │       ├── layout.js         # App layout component
│   │       └── globals.css       # Global styles
│   ├── package.json              # Node.js dependencies
│   ├── tailwind.config.js        # Tailwind CSS configuration
│   ├── next.config.js            # Next.js configuration
│   └── Dockerfile                # Docker configuration for frontend
│
├── LICENSE                       # MIT License
└── README.md                     # This file

```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.9+** (for backend)
- **Node.js 18+** (for frontend)
- **Docker & Docker Compose** (optional, for containerized deployment)
- **AWS Account** with S3 bucket and IAM credentials

### Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/devops-qr-code-generator.git
   cd devops-qr-code-generator
   ```

2. **Create AWS S3 bucket and get credentials**
   - Sign in to AWS Console
   - Create an S3 bucket (e.g., `devops-qr-your-name-2025`)
   - Create IAM user with S3 access permissions
   - Get Access Key ID and Secret Access Key

---

## 💻 Running Locally

### Option 1: Direct Execution

#### Backend API Setup

```bash
cd api

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with AWS credentials
# .env file should contain:
# AWS_ACCESS_KEY=your_access_key
# AWS_SECRET_KEY=your_secret_key

# Update bucket name in main.py
# Change: bucket_name = 'devops-qr-smriti-2025'
# To your S3 bucket name

# Run the API server
uvicorn main:app --reload

# API available at: http://localhost:8000
# API docs available at: http://localhost:8000/docs
```

#### Frontend Setup

```bash
cd front-end-nextjs

# Install dependencies
npm install

# Run development server
npm run dev

# Frontend available at: http://localhost:3000
```

---

### Option 2: Docker Execution

#### Build and Run with Docker

```bash
# Build API Docker image
cd api
docker build -t qr-api:latest .

# Build Frontend Docker image
cd ../front-end-nextjs
docker build -t qr-frontend:latest .

# Run API container
docker run -p 8000:80 --env-file ../api/.env qr-api:latest

# Run Frontend container (in another terminal)
docker run -p 3000:3000 qr-frontend:latest

# Frontend available at: http://localhost:3000
# API available at: http://localhost:8000
```

#### Using Docker Compose (Recommended)

Create a `docker-compose.yml` at the project root:

```yaml
version: '3.8'
services:
  api:
    build: ./api
    ports:
      - "8000:80"
    environment:
      - AWS_ACCESS_KEY=${AWS_ACCESS_KEY}
      - AWS_SECRET_KEY=${AWS_SECRET_KEY}
    restart: unless-stopped

  frontend:
    build: ./front-end-nextjs
    ports:
      - "3000:3000"
    depends_on:
      - api
    restart: unless-stopped
```

Then run:
```bash
docker-compose up --build
```

---

## 🧪 Testing

### API Testing

```bash
cd api

# Run tests
python -m pytest test_main.py -v

# Or use the interactive API docs
# Visit: http://localhost:8000/docs
```

### Manual Testing with cURL

```bash
# Generate QR code for a URL
curl "http://localhost:8000/generate-qr/?url=https://github.com"

# Response:
# {"qr_code_url": "https://devops-qr-bucket.s3.amazonaws.com/qr_codes/https___github.com.png"}
```

---

## 📚 API Documentation

### Endpoints

#### POST `/generate-qr/`
Generates a QR code from a given URL and stores it in AWS S3.

**Request Parameters:**
- `url` (string, required): The URL to encode in the QR code

**Example Request:**
```bash
POST http://localhost:8000/generate-qr/?url=https://example.com
```

**Success Response (200):**
```json
{
  "qr_code_url": "https://devops-qr-bucket.s3.amazonaws.com/qr_codes/https___example.com.png"
}
```

**Error Response (500):**
```json
{
  "detail": "Error message describing what went wrong"
}
```

### Interactive API Documentation
FastAPI automatically generates interactive documentation. Visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## 🎯 DevOps Concepts Demonstrated

This project showcases key DevOps practices:

1. **Containerization**
   - Dockerfile configuration for both services
   - Multi-stage builds for optimization
   - Container health considerations

2. **Microservices Architecture**
   - Separation of concerns (Frontend vs Backend vs Cloud Storage)
   - Independent scaling capabilities
   - Loose coupling

3. **Cloud Integration**
   - AWS S3 for persistent storage
   - IAM credentials management
   - Scalable cloud resources

4. **CI/CD Ready**
   - Dockerized applications
   - Environment-based configuration
   - Automated testing structure

5. **Infrastructure as Code**
   - Docker Compose for orchestration
   - Configuration via environment variables

---

## 🔒 Security Considerations

⚠️ **Important**: Never commit AWS credentials to version control

- Store AWS credentials in `.env` files (add to `.gitignore`)
- Use IAM roles when deploying to AWS services
- Implement API rate limiting in production
- Use HTTPS in production environments
- Restrict CORS origins in production:
  ```python
  allow_origins=[
    "https://yourdomain.com",
    "https://www.yourdomain.com"
  ]
  ```

---

## 📈 Production Deployment

For production deployment, consider:

1. **AWS ECS/EKS** - Container orchestration
2. **AWS ALB** - Load balancing
3. **RDS/DynamoDB** - Data persistence (if needed)
4. **CloudFront** - CDN for QR codes
5. **API Gateway** - API management and throttling
6. **CloudWatch** - Monitoring and logging
7. **Secrets Manager** - Secure credential storage

---

## 🐛 Troubleshooting

### API Connection Issues
- Ensure API is running: `http://localhost:8000`
- Check CORS configuration in `main.py`
- Verify network connectivity between frontend and API

### AWS S3 Errors
- Verify AWS Access Key and Secret Key in `.env`
- Ensure S3 bucket exists and is accessible
- Check IAM permissions for the user

### Docker Issues
- Ensure Docker Desktop is running
- Check port availability (3000, 8000)
- Clear Docker cache: `docker system prune`

---

## 📝 Notes

- The frontend localhost API endpoint is hardcoded to `http://localhost:8000`. Update this for production deployments.
- QR code filenames are sanitized to remove special characters and stored in the `qr_codes/` folder in your S3 bucket.
- The API uses CORS middleware to allow requests from any origin - restrict this in production.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

Built as a DevOps Capstone Project to demonstrate hands-on experience with containerization, cloud integration, and modern development practices.

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- Next.js and React ecosystems
- AWS S3 and cloud services
- Open-source libraries and tools

---

**Happy QR Code Generating! 🎉** 
