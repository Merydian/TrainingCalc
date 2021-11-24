from TrainingCalc import TrainingCalc
import pandas as pd 

path = './amrap-Tests/Test_template.csv'
df = pd.read_csv(path, index_col=0, sep=';')

if __name__ == '__main__':
	for i in df:
		human = df[i]
		rm = {'Benchpress':(int(human.benchWeight), int(human.benchReps)),
				'Squat' : (int(human.squatWeight), int(human.squatReps)), 
				'Deadlift' : (int(human.deadWeight), int(human.deadReps)),
				'Pullup' : (int(human.pullupWeight), int(human.pullupReps))}
		x = TrainingCalc(human.name, human.gender, int(human.height), int(human.mass), int(human.age), rm, int(human.days))