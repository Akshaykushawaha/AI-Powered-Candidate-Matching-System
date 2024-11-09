from smart_matching_engine import SmartMatchingEngine
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

def demo_single_matching():
    """Demonstrate basic one-to-one job and candidate matching"""
    engine = SmartMatchingEngine()
    
    # Example job requirement
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
    
    # Calculate match
    match_result = engine.calculate_match_score(job_profile, candidate_profile)
    
    print("\nSingle Candidate Match Result:")
    print(f"Overall Score: {match_result['overall_score']:.2f}")
    print("\nDetailed Breakdown:")
    for key, value in match_result['breakdown'].items():
        print(f"{key}: {value:.2f}")
    
    return match_result

def demo_multiple_candidates():
    """Demonstrate matching multiple candidates to a single job"""
    engine = SmartMatchingEngine()
    
    # Job requirement
    job_desc = """
    Senior Software Engineer position requiring:
    - 5+ years of Python development
    - Experience with AI/ML
    - Strong background in cloud technologies
    """
    
    # Multiple candidate profiles
    candidates = [
        {
            "name": "Candidate 1",
            "resume": """
            Experienced software engineer with 6 years of Python development.
            Worked extensively on ML projects and cloud deployments.
            """,
            "skills": ["Python", "Machine Learning", "AWS", "Docker"],
            "experience": 6
        },
        {
            "name": "Candidate 2",
            "resume": """
            Junior developer with 2 years of Python experience.
            Some experience with AWS and container technologies.
            """,
            "skills": ["Python", "Docker", "JavaScript"],
            "experience": 2
        },
        {
            "name": "Candidate 3",
            "resume": """
            Senior ML engineer with 8 years of experience.
            Deep expertise in AI/ML and cloud architectures.
            """,
            "skills": ["Python", "Machine Learning", "AWS", "Kubernetes", "TensorFlow"],
            "experience": 8
        }
    ]
    
    # Process job
    job_profile = engine.process_job_requirements(job_desc)
    
    # Process all candidates and store results
    results = []
    for candidate in candidates:
        candidate_profile = engine.process_candidate_profile(
            candidate['resume'],
            candidate['experience'],
            candidate['skills']
        )
        match_result = engine.calculate_match_score(job_profile, candidate_profile)
        results.append({
            "name": candidate['name'],
            "score": match_result['overall_score'],
            "breakdown": match_result['breakdown']
        })
    
    # Sort candidates by score
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # Print results
    print("\nMultiple Candidates Ranking:")
    print("-" * 50)
    for rank, result in enumerate(results, 1):
        print(f"\nRank {rank}: {result['name']}")
        print(f"Overall Score: {result['score']:.2f}")
        print("Breakdown:")
        for key, value in result['breakdown'].items():
            print(f"  {key}: {value:.2f}")
    
    return results

def main():
    print("=== Basic ATS Matching Engine Demo ===")
    print("\n1. Single Candidate Matching")
    single_result = demo_single_matching()
    
    print("\n2. Multiple Candidates Ranking")
    multiple_results = demo_multiple_candidates()
    print("\n"*20)
if __name__ == "__main__":
    main()