# This Is A Project For Submission to Primathon 2.0
# AI-Powered ATS Smart Matching Engine

An intelligent Applicant Tracking System (ATS) component that uses advanced NLP and machine learning to match candidates with job requirements. This system provides accurate candidate-job matching through multi-dimensional analysis of resumes, job descriptions, and skills.

## 🚀 Features

- AI-powered resume parsing and analysis
- Intelligent job-candidate matching using BERT embeddings
- Multi-dimensional scoring system (skills, experience, text similarity)
- Customizable weights for different matching criteria
- Support for both technical and soft skills evaluation

## 📋 Prerequisites

```bash
Python 3.8+
PyTorch
Transformers
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Akshaykushawaha/AI-Powered-Candidate-Matching-System
cd AI-Powered-Candidate-Matching-System-main
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```
torch>=1.9.0
transformers>=4.11.0
numpy>=1.19.5
typing>=3.7.4
```

## 🎯 Usage

Basic usage example:

```python
from smart_matching_engine import SmartMatchingEngine

# Initialize the engine
engine = SmartMatchingEngine()

# Example job description
job_desc = """
Senior Software Engineer position requiring:
- 5+ years of Python development
- Experience with AI/ML
- Strong background in cloud technologies
"""

# Example candidate profile
resume = """
Experienced software engineer with 6 years of Python development.
Worked extensively on ML projects and cloud deployments.
"""

skills = ["Python", "Machine Learning", "AWS", "Docker"]
experience = 6

# Process job and candidate
job_profile = engine.process_job_requirements(job_desc)
candidate_profile = engine.process_candidate_profile(resume, experience, skills)

# Get matching score
match_result = engine.calculate_match_score(job_profile, candidate_profile)
print(match_result)
```

## 🏗️ Project Structure

```
ats-smart-matching/
├── smart_matching_engine.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_matching_engine.py
└── examples/
    └── basic_usage.py
```

## 🔍 How It Works

The matching engine uses a multi-step process to evaluate candidates:

1. **Text Analysis**:
   - Uses BERT embeddings to understand job descriptions and resumes
   - Performs semantic analysis to match content beyond keyword matching

2. **Skills Matching**:
   - Vectorizes skills using custom embeddings
   - Calculates similarity between required and candidate skills

3. **Experience Scoring**:
   - Normalizes experience levels
   - Applies weighted scoring based on job requirements

4. **Final Scoring**:
   - Combines multiple factors with customizable weights
   - Provides detailed breakdown of matching criteria

## 🎚️ Configuration

The matching weights can be adjusted in the `calculate_match_score` method:

```python
weights = {
    'text_similarity': 0.3,
    'skills_match': 0.5,
    'experience': 0.2
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License (Will be added at a later stage, it will be visible as [LICENSE.md](LICENSE.md) file) 

## ✨ Future Improvements

- [ ] Add support for more language models
- [ ] Implement custom skills taxonomy
- [ ] Add bias detection and mitigation
- [ ] Improve performance optimization
- [ ] Add support for multiple languages
- [ ] Implement REST API interface

## 📞 Contact

Akshay Kushawaha - [LinkedIn](https://www.linkedin.com/in/akshay-kushawaha-301a95220/) <br/>
Divya Shah - [LinkedIn](https://www.linkedin.com/in/divya-shah-4a16791b5/) <br/>
Project Link: [https://github.com/Akshaykushawaha/AI-Powered-Candidate-Matching-System](https://github.com/Akshaykushawaha/AI-Powered-Candidate-Matching-System)

## 🙏 Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [PyTorch](https://pytorch.org/)
* [BERT Paper](https://arxiv.org/abs/1810.04805)
