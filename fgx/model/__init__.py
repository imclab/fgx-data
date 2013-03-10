##@package fgx.model
# @brief The database and model configuration is different from the default pylons app 
#        bacause it contains more than one db connection.






from fgx.model.meta import Sess, Base


from fgx.model.navdata import *
from fgx.model.users import *
from fgx.model.mpnet import *
		


def init_model(engines):
	"""Initialises and binds engines to the Sess
	
	      Args: TODo
			engines (class): an Object with the container
	"""
	Sess.navdata.configure(bind=engines.navdata)
	Sess.users.configure(bind=engines.users)
	Sess.mpnet.configure(bind=engines.mpnet)



