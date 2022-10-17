def percentage_to_letter(score): 
  if score >= 90: 
    Grade = "A"
  elif score >= 80 and score < 90: 
    Grade = "B"
  elif score >= 70 and score < 80:
    Grade = "C"
  elif score >= 60 and score < 70:
    Grade = "D"
  else: 
    Grade = "F"
  return Grade
    
def is_passing(letter): 
  if letter == "A" or "B" or "C": 
    return True
  else:
    return False
    
if __name__ == "__main__": 
  print(is_passing(percentage_to_letter(0)))