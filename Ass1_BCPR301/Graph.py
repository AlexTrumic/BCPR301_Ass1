import plotly as plt
import plotly.graph_objs as go

class Graph():

	#Ryan
	def Create_Pie():
		pass
		
	#Alex
	def Create_Bar():
		pass
		
	#Kate
	def Create_Scatter(self, data1, data2):
        data = go.Scatter(
            x = data,
            y = data2,
            mode = 'markers'
        )

        self.graph = plt.iplot(data, filename='scatter-plot')