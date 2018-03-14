import pygal  # First import pygal
import plotly


class Graph():

	#Ryan
    def create_pie(self, all_my_employees, type):
        type = type.lower()
        if type == 'bmi':
            normal = 0
            under_weight = 0
            over_weight = 0
            obesity = 0
            for emp in all_my_employees:
                if emp.bmi == 'Normal':
                    normal += 1
                elif emp.bmi == 'Underweight':
                    under_weight += 1
                elif emp.bmi == 'Overweight,':
                    over_weight += 1
                elif emp.bmi == 'Obesity':
                    obesity += 1
            fig = {
                'data': [{'labels': ['Normal', 'Underweight', 'Overweight, Obesity'],
                          'values': [normal, under_weight, over_weight, obesity ],
                          'type': 'pie'}],
                'layout': {
                    'title': 'BMIs of employees percentage'}
            }

            plotly.offline.plot(fig)

        elif type == 'gender':
            male = 0
            female = 0
            for emp in all_my_employees:
                if emp.gender == 'M':
                    male += 1
                elif emp.gender == 'F':
                    female += 1
            fig = {
                'data': [{'labels': ['Male', 'Female'],
                          'values': [male, female],
                          'type': 'pie'}],
                'layout': {
                    'title': 'comparison of employees genders'}
            }

            plotly.offline.plot(fig)
		
	#Alex
	def create_bar():
		pass
		
	#Kate
	def create_scatter():
		pass
