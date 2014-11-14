Documentation for Project 1
13302010039 TongZhongyi

The project is written in Python!
I. Analysis work
The profile is done instructed by the following step:
1. Insert into trees the data in the file 1_initial.txt
2. Delete the data in the file 2_delete.txt
3. Add the data in the file 3_insert.txt
4. Query a word
5. Query some words
and here are some noticeable information:
	In the first three steps, time is counted every 200 piece of data. 
	The data source of step 4 is randomly selected words, including some in the tree and some not in the tree.
	The search range in step 5 is from ‘b’ to ‘h’.
	The test procedure and test data set of B tree and Red-Black Tree are virtually the same.
	The time unit is clock.
The table below compares the running time of two data structures.
Clock(s)	B Tree	Red-Black Tree
Step 1: Initialize	0.35945442027343133	0.25324512600334415
Step 2: Delete	0.10402192924312464	10.527893501195248
Step 3: Insert	0.052400542244155246	0.037831793126157365
Step 4: Naïve search	0.0016083440599035104	0.0017657146033887017
Step 5: Range search	0.16599128475087987	1.0174142480211081
Red-Black Tree is roughly competitive as B Tree in insertion and naïve search, and may even be slightly better. However, as deletion and range search are concerned, its speed is far behind B tree. This indicates B tree is more competitive in maintaining large pieces of data.

However, the running time is affected by some implementation details, which may differ from person to person. So the test result may be different compared to that of another implementation.

II. Code Structure
	batch >>1_initial.txt; 2_delete.txt; 3_insert.txt; 4_search.txt; i.txt ; ii.txt ; preorder.txt
	 core>>B_Tree.py; dal.py; RB_Tree.py
	__init__.py
	AnalysisUtil.py
	DicMain.py
	DicTest.py
	The program starts with __init__.py. batch folder contains given and self-defined test data. core folder contains two tree objects and dal.py. dal.py is a data access layer, which communicates with user interaface and data. DicMain.py and DicTest.py are graphic interfaces for dictionary and vocabulary.





III. Features
	The dictionary supports:
	bulk deletions/ insertions from file
	insertion/deletion of a single word
	search a single world
	search in a given range, e.g. ‘apple >> banana’
	switch between B Tree and red-Black Tree
	Bonus feature: vocabulary test. Given a word and select correct meaning from four choices.
Besides, the back-end supports preorder traversal the tree into batch/preorder.txt. Attention: The feature is triggered by __str__() instead of preoder_traversal()!
Following are snapshots of some features.
 
 
 
 
Appendix I. Raw data of analysis work
D:\Python34\python.exe D:/Users/Tong/PycharmProjects/MyDictionary/AnalysisUtil.py
# B tree
# Each clock interval for initializing 200 pieces of words.
[4.2763734642473794e-07, 0.01263240721338676, 0.026255222521093212, 0.04007774446958002, 0.05372108636991486, 0.0692019859478368, 0.08541542830018431, 0.1013295245100345, 0.11801849959160633, 0.13304738649435732, 0.15086190307171907, 0.16949662807952345, 0.1897747634096381, 0.2026398053394799, 0.2161924881223727, 0.22882318478637376, 0.2445978712212895, 0.2585482567363573, 0.2720141291379259, 0.28853119400623495, 0.30259362050606603, 0.3181874163434441, 0.3321856972413115, 0.34616644500797544, 0.35945484791077775]
# Each clock interval for deleting 200 pieces of words.
[0.37349974127940544, 0.39492822107140263, 0.41764731037490965, 0.4467920784457948, 0.4775216705225301]
# Each clock time for inserting 200 pieces of words.
[0.5093468694808055, 0.5220335866371882, 0.5348605688431982, 0.5485500955769469, 0.5617474117249608]
# Each clock interval for searching one single word.
[0.5748621938651146, 0.5750208473206382, 0.5752449292901648, 0.5753300291221033, 0.5754121354926168, 0.5754643072488806, 0.5755246041147265, 0.5756037170238151, 0.5756571716921182, 0.5757375675132461, 0.5758051342139812, 0.5758889511338804, 0.5761232963997212, 0.5761985605726919, 0.5762695483721985, 0.5763187266670373, 0.5763986948508187, 0.5764705379250181]
# Clock interval for searching in a range.
[0.57656718396531, 0.7425584687161899]
# Red-Black tree
# Each clock interval for initializing 200 pieces of words.
[0.8197829312829548, 0.8302014599539007, 0.8384450250809303, 0.8477452820909755, 0.8581971664749426, 0.8670962996540413, 0.8771124215820016, 0.8860658647040963, 0.8963052133268903, 0.9051209572234362, 0.9146102299406011, 0.9238424926125648, 0.93657197350359, 0.9486351954088854, 0.9631397989249197, 0.9791954430964365, 0.988812151742836, 0.998426294565157, 1.0094234165658156, 1.018778411156203, 1.0298422445829039, 1.0399657034848167, 1.0522397506018997, 1.0628780848689077, 1.073028057286299]
# Each clock interval for deleting 200 pieces of words.
[1.081706957231989, 3.337879688508957, 6.2202623127482966, 9.68106934994847, 11.609600458427236]
# Each clock time for inserting 200 pieces of words.
[13.672079130014582, 13.680303023823676, 13.690709151011577, 13.699874702257498, 13.70991092314074]
# Each clock interval for searching one single word.
[13.719306543279037, 13.719444670141932, 13.719564836236279, 13.719658916452492, 13.71974145046035, 13.7198432281488, 13.719927900343393, 13.720030533306534, 13.720140008467219, 13.72024991126525, 13.72032432016353, 13.7204355058736, 13.720536000650009, 13.720621100481948, 13.720719884708972, 13.720836629704545, 13.720967486732551, 13.721072257882426]
# Clock interval for searching in a range.
[13.72112785073746, 14.738542098758568]
