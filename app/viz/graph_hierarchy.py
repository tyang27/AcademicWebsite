from tree import Node
import graphviz as gv
from graphviz import Digraph

dot = Digraph(strict=True)
dot.format = 'svg'

dot.node(' ', color='gray80')

dot.node('Service', color='gray60')
dot.node('Research', color='gray60')
dot.node('Classes', color='gray60')
dot.node('Fun', color='gray60')
dot.edge(' ', 'Service')
dot.edge(' ', 'Research')
dot.edge(' ', 'Classes')
dot.edge(' ', 'Fun')

dot.node('B\'more First', color='gray40')
dot.node('Politics', color='gray40')
dot.node('Health', color='gray40')
dot.node('Wellness', color='gray40')
dot.node('Animation', color='gray40')
dot.edge('Service', 'B\'more First')
dot.edge('Service', 'Politics')
dot.edge('Research', 'Health')
dot.edge('Fun', 'Wellness')
dot.edge('Fun', 'Animation')

dot.edge('Politics', 'NYT')
dot.edge('Politics', 'Letters')
dot.node('Cooking')
dot.node('Exercise')
dot.edge('Wellness', 'Cooking')
dot.edge('Wellness', 'Exercise')

#dot.edge('	', 'Future')
#dot.node('Recruiting')
#dot.node('Patients')
#dot.edge('Future', 'Recruiting')
#dot.edge('Future', 'Patients')

dot.render('hierarchy')
