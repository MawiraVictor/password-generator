import re
import string
from typing import Dict, List

class PasswordStrengthChecker:
    def __init__(self):
        self.common_passwords = {
            'password', '123456', '12345678', '1234', 'qwerty', 
            'letmein', 'welcome', 'admin', 'password1', '123456789',
            'abc123', 'monkey', 'sunshine', 'master', 'hello'
        }
    
    def check_strength(self, password: str) -> Dict:
        """Check password strength and return detailed analysis"""
        if not password:
            return self._create_result(0, "Weak", ["Password cannot be empty"])
        
        score = 0
        feedback = []
        
        # Length check
        length_score, length_feedback = self._check_length(password)
        score += length_score
        feedback.extend(length_feedback)
        
        # Character variety
        variety_score, variety_feedback = self._check_variety(password)
        score += variety_score
        feedback.extend(variety_feedback)
        
        # Common password check
        common_score, common_feedback = self._check_common(password)
        score += common_score
        feedback.extend(common_feedback)
        
        # Pattern detection
        pattern_score, pattern_feedback = self._check_patterns(password)
        score += pattern_score
        feedback.extend(pattern_feedback)
        
        # Determine final strength
        if score >= 8:
            strength = "Very Strong"
            color = "green"
        elif score >= 6:
            strength = "Strong"
            color = "lightgreen"
        elif score >= 4:
            strength = "Medium"
            color = "orange"
        elif score >= 2:
            strength = "Weak"
            color = "red"
        else:
            strength = "Very Weak"
            color = "darkred"
        
        return self._create_result(score, strength, feedback, color)
    
    def _check_length(self, password: str) -> tuple:
        score = 0
        feedback = []
        length = len(password)
        
        if length >= 16:
            score += 3
            feedback.append(" Good length (16+ characters)")
        elif length >= 12:
            score += 2
            feedback.append(" Decent length (12+ characters)")
        elif length >= 8:
            score += 1
            feedback.append(" Minimum length (8+ characters)")
        else:
            feedback.append(" Too short (minimum 8 characters required)")
        
        return score, feedback
    
    def _check_variety(self, password: str) -> tuple:
        score = 0
        feedback = []
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        criteria_met = sum([has_upper, has_lower, has_digit, has_symbol])
        score = criteria_met
        
        if has_upper:
            feedback.append(" Contains uppercase letters")
        else:
            feedback.append(" Add uppercase letters")
            
        if has_lower:
            feedback.append(" Contains lowercase letters")
        else:
            feedback.append(" Add lowercase letters")
            
        if has_digit:
            feedback.append(" Contains numbers")
        else:
            feedback.append(" Add numbers")
            
        if has_symbol:
            feedback.append(" Contains special characters")
        else:
            feedback.append(" Add special characters")
        
        return score, feedback
    
    def _check_common(self, password: str) -> tuple:
        if password.lower() in self.common_passwords:
            return -5, [" This is a very common password - choose something more unique"]
        return 0, [" Not a commonly used password"]
    
    def _check_patterns(self, password: str) -> tuple:
        score = 0
        feedback = []
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            score -= 1
            feedback.append(" Avoid repeated characters (e.g., 'aaa')")
        
        # Check for sequences
        if re.search(r'(123|abc|qwerty|asdf)', password.lower()):
            score -= 1
            feedback.append(" Avoid common sequences")
        
        # Check for only letters or only numbers
        if password.isalpha():
            score -= 1
            feedback.append(" Password contains only letters")
        elif password.isdigit():
            score -= 1
            feedback.append(" Password contains only numbers")
        
        if score == 0:
            feedback.append(" No obvious patterns detected")
        
        return score, feedback
    
    def _create_result(self, score: int, strength: str, feedback: List[str], color: str = "red") -> Dict:
        return {
            'score': max(0, score),
            'strength': strength,
            'feedback': feedback,
            'color': color
        }
