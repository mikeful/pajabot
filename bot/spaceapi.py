import zerorpc

class SpaceAPI(object):
    def __init__(self, url):
	print "SpaceAPI connecting to " + url
	c = zerorpc.Client()
	c.connect(url)

    def updateStatus(self, labOpen, topic):
	print "Setting lab open " + str(labOpen) + " and topic " + topic
	c.updateStatus(labOpen, topic)
        print "Update ok"

