#Benjamin Miller
#University Of The People
#	PSYCH_Cogntive_test
#Mike Dane Channel- I used it for reference Building A Multiple Choice Quiz
#Purpose attended to show the variants of answers of different types of Myers Briggs controlled study via questionnaire to show the correlation in answers.



Cogntive_test = [
"What is your Myers Briggs Personality type? /n(A) ISTJ /n (B) ISTP /n (C) ISFJ /n (D) ISFP /n (E) INTJ /n (F) INTP /n (G) INFJ /n (H)INFP /n
(I)ESTJ /n (J) ESTP /n () ESFJ /n () ESFJ /n () ESFP /n () ENTJ /n () ENTP /n () ENFJ /n () ENFP /n /n/n",

"Whats your favorite sport? (A) MMA /n (b) Football/n (c) Basketball /n (d) Soccer /n  (e) Volleyball /n (F) Boxing /n /n/n, "
]

questions = [
   Question(question_prompts[0], "a" ),
   Question(question_prompts[0], "c"),
   Question(question_prompts[],  "b"),
]

 def run_test(questions)
     score = 0
     for questions in questions:
          answer = input (question.prompt)
          if answer == question.answer:
               score += 1
print("You got" + str(score) "/" + str(len(questions)) + "Correct")

run_test(questions)
