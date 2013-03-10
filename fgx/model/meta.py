##@package fgx.model.meta 
# @brief SQLAlchemy Metadata and Session objects
#
# The meta is the typical way to access sqlAlchemy sessions and the isntances within.
# @example from fgx.model import meta
#         

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


#__all__ = ['Base', 'Sess']

class DbConnectionsContainer():
	"""A class to hold the database connections, sessions and metadata
	
		.. note::
			This class is a container that is passed around
	"""
	def __init__(self):
		
		
		self.navdata = None
		""".. attribute:: Navdata and "postgis" database with navigation data imported and processed
		
			.. note:: This is expected to be a readonly 'spacial' data, eg postgis
		"""
		
		
		self.users = None
		""".. attribute:: Users info and profile, shared data etc
		
			.. note:: Read and Write DB and user authenticalion, meta etc
		"""
		
		
		self.mpnet = None
		""".. attribute:: Tracker and multiplayer database
		
			.. note:: Fast writes by webserver of data, and crossfeed
		"""
		
		
##@brief The sqlalchemy database Sessions/connecctions
#
# @see fgx.model.init_model()
Sess = DbConnectionsContainer()
""" The sqlalchemy database Sessions/connections instance of :py:func:`fgx.model.meta.DbConnectionsContainer`
	
	These are scoped_session's that are passed around
	
	.. seealso:: :py:func:`fgx.model.init_model`   
"""
Sess.navdata = scoped_session(sessionmaker())
Sess.users = scoped_session(sessionmaker())
Sess.mpnet = scoped_session(sessionmaker())


## The declarative Base for ORM access
Base = DbConnectionsContainer()
Base.navdata = declarative_base()
Base.users = declarative_base()


Base.mpnet = declarative_base()






#########################################################
## pete's data helpers
#########################################################
def select_sql(cmap):
	lst = cmap.replace("\t", "").strip().replace("\n", "").split(" ")
	arrc = [ s.strip() for s in lst]
	cols = []
	sqls = []
	for colr in arrc:
		col = colr.strip()
		if len(col) > 0:
			if col.find(" as ") > -1:
				p = col.split(" ")
				pp = []
				for pl in p:
					if len(pl) > 0:
						pp.append(pl)
				cols.append(pp[2])
				sqls.append(col)
			else:
				cols.append(col)
				sqls.append(col)
	sql = 'select ' + ", ".join(sqls)
	sql += " " # ta
	return sql, cols
	
def query_to_dic(resultsObj, cols):
	return_list = []
	for r in resultsObj:
		dic = {}
		for c in cols:
			dic[c] = r[c]
		return_list.append(dic)
	return return_list	

	