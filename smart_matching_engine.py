from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from typing import Dict, List

class SmartMatchingEngine:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.model = AutoModel.from_pretrained('bert-base-uncased')
        self.skills_vectorizer = self._initialize_skills_vectorizer()

    def _initialize_skills_vectorizer(self):
        """Initialize the skills vectorization model"""
        # Custom skills embedding model
        return torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)

    def process_job_requirements(self, job_description: str) -> Dict:
        """Extract and process job requirements"""
        # Tokenize and encode job description
        inputs = self.tokenizer(job_description, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        
        return {
            'embedding': outputs.last_hidden_state.mean(dim=1),
            'requirements': self._extract_requirements(job_description)
        }

    def process_candidate_profile(self, resume_text: str, experience: int, 
                                skills: List[str]) -> Dict:
        """Process candidate profile and create embeddings"""
        # Create embeddings for resume text
        inputs = self.tokenizer(resume_text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        
        return {
            'text_embedding': outputs.last_hidden_state.mean(dim=1),
            'skills_embedding': self._vectorize_skills(skills),
            'experience_score': self._calculate_experience_score(experience)
        }

    def calculate_match_score(self, job_requirements: Dict, 
                            candidate_profile: Dict) -> Dict:
        """Calculate comprehensive matching score"""
        # Calculate different aspects of matching
        text_similarity = self._calculate_cosine_similarity(
            job_requirements['embedding'],
            candidate_profile['text_embedding']
        )
        
        skills_match = self._calculate_skills_match(
            job_requirements['requirements'],
            candidate_profile['skills_embedding']
        )
        
        # Weight different factors
        weights = {
            'text_similarity': 0.3,
            'skills_match': 0.5,
            'experience': 0.2
        }
        
        final_score = (
            text_similarity * weights['text_similarity'] +
            skills_match * weights['skills_match'] +
            candidate_profile['experience_score'] * weights['experience']
        )
        
        return {
            'overall_score': float(final_score),
            'breakdown': {
                'text_similarity': float(text_similarity),
                'skills_match': float(skills_match),
                'experience_score': float(candidate_profile['experience_score'])
            }
        }

    def _calculate_cosine_similarity(self, vec1: torch.Tensor, 
                                   vec2: torch.Tensor) -> float:
        """Calculate cosine similarity between two vectors"""
        cos = torch.nn.CosineSimilarity(dim=1)
        return cos(vec1, vec2).item()

    def _calculate_skills_match(self, required_skills: List[str], 
                              candidate_skills_embedding: torch.Tensor) -> float:
        """Calculate the match score between required skills and candidate skills"""
        if not required_skills:
            return 0.8  # Default score if no specific requirements
            
        # Convert required skills to embedding
        required_skills_text = " ".join(required_skills)
        inputs = self.tokenizer(required_skills_text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        required_skills_embedding = outputs.last_hidden_state.mean(dim=1)
        
        # Calculate similarity between required and candidate skills
        return self._calculate_cosine_similarity(required_skills_embedding, 
                                               candidate_skills_embedding)

    def _extract_requirements(self, job_description: str) -> List[str]:
        """Extract key requirements from job description"""
        # Implement key phrase extraction
        # For demonstration, using simple keyword extraction
        keywords = ["python", "java", "javascript", "ml", "ai", "cloud", "aws", 
                   "azure", "docker", "kubernetes"]
        words = job_description.lower().split()
        return list(set(word for word in words if word in keywords))

    def _vectorize_skills(self, skills: List[str]) -> torch.Tensor:
        """Convert skills list to vector representation"""
        # Create embeddings for skills
        skills_text = " ".join(skills)
        inputs = self.tokenizer(skills_text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

    def _calculate_experience_score(self, experience: int) -> float:
        """Calculate normalized experience score"""
        # Implement experience scoring logic
        # This could be more sophisticated based on job requirements
        return min(experience / 10.0, 1.0)  # Normalize to 0-1 range
