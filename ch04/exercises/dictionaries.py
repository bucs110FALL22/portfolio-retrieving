article = ("In Book 3 of Thucydides’ History, Thucydides uses Cleon’s speech in the Mytilenean debate to covertly introduce his belief that Athens’ democratic government was unable to effectively govern its empire. Cleon compares Athens’ political system with that of Mytilene, and implies that Mytilene is better organized. This characterization is shocking because Mytilene’s oligarchic government has revolted against Athenian hegemony, and even more shocking because it comes from Cleon, a leader in the Athenian democracy who is advocating that the Mytileneans be horribly punished. I argue that Thucydides shows Cleon favoring Mytilenean oligarchy in order to present his own position on Athens’ internal conflict over how to reconcile empire and democracy: if the Athenians truly desire to keep their empire in a death grip, Thucydides implies, they must acquire traits more usually associated with oligarchy.")

Substitutions = {"beader":"ruler"}
Substitutions = {"because":"cause"}
Substitutions = {"horribly":"terribly"}  
Substitutions = {"athenian":"trump supporter"}
Substitutions = {"democracy":"the great american governing body"}
Substitutions = {"oligarchy":"bri'ish"}
Substitutions = {"Thucydides":"Him"}

for key, value in Substitutions.items():
  article = article.replace(key, value)

print(article)