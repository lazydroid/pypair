#!/usr/bin/env python2

from pypair import Tournament, random

import json, os, sys
import datetime

name_list = '''
1 	James 	4,663,035 	Mary 	3,124,584
2 	Robert 	4,407,377 	Patricia 	1,555,054
3 	John 	4,403,862 	Jennifer 	1,469,031
4 	Michael 	4,340,931 	Linda 	1,448,283
5 	David 	3,564,313 	Elizabeth 	1,411,916
6 	William 	3,524,670 	Barbara 	1,391,959
7 	Richard 	2,439,835 	Susan 	1,103,018
8 	Joseph 	2,317,860 	Jessica 	1,047,000
9 	Thomas 	2,143,281 	Sarah 	989,810
10 	Charles 	2,060,835 	Karen 	986,072
11 	Christopher 	2,044,437 	Lisa 	965,015
12 	Daniel 	1,900,488 	Nancy 	963,833
13 	Matthew 	1,614,109 	Betty 	906,997
14 	Anthony 	1,407,623 	Margaret 	892,334
15 	Mark 	1,348,322 	Sandra 	873,655
16 	Donald 	1,323,467 	Ashley 	851,020
17 	Steven 	1,283,686 	Kimberly 	841,144
18 	Paul 	1,263,912 	Emily 	835,442
19 	Andrew 	1,255,723 	Donna 	821,223
20 	Joshua 	1,226,213 	Michelle 	813,153
21 	Kenneth 	1,212,646 	Carol 	804,807
22 	Kevin 	1,176,784 	Amanda 	773,501
23 	Brian 	1,169,267 	Dorothy 	772,958
24 	George 	1,110,560 	Melissa 	754,784
25 	Timothy 	1,072,620 	Deborah 	740,223
26 	Ronald 	1,072,270 	Stephanie 	738,905
27 	Edward 	1,060,576 	Rebecca 	729,447
28 	Jason 	1,041,127 	Sharon 	720,831
29 	Jeffrey 	976,651 	Laura 	714,847
30 	Ryan 	947,756 	Cynthia 	705,778
31 	Jacob 	941,181 	Kathleen 	683,064
32 	Gary 	900,277 	Amy 	682,347
33 	Nicholas 	896,856 	Angela 	659,597
34 	Eric 	880,874 	Shirley 	657,764
35 	Jonathan 	853,162 	Anna 	607,022
36 	Stephen 	838,395 	Brenda 	606,299
37 	Larry 	802,063 	Pamela 	592,699
38 	Justin 	781,577 	Emma 	591,173
39 	Scott 	770,208 	Nicole 	590,414
40 	Brandon 	763,634 	Helen 	584,461
41 	Benjamin 	749,881 	Samantha 	581,626
42 	Samuel 	717,912 	Katherine 	568,258
43 	Gregory 	707,931 	Christine 	558,861
44 	Alexander 	683,727 	Debra 	548,281
45 	Frank 	675,530 	Rachel 	545,873
46 	Patrick 	665,520 	Carolyn 	539,223
47 	Raymond 	657,165 	Janet 	537,105
48 	Jack 	635,483 	Catherine 	534,876
49 	Dennis 	610,810 	Maria 	529,993
50 	Jerry 	601,368 	Heather 	524,171
51 	Tyler 	594,971 	Diane 	515,112
52 	Aaron 	588,205 	Ruth 	514,443
53 	Jose 	565,276 	Julie 	506,856
54 	Adam 	557,653 	Olivia 	498,779
55 	Nathan 	554,162 	Joyce 	497,784
56 	Henry 	552,869 	Virginia 	496,631
57 	Douglas 	546,783 	Victoria 	489,302
58 	Zachary 	543,288 	Kelly 	471,945
59 	Peter 	537,153 	Lauren 	471,879
60 	Kyle 	482,101 	Christina 	471,224
61 	Ethan 	453,826 	Joan 	465,670
62 	Walter 	452,806 	Evelyn 	457,188
63 	Noah 	445,870 	Judith 	449,739
64 	Jeremy 	440,663 	Megan 	438,147
65 	Christian 	434,517 	Andrea 	437,735
66 	Keith 	430,900 	Cheryl 	436,888
67 	Roger 	427,016 	Hannah 	435,256
68 	Terry 	422,105 	Jacqueline 	420,410
69 	Gerald 	421,918 	Martha 	417,402
70 	Harold 	421,631 	Gloria 	406,375
71 	Sean 	420,553 	Teresa 	403,870
72 	Austin 	418,592 	Ann 	402,317
73 	Carl 	418,263 	Sara 	400,065
74 	Arthur 	399,784 	Madison 	399,308
75 	Lawrence 	396,484 	Frances 	399,109
76 	Dylan 	390,694 	Kathryn 	398,924
77 	Jesse 	387,393 	Janice 	398,820
78 	Jordan 	386,325 	Jean 	390,826
79 	Bryan 	383,979 	Abigail 	388,793
80 	Billy 	376,747 	Alice 	387,931
81 	Joe 	376,613 	Julia 	378,548
82 	Bruce 	375,068 	Judy 	377,609
83 	Gabriel 	366,152 	Sophia 	376,519
84 	Logan 	359,286 	Grace 	376,006
85 	Albert 	358,151 	Denise 	371,271
86 	Willie 	354,624 	Amber 	371,156
87 	Alan 	351,694 	Doris 	370,008
88 	Juan 	349,098 	Marilyn 	369,504
89 	Wayne 	335,173 	Danielle 	369,198
90 	Elijah 	329,248 	Beverly 	368,510
91 	Randy 	328,337 	Isabella 	365,383
92 	Roy 	326,203 	Theresa 	364,816
93 	Vincent 	323,623 	Diana 	360,717
94 	Ralph 	321,289 	Natalie 	359,738
95 	Eugene 	316,285 	Brittany 	359,143
96 	Russell 	315,198 	Charlotte 	357,576
97 	Bobby 	313,130 	Marie 	349,383
98 	Mason 	312,464 	Kayla 	341,740
99 	Philip 	311,366 	Alexis 	341,562
100 	Louis 	308,706 	Lori 	337,993
'''

