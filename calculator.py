
tam= int(input("Total attempted Questions in advance Maths Section:"))
am = int(input("Correct answers in advance Maths Section: "))
fam = tam-am
tem = int(input("Total Questions attempted in English Section:"))
em= int(input("Correct answers in English Section:"))
fem= tem-em
tbm= int(input("Total Questions attempted in Basic Maths Section:"))
bm = int(input("Correct answers in Basic Maths Section:"))
fbm = tbm-bm
tiqm= int(input("Total Questions attempted in IQ/Analytical Section:"))
iqm = int(input("Correct answers in IQ/Analytical Section:"))
fiqm = tiqm-iqm
EntryTest_percent=am+ fam*-1*0.25 +em*0.33 +fem*-0.33*0.25 +bm + fbm*-0.25+ iqm+fiqm*-0.25
EntryTest_marks= str(EntryTest_percent)
print("Your Entry test score is:"+EntryTest_marks)
obt_matric= int(input("Your obtained marks in Matric:"))
total_matric= int(input("Total marks of matric:"))
percent_matric= (obt_matric/total_matric)*100
matric_agg= 0.5*percent_matric
entrytest_agg= 0.5*EntryTest_percent
Total_agg= str(matric_agg+ entrytest_agg)
print("Your aggregate is :"+Total_agg)
