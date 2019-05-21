import Classes

#Section is an area of the store a sales assosciate is responsible for
#Each section has a name and what aisles are in that section
section_0 = Classes.Section(0,'none',[[0,0]])
section_1 = Classes.Section(1,'Sports/Auto',[[1,35]])
section_2 = Classes.Section(2,'Home/Seasonal',[[44,84],[97,111]])
section_3 = Classes.Section(3,'Seasonal/Decor',[[64,84],[97,111]])
section_4 = Classes.Section(4,'Sports',[[21,22],[26,43]])
section_5 = Classes.Section(5,'Auto',[[1,20],[23,25]])
section_6 = Classes.Section(6,'Home Improvement',[[44,84]])
section_7 = Classes.Section(7,'Seasonal',[[97,111]])
section_8 = Classes.Section(8,'Kitchen Place',[[75,84]])
section_9 = Classes.Section(9,'Parts Desk',[[9,14]])
section_10 = Classes.Section(10,'Kid Zone',[[31,35]])
section_11 = Classes.Section(11,'Paint and Tools',[[44,54]])
section_12 = Classes.Section(12,'Patio / BBQ',[[97,101]])
section_Z = Classes.Section('Z','facing',[[0,0]])
section_num = Classes.Section('/#','num',[[0,0]])

#Store is currently just a list of sections
#But it seems like it should be an object
store_ct457 = Classes.Store('ct457',[section_0,section_1,section_2,section_3,section_4,section_5,section_6,section_7,section_8,section_9,section_10,section_11,section_12,section_Z])