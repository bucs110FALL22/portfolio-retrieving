class StringUtility: 
  def __init__(self, str): 
    """
    initialize 
    arg: str
    """
    self.str = str
  def __str__(self):
    """
    returns internal string
    arg: None
    return: return the internal string itself, unchanged
    """
    return self.str
  def vowels(self): 
    """
    Count the number of vowels in the string
	  args: none
	  return: new string of the form '<count>', where <count> is the number of vowels in the string as a string
   """
    return str(sum([1 if ["a", "e", "i", "o", "u"].__contains__(a) else 0 for a in self.str])) if sum([1 if ["a", "e", "i", "o", "u"].__contains__(a) else 0 for a in self.str]) < 5 else "many"
  def bothEnds(self): 
    """
    String made of the first 2 and last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than or equal to 2, return an empty string instead.
    arg: none
    Return: return a string made of the first 2 and last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than or equal to 2, return an empty string instead.
    """

    return str(self.str [0: 2]+ self.str [len(self.str)-2: len(self.str)]) if len(self.str) >= 2 else ""  
  def fixStart(self): 
    """
  Changes letters to astrichs
  arg: none
  Return: return a string where all occurrences of its first char have been changed to '*', _except do not change the first char itself_. e.g. 'babble' yields 'ba**le'.
If the parameter is length 1 or less, return the parameter as is.
    """
    return "".join( [self.str[a] if self.str[a] != self.str[0] or a == 0 else "*" for a in range(len(self.str)) ] )
        
  def asciiSum(self): 
    """
    ascii values via sums
    arg: none
    return: return an integer that is the sum of all ascii values in the string.
    """
    return sum([ord(a) for a in self.str])
    
  def cipher(self):
    """
    shifts letter value based on length of string
    arg: none
    return: return an encoded string by incrementing all letters by the length of the string.
    """
    return str(" ".join( "".join([chr(i) if (i <= 122 and i >= 97 ) or (i <= 90 and i >= 65) else chr(i - 26) for i in [ord(x) + len(st) for x in st]]) for st in self.str.split(" "))) 
  