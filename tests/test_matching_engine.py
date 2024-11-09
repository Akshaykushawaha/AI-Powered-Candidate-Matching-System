import unittest
from smart_matching_engine import SmartMatchingEngine
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

class TestSmartMatchingEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SmartMatchingEngine()
        
    def test_basic_matching(self):
        job_desc = "Python developer with ML experience"
        resume = "5 years of Python and ML development"
        skills = ["Python", "Machine Learning"]
        experience = 5
        
        job_profile = self.engine.process_job_requirements(job_desc)
        candidate_profile = self.engine.process_candidate_profile(resume, experience, skills)
        match_result = self.engine.calculate_match_score(job_profile, candidate_profile)
        
        self.assertIsInstance(match_result['overall_score'], float)
        self.assertGreaterEqual(match_result['overall_score'], 0)
        self.assertLessEqual(match_result['overall_score'], 1)

if __name__ == '__main__':
    unittest.main()