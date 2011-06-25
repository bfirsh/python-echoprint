import echoprint
import simplejson
import unittest

class EchoprintTest(unittest.TestCase):
    def test_codegen(self):
        d = echoprint.codegen(simplejson.load(open('test_data.json')))
        self.assertEqual(d['code'], 'eJydz7sNAzAIRdGV-GPGiQHvP0KcypVdpDnNFUIPANDhAdWL963AC7T_YbrSnjJMocwJo7Qy5FAELdcqtpBt6Ezu38I0r4MH7e-3iroTDooJAZO7LO2AWeszaBXyXt_anXgQlcBr_QIy12Qh')
        self.assertEqual(d['version'], '4.11')

