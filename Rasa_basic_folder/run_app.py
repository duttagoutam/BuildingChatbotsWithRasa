#from rasa_core.channels.channel import HttpInputChannel
from rasa_core.channels.channel import InputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-455545604819-456694959687-456937338551-fd82f8366e835c911a7dad05df8bd26b', #app verification token
							'xoxb-455545604819-455274087745-yZAhjiiLWrrihtCLNq5sR6ul', # bot verification token
							'X1R7CUdbr2xrFQYlSk0u0hqz', # slack verification token
							True)

agent.handle_channels([input_channel],5004, True)