names = [n.split()[1] for n in name_list.split('\n') if len(n) > 5]

names = [ 'Yuta', 'Liu, An-Chi', 'Mirai', 'Kazuki Tsurumi', 'Devwrat', 'lenik', 'Andrew Huie', 'yoshiki', 'Divyansh', 'puttichai', 'Takeshi', 'Yuto', 'Gabriel', 'Sergey', 'jeonghyun', 'Faizan' ]
names = [ 'Yuta', 'Liu, An-Chi', 'Mirai', 'Kazuki Tsurumi', 'Devwrat', 'lenik', 'Andrew Huie', 'yoshiki', 'puttichai', 'Takeshi', 'Yuto', 'Gabriel', 'Sergey', 'jeonghyun', 'Faizan' ]

Players = { a+1:b for a,b in enumerate(names[:20]) }
#print( Players )
#sys.exit(1)

# { 1:"Tim",
#            2:"Jeff",
#            3:"Kristi",
#            4:"Jacob",
#            5:"Doug",
#            6:"Karen",
#            7:"David"}

def load_the_most_recent(folder = '.') :
	r, d, files = os.walk( folder ).next()
	files = [f for f in files if f.endswith('.json') and f.startswith('match_')]

	if len(files) == 0 :
		return {}

	files.sort()

	print 'loading', files[-1]
	with open( files[-1] ) as fin :
		return json.load( fin )

