
import sys
sys.path.append('..')
import receptor

class testClass:
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_c1(self):
        tobj = receptor.receptor()
        tobj.key_in.set_value(1)
        tobj(1)
        tobj.key_in.set_value(0)
        tobj(1)
        assert(tobj.accumulate_value.get_value()=='0b00000001')
        pass

