from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def run_restaurant_online(interpreter, 
	                      domain_file='restaurant_domain.yml',
                          training_data_file='data/stories.md'):

	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()], interpreter=interpreter, action_endpoint=action_endpoint)
	training_data = agent.load_data(training_data_file)
	agent.train(training_data, batch_size=50, epochs=200, max_training_samples=300)
	interactive.run_interactive_learning(agent)
	return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
    run_restaurant_online(nlu_interpreter)