if __name__ == '__main__' :

	to = Tournament()

	if len(sys.argv) > 1 :
		print 'loading:', sys.argv[1]
		with open( sys.argv[1] ) as fin:
			recent = json.load( fin )
	else :
		recent = load_the_most_recent('.')

	if len(recent) == 0 :
		print 'generating random players'
		for player in Players:
			to.addPlayer( player, Players[player] )
	else:
		to.assign( recent )


	def print_standing() :
		data = [ [key, to.playersDict[key]['Name'],  to.playersDict[key]['Points'],  to.playersDict[key]['OMW%']] for key in sorted(to.playersDict.keys()) ]
		data.sort( key=lambda x : x[2] + float(x[3]), reverse=True )
		for d in data :
			print d[0], d[1], d[2], d[3]

	# round 1
#	to.reportMatch(1, [0,2,0])
#	to.reportMatch(2, [0,2,0])
#	to.reportMatch(3, [0,2,0])
#	to.reportMatch(4, [2,0,0])
#	to.reportMatch(5, [2,0,0])
#	to.reportMatch(6, [2,0,0])
#	to.reportMatch(7, [2,0,0])

	# round 2
#	to.reportMatch(1, [2,0,0])
#	to.reportMatch(2, [2,0,0])
#	to.reportMatch(3, [0,2,0])
#	to.reportMatch(4, [2,0,0])
#	to.reportMatch(5, [0,2,0])
#	to.reportMatch(6, [2,0,0])
#	to.reportMatch(7, [2,0,0])

	# round 3
#	to.reportMatch(1, [0,2,0])
#	to.reportMatch(2, [0,2,0])
#	to.reportMatch(3, [2,0,0])
#	to.reportMatch(4, [2,0,0])
#	to.reportMatch(5, [2,0,0])
#	to.reportMatch(6, [2,0,0])
#	to.reportMatch(7, [0,2,0])

	# round 4
#	to.reportMatch(1, [0,2,0])
#	to.reportMatch(2, [0,2,0])
#	to.reportMatch(3, [2,0,0])
#	to.reportMatch(4, [0,2,0])
#	to.reportMatch(5, [2,0,0])
#	to.reportMatch(6, [0,2,0])
#	to.reportMatch(7, [2,0,0])

	# round 5
#	to.reportMatch(1, [0,2,0])
#	to.reportMatch(2, [2,0,0])
#	to.reportMatch(3, [0,2,0])
#	to.reportMatch(4, [2,0,0])
#	to.reportMatch(5, [2,0,0])
#	to.reportMatch(6, [2,0,0])
#	to.reportMatch(7, [2,0,0])

#	print_standing()
#	sys.exit(1)

	pairings = to.pairRound()

	print( pairings )

	for key in sorted(pairings.keys()) :
		p1 = to.playersDict[pairings[key][0]]['Name']
		p2 = to.playersDict[pairings[key][1]]['Name']
		print( "%2d %15s %s" % (key, p1, p2 ))

	'''
	while len(to.tablesOut) :
		table = to.tablesOut[-1]
		to.reportMatch(table, [2,0,0])

	pairings = to.pairRound()

	print( pairings )

	print_standing()
	'''

	now = datetime.datetime.now()
	suffix = now.strftime( '%Y-%m-%d_%H%M%S' )
	with open( 'match_%s.json' % suffix, 'w' ) as fout:
		to.save( fout )

'''
	for _ in range(4) :

		pairings = to.pairRound()

		print( pairings )

		for key in sorted(pairings.keys()) :
			p1 = to.playersDict[pairings[key][0]]['Name']
			p2 = to.playersDict[pairings[key][1]]['Name']
			print( "%2d %15s %s" % (key, p1, p2 ))

		for table in pairings:
			if not type(pairings[table]) is str:
				per = random.randint(1, 100)
				if per < 25:
				    to.reportMatch(table, [2,0,0])
				elif per < 47:
				    to.reportMatch(table, [2,1,0])
				elif per < 60:
				    to.reportMatch(table, [0,2,0])
				elif per < 97:
				    to.reportMatch(table, [1,2,0])
				elif per < 98:
				    to.reportMatch(table, [0,0,1])
				else:
				    to.reportMatch(table, [1,1,1])


		#print( json.dumps( to.playersDict, indent=4 ))

'''
