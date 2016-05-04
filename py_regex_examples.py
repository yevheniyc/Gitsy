'''
	py_regex_examples.py - Yevheniy Chuba - 04/29/2016

	Summary of regex module with practical examples.
	Following: https://automatetheboringstuff.com/chapter7/

'''


import re

def re_group():
	phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	mo = phoneNumRegex.search('My number is 415-555-4252.')
	print mo.group(1) # '415'
	print mo.group(2) # '555-4242'
	print mo.group(0) # '415-555-4242'
	print mo.groups() # ('415', '555-4242')

	phoneNumRegex_2 = re.compile(r'(\(\d\d\d\))) (\d\d\d-\d\d\d\d)') # escape parentathes
	mo = phoneNumRegex.search('My number is (415) 555-4252.')
	print mo.group(1) # '415'
	print mo.group(2) # '555-4242'
	print mo.group(0) # '415-555-4242'
	print mo.groups() # ('415', '555-4242')


def re_multi_group():
	heroRegex = re.compile(r'Batman|Tina Fey')
	mo = heroRegex.search('Batman and Tina Fey')
	print mo.group() # Batman

	batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # match either of the groups
	mo_2 = batRegex.search('Batmobile lost a wheel')
	print mo_2.group()  # Batmobile
	print mo_2.group(1) # mobile

	batRegexOptional = re.compile(r'Bat(wo)?man') # optional group to mach with "(pattern)?"
	mo_3 = batRegexOptional.search('The Advantures of Batman')
	mo_4 = batRegexOptional.search('The Advantures of Batwoman')
	print mo_3.group()  # Batman 
	print mo_4.group()  # Batwoman
