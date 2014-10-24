#serialization

import json
import cPickle


json_string = json.dumps([1,2,3,'a', 'b', 'c'])
print json.loads(json_string)


pickled_string = cPickle.dumps([1,2,3, 'a', 'b', 'c'])
print cPickle.loads(pickled_string)
