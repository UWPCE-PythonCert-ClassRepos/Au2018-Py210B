'''
test_mailroom_oo.py:  Tests classes for Object-Oriented Mailroom assignment.
Written by David K. Arasim ~ December 6, 2018
'''

import io
import pytest

from donor_models import *


def test_Donor_class():
    # Adding a Name with no Donation
    d = Donor('Bill Gates')

    print('dict:', d.__dict__) # Shows the whole dict

    print('name:', d.name)
    print('donations:', d.donations)
    print('num_donations:', d.num_donations)
    print('total_donation:', d.total_donation)
    print('avg_donation:', d.avg_donation)
    print('__str__:', d)
    
    assert d.name == 'Bill Gates'
    assert d.donations == []
    assert d.num_donations == 0
    assert d.total_donation == 0
    assert d.avg_donation == 0
    assert str(d) == 'Bill Gates:'
    
    print()

    # Adding a Donation to existing Name with no existing Donation
    d.add_donation(1234)

    print('dict:', d.__dict__) # Shows the whole dict

    print('name:', d.name)
    print('donations:', d.donations)
    print('num_donations:', d.num_donations)
    print('total_donation:', d.total_donation)
    print('avg_donation:', d.avg_donation)
    print('__str__:', d)
    
    assert d.name == 'Bill Gates'
    assert d.donations == [1234]
    assert d.num_donations == 1
    assert d.total_donation == 1234
    assert d.avg_donation == 1234
    assert str(d) == 'Bill Gates:1234.0'

    print()

    # Adding a Name with a Donation (reusing 'd' instance)
    d = Donor('Bill Gates', 1000)

    print('dict:', d.__dict__) # Shows the whole dict

    print('name:', d.name)
    print('donations:', d.donations)
    print('num_donations:', d.num_donations)
    print('total_donation:', d.total_donation)
    print('avg_donation:', d.avg_donation)
    print('__str__:', d)
    
    assert d.name == 'Bill Gates'
    assert d.donations == [1000]
    assert d.num_donations == 1
    assert d.total_donation == 1000
    assert d.avg_donation == 1000
    assert str(d) == 'Bill Gates:1000.0'
    
    print()

    # Adding another Donation to existing Name with existing Donation
    d.add_donation(1234)

    print('dict:', d.__dict__) # Shows the whole dict

    print('name:', d.name)
    print('donations:', d.donations)
    print('num_donations:', d.num_donations)
    print('total_donation:', d.total_donation)
    print('avg_donation:', d.avg_donation)
    print('__str__:', d)
    
    assert d.name == 'Bill Gates'
    assert d.donations == [1000, 1234]
    assert d.num_donations == 2
    assert d.total_donation == 2234
    assert d.avg_donation == 1117
    assert str(d) == 'Bill Gates:1000.0,1234.0'

    print()

#    assert False  # Not an error:  Used to display print() statements above


def test_DonorCollection_class():
    # Testing Donor Collection from default (no file to be imported)
    dc = DonorCollection()
    print('dc.__dict__:', dc.__dict__)
    assert dc.__dict__ == {'donors': {}, 'donor_file': None}

    dc.add_new_donor('Paul Allen')
    print('dict:', dc.__dict__) # Shows the whole dict
    print('get_donor:', dc.get_donor('Paul Allen'))
    assert str(dc.get_donor('Paul Allen')) == 'Paul Allen:'

    dc.add_donation('Paul Allen', 5000)
    print('get_donor:', dc.get_donor('Paul Allen'))
    assert str(dc.get_donor('Paul Allen')) == 'Paul Allen:5000.0'

    dc.add_new_donor('Paul Allen') # Trying to clobber existing Donor record
    print('get_donor:', dc.get_donor('Paul Allen'))
    assert str(dc.get_donor('Paul Allen')) == 'Paul Allen:5000.0'
    
    dc.add_new_donor('Steve Jobs')
    print('dict:', dc.__dict__) # Shows the whole dict
    print('get_donor:', dc.get_donor('Steve Jobs'))
    assert str(dc.get_donor('Steve Jobs')) == 'Steve Jobs:'
    
    dc.add_donation('Warren Buffett', 56789)
    print('dict:', dc.__dict__) # Shows the whole dict
    print('get_donor:', dc.get_donor('Warren Buffett'))
    assert str(dc.get_donor('Warren Buffett')) == 'Warren Buffett:56789.0'

    dc.add_donation('Paul Allen', 4999)
    print('get_donor:', dc.get_donor('Paul Allen'))
    assert str(dc.get_donor('Paul Allen')) == 'Paul Allen:5000.0,4999.0'    

    print('get_donor (Mickey Mouse):', dc.get_donor('Mickey Mouse'))
    assert str(dc.get_donor('Mickey Mouse')) == 'Name not found'

    print('generate_report:\n', dc.generate_report(), sep='')
    print()
    print('generate_list:\n', dc.generate_list(), sep='')

#    assert False  # Not an error:  Used to display print() statements above


def test_DonorCollection_class_file():
    # Testing Donor Collection from imported file and subsequent export to file
    # donors.txt must have 'Bill:1.0,100.0' in it for this test to work!
    dc = DonorCollection('donors.txt')
    print('dc.__dict__:', dc.__dict__)

    print('get_donor:', dc.get_donor('Bill'))
    assert str(dc.get_donor('Bill')) == 'Bill:1.0,100.0'

    dc.add_donation('Ted', 200)
    print('get_donor:', dc.get_donor('Ted'))

    print('get_donor (Mickey Mouse):', dc.get_donor('Mickey Mouse'))
    assert str(dc.get_donor('Mickey Mouse')) == 'Name not found'

    print('generate_report:\n', dc.generate_report(), sep='')
    print()
    print('generate_list:\n', dc.generate_list(), sep='')

    print('saving text file:', dc.build_donor_text())
    
#    assert False  # Not an error:  Used to display print() statements above
