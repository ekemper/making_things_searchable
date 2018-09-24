import unittest
import esApi

class esApiTest(unittest.TestCase):    

    def test_createIndex(self):
        createIndexResponse = esApi.createIndex() # this will use the default args
        expectedText = '{"acknowledged":true,"shards_acknowledged":true,"index":"new_index_name"}'
        assert(createIndexResponse.text == expectedText)

    def test_deleteIndex(self):
        deleteIndexResponse = esApi.deleteIndex('new_index_name')
        expectedText = '{"acknowledged":true}'
        assert(deleteIndexResponse.text == expectedText)

if __name__ == '__main__':
    unittest.main()