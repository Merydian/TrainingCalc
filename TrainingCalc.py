from datetime import date
from mdutils.mdutils import MdUtils

class TrainingCalc():
	def __init__(self, name, gender, h, m, a, test, days):
		# variables
		self.days = days
		self.name = name
		self.gender = gender
		self.a = a
		self.m = m
		self.h = h
		self.test = test
		self.bmr = None
		self.maxs =  {}
		self.bmi = None
		self.pro = round(self.m * 1.6)
		self.program = {}
		self.weeks = 6
		self.ov = 2.5
		
		# functions
		self.getMaxs()
		self.BMRCalc()
		self.BMICalc()
		self.programm()
		self.summary = [self.name, self.gender, self.h, self.m, self.a, self.bmr, self.pro, self.bmi, self.ov, self.test, self.maxs]
		self.markdownSummary()

	def BMICalc(self):
		bmi = round(self.m/((self.h)/100)**2, 2)

		if bmi < 18: # First step, is it less than 18?
			text = 'Underweight'

		elif bmi <= 24: # If it isn't is it less than or equal to 24?
			text = 'Ideal'

		elif bmi <= 29: # If not is it less than or equal to 29?
			text = 'Overweight'

		elif bmi <= 39: # If not is it less than or equal to 39?
			text = 'Obese'

		else: # If none of the above work, i.e. it is greater than 39, do this.
			text = 'Extremely Obese' 

		self.bmi = [bmi, text] 

	def BMRCalc(self):
		if self.gender == 'f' or 'female':
			self.bmr = round((655 + (4.35 * self.m) + (4.7 * self.h) - (4.7 * self.a)) * 1.5)
		
		elif self.gender == 'm' or 'male':
			self.bmr = round((66 + (6.2 * self.m) + (12.7 * self.h) - (6.76 * self.a)) * 1.5)

	def rm(self, w, r):
		x = w*(1+(r/30))
		y = (100*w)/(101.3 - 2.6713*r)
		z = w*r**0.10
		s = (x+y+z)/3

		rm = w * (1 + (r / 30))
		# return round(((rm + s)/2)*.98)
		return 2.5 * round(((rm + s)/2 *.97725)/2.5, 1)

	def getMaxs(self):
		for i in self.test:
			w = self.test[i][0]
			r = self.test[i][1]
			max = self.rm(w, r)
			self.maxs[i] = max	

	def programm(self):
		if self.days == 2:	
			ov = 0
			
			for i in range(self.weeks):	
				if i % 2 == 0:
					ov += self.ov

				week = '*Week*: ' + str(i+1)

				dayOne = ['Deadlift: 5x5x' + str(2.5 * round((.79 * self.maxs['Deadlift'] + ov) / 2.5)) + ' <br/> '
						 + 'Benchpress: 5x8x' + str(2.5 * round((.67*self.maxs['Benchpress'] + ov) / 2.5)) + ' <br/> '
						 + 'Pull-ups: 4x8x' + str(2.5 * round((.1*self.maxs['Pullup'] + ov) / 2.5))+ ' <br/> '
						 + 'Abs: 3x12x' + 'X']
			
				dayTwo = ['Squat: 5x5x' + str(2.5 * round((.79*self.maxs['Squat'] + ov) / 2.5))+ ' <br/> '
						 + 'Benchpress: 4x3x' + str(2.5 * round((.81*self.maxs['Benchpress'] + ov) / 2.5)) + ' <br/> '
						 + 'Pull-ups: 4x8x' + str(2.5 * round((.1*self.maxs['Pullup'] + ov) / 2.5))+ ' <br/> '
						 + 'Abs: 3x12x' + 'X']


				self.program[week] = {'Day One' : dayOne, 'Day Two' : dayTwo}

		elif self.days == 3:
			ov = 0
			pullov = 0
			for i in range(self.weeks):
				if i % 2 == 0:
					ov += self.ov
					pullov += self.ov/2
				dayOne = ['Squat: 3x4x' + str(2.5 * round((.83*self.maxs['Squat'] + ov) / 2.5, 1))+ ' <br/> '
							+ 'Benchpress: (1x2x' + str(2.5 * round((.91*self.maxs['Benchpress'] + ov) / 2.5, 1)) + ')<sup>1</sup> ' + '2x8x' + str(round(.7*self.maxs['Benchpress'] + ov, 1)) + ' <br/> '
						    + 'Pull-ups: 4x5x' + str(2.5 * round((.125 * self.maxs['Pullup'] + pullov) / 2.5, 1)) + ' <br/> '
							+ 'Abs: 3x12x' + 'X']

				dayTwo = ['Squat: 3x6x' + str(2.5 * round((.76*self.maxs['Squat'] + ov) / 2.5, 1))+ ' <br/> '
	  	 				    + 'Benchpress: 4x3x' + str(2.5 * round((.81 * self.maxs['Benchpress'] + ov) / 2.5, 1)) + ' <br/> '
						    + 'Pull-ups: 3x5x' + str(2.5 * round((.125 * self.maxs['Pullup'] + pullov) / 2.5, 1)) + ' <br/> '
							+ 'Calf Raises: 3x12x' + 'X'  + ' <br/> ']

				dayThree = ['Deadlift: 4x5x' + str(2.5 * round((.81 * self.maxs['Deadlift'] + ov) / 2.5, 1))+ ' <br/> '
							+ 'Benchpress: 3x8x' + str(2.5 * round((.73*self.maxs['Benchpress'] + ov) / 2.5, 1)) + ' <br/> '
							+ 'Pull-ups: 3x5x' + str(2.5 * round((.125 * self.maxs['Pullup'] + pullov) / 2.5, 1)) + ' <br/> '
							+ 'Abs: 3x12x' + 'X' + ' <br/> '
							+ 'Calf Raises: 3x12x' + 'X'  + ' <br/> ']

				week = '*Week*: ' + str(i+1)
				self.program[week] = {'Day One' : dayOne, 'Day Two' : dayTwo, 'Day Three' : dayThree}

	def markdownSummary(self):
		file_name = '_plaene/Trainingsplan_' + self.name + '_' + str(date.today())
		mdFile = MdUtils(file_name=file_name)

		mdFile.new_header(level=1, title='Trainingsplan: ' + self.name)
		mdFile.new_header(level=2, title='Überblick')
		tableOne = ["Name", "Geschlecht", "Größe<br/>[cm]", 'Gewicht<br/>[Kg]', 'Alter', 'BMR*1.5<br/>[KCal]', 'Protein pro Tag<br/>[g]', 'BMI', 'Overload<br/>[Kg]']
		tableOne.extend([str(i) for i in self.summary[0:9]])
		mdFile.new_line()
		mdFile.new_table(columns=9, rows=2, text=tableOne, text_align='center')


		mdFile.new_header(level=2, title='AMRAP-Test')
		tableTwo = [i for i in self.test]
		tableTwo.insert(0, ' ')
		tableTwo.extend(['Test<br/>[Reps@Weight]'] + [str(self.test[i][::-1]) for i in self.test])
		tableTwo.extend(['1RM-estimate<br/>[Kg]'] + [str(self.maxs[i]) for i in self.maxs])
		tableTwo.extend(['Bw%'])
		tableTwo.extend(str(round(i / self.m, 2)) for i in self.maxs.values())
		mdFile.new_line()
		mdFile.new_table(columns=5, rows=4, text=tableTwo, text_align='center')

		
		mdFile.new_header(level=2, title='Plan')

		for x in self.program:
			tablePlan = [' '] + [i for i in self.program[x]]
			tablePlan.extend([x + '<br/>[Sets x Reps x Weight]'] + [str(self.program[x][i])[1:-1].strip("'") for i in self.program[x]])
			mdFile.new_line()
			mdFile.new_table(columns=self.days+1, rows=2, text=tablePlan, text_align='center')


		tableComment = '*<sup>1</sup>Topset: Schweres Set am Anfang; Freiwillig, und nicht jede Woche.*<br/>' \
					   '*Wenn Gewichte auf dem Plan nicht genau auf die Stange gehen, das was am nächsten dran ist benutzen.*'
		mdFile.new_line(tableComment)
		tableComment2 = 'Infos zu den Exercises:<br> [Benchpress](https://exrx.net/WeightExercises/PectoralSternal/BBBenchPress),' \
						' [Deadlift](https://exrx.net/WeightExercises/GluteusMaximus/BBDeadlift),' \
						' [Squat](https://exrx.net/WeightExercises/Quadriceps/BBSquat),' \
						' [Pullup](https://exrx.net/WeightExercises/LatissimusDorsi/WtPullup),' \
						' [Abs](https://exrx.net/WeightExercises/RectusAbdominis/CBKneelingCrunch)'
		mdFile.new_line(tableComment2)


		mdFile.create_md_file()

if __name__ == '__main__':
	rm = {'Benchpress':(70, 6),'Squat' : (75, 6), 'Deadlift' : (120, 8), 'Pullup' : (120, 8)}

	x = TrainingCalc('Till', 'm', 180, 81, 22, rm, 2)